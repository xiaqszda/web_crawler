from urllib import request


class HttpUtil:

    @staticmethod
    def get_page(url):
        coon = request.urlopen(url)
        html = coon.read().decode('utf-8')
        return html
