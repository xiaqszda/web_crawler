from http_util import HttpUtil


if __name__ == "__main__":
    url_path = 'http://news.baidu.com/'
    html = HttpUtil.get_page(url_path)
    print(html)
