#!/bin/bash/env python3
# -*- coding: utf-8 -*-


import os
import re
import shutil
import requests
import datetime
import threading
import html2markdown
from bs4 import BeautifulSoup


lock = threading.Lock()


def get_html(url):
    return (requests.get(url).content).decode('utf-8')


def get_article_title(html):
    return ((html.split('<title>')[1]).split('</title>')[0]).split('@')[0]


def get_core_content(html):
    html = html.replace('<!--program-think-->', '')
    html = (html.split("<div class='post-body entry-content'>")[1]).split("<div class='post-copyright'>")[0]
    html = "<div class='post-body entry-content'>" + html + "</div>"
    return html


def convert_html_to_md(html):
    md_text = html2markdown.convert(html)
    md_text = md_text.replace('src="//', 'src="http://')
    return md_text


def write_markdown_file(file_name, md_text):
    with open(file_name, 'w') as f:
        f.write(md_text)


def find_all_non_image_link(md_text):
    links = []
    soup = BeautifulSoup(md_text, features="html5lib")
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    return links


def find_all_image_link(md_text):
    links = []
    soup = BeautifulSoup(md_text, features="html5lib")
    links_html = soup.findAll('img')
    rule = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    for single_link_html in links_html:
        urls = re.findall(rule, str(single_link_html))
        links += urls
    return links


def make_directory(directory, force_empty=False):
    lock.acquire()
    if force_empty and os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)
    if not os.path.exists(directory):
        os.system('mkdir -p ' + directory)
    lock.release()


def extract_image_name_from_link(link):
    return os.path.basename(link)


def download_single_image(link, image_save_path):
    r = requests.get(link, stream=True)

    retry = 0
    while r.status_code != 200:
        retry += 1
        print('Error in download image, retry (%d) %s' % (retry, link))
        r = requests.get(link, stream=True)

    with open(image_save_path + extract_image_name_from_link(link), 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


def download_all_image(image_save_path, links_list):
    make_directory(image_save_path)

    for link in links_list:
        download_single_image(link, image_save_path)


def replace_image_link_in_markdown_text(md_text, image_save_path, links_list):
    for link in links_list:
        md_text = md_text.replace(link, image_save_path + extract_image_name_from_link(link))
    return md_text


def replace_blog_non_image_link_in_markdown_text(md_text, links_list):
    blog_url = 'https://program-think.blogspot.com/'
    for link in links_list:
        if link is None:
            continue
        if link.startswith(blog_url) and len(link) > len(blog_url):
            path = (link.split(blog_url)[1]).split('.html')[0] + '.md'
            md_text = md_text.replace(link, '../../' + path)
    return md_text


def get_md_name_from_url(url):
    split_list = url.split('/')
    return ((split_list[len(split_list) - 1]).split('.html')[0]) + '.md'


def get_copyright_statement(url):
    s = '\n\n\n------------------------------------------------\n\n'
    s += '版权声明本博客所有的原创文章，作者皆保留版权。'
    s += '转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：'
    s += url
    s += '\n'
    return s


def url_to_markdown(url, save_path):
    print('Processing url: %s' % url)
    image_save_path = save_path + "/images/"
    html = get_html(url)
    md_text = convert_html_to_md(get_core_content(html))
    non_image_links = find_all_non_image_link(md_text)
    image_links = find_all_image_link(md_text)
    download_all_image(image_save_path, image_links)
    md_text = replace_blog_non_image_link_in_markdown_text(md_text, non_image_links)
    md_text = replace_image_link_in_markdown_text(md_text, 'images/', image_links)
    title_name = html2markdown.convert(get_article_title(html)).replace('/', '-')
    md_text = '# ' + title_name + '\n\n-----\n\n' + md_text + get_copyright_statement(url)
    write_markdown_file(save_path + '/' + get_md_name_from_url(url), md_text)


def test_url_to_markdown():
    url = 'https://program-think.blogspot.com/2011/06/june-fourth-incident-0.html'
    # url = 'https://program-think.blogspot.com/2018/08/USA-Containment-Strategies-in-Cold-War.html'
    # url = 'https://program-think.blogspot.com/2015/03/weekly-share-82.html'
    # url = 'https://program-think.blogspot.com/2016/01/Taiwan-Political-Movements.html'
    url_to_markdown(url, './')


def find_article_links_in_url(url):
    html = get_html(url)
    pattern = re.compile(r"<h1 class='post-title entry-title'>\n<a href='(.*)'>")
    match_list = pattern.findall(html)
    return match_list


def get_current_year_and_month():
    now = datetime.datetime.now()
    return now.year, now.month


def construct_search_link(year, month):
    return 'https://program-think.blogspot.com/%04d/%02d/' % (year, month)


def download_all_articles_in_url_list(url_list, save_path):
    index = 0
    retry = 0
    list_len = len(url_list)

    while index < list_len:
        try:
            url_to_markdown(url_list[index], save_path)
        except Exception as e:
            retry += 1
            print(e)
            print('Error in downloading %s (index: %d), retry count: %d.' % (url_list[index], index, retry))
            continue
        index += 1
        retry = 0


def download_articles_by_year(start_year, end_year):
    year = start_year
    month = 1
    current_year, current_month = get_current_year_and_month()

    if end_year >= current_year:
        print('Start downloading artcles from %04d-01 to %04d-%02d. ' % (start_year, current_year, current_month))
    else:
        print('Start downloading artcles from %04d-01 to %04d-12. ' % (start_year, end_year))

    while year <= end_year:
        year_dir = '%04d' % year
        make_directory(year_dir, True)

        while ((year != current_year and month <= 12) or (year == current_year and month <= current_month)):
            search_url = construct_search_link(year, month)
            month_dir = '%02d' % month
            make_directory(year_dir + '/' + month_dir, True)
            save_path = year_dir + '/' + month_dir + '/'
            download_all_articles_in_url_list(find_article_links_in_url(search_url), save_path)
            month += 1
        month = 1
        year += 1

    if end_year >= current_year:
        print('Downloading artcles from %04d-01 to %04d-%02d finished.' % (start_year, current_year, current_month))
    else:
        print('Downloading artcles from %04d-01 to %04d-12 finished.' % (start_year, end_year))


def search_and_download_all_articles():
    start_year = 2009
    current_year = get_current_year_and_month()[0]

    thread_list = []

    for year in range(start_year, current_year + 1):
        t = threading.Thread(target=download_articles_by_year, args=(year, year))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    print('Done !')


if __name__ == '__main__':
    # test_url_to_markdown()
    # print(find_article_links_in_url('https://program-think.blogspot.com/2018/07/'))
    search_and_download_all_articles()
