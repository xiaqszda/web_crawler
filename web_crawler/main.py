from http_util import HttpUtil
from re_util import ReUtil


if __name__ == "__main__":
    url_path = 'http://news.baidu.com/'
    html = HttpUtil.get_page(url_path)
    print("该网页标题为:" + ReUtil.get_title(html))
    print(ReUtil.get_sentence_base_word(html, 'li'))
    # print(html)
