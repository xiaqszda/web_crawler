import re


class ReUtil:

    @staticmethod
    def get_title(html):
        rule_title = r'<title>(.*?)</title>'
        res = re.search(rule_title, html)
        title = res.group(0)[len(r"<title>"):0 - len(r"</title>")]
        return title

    @staticmethod
    def get_sentence_base_word(html, t):
        rule = r'<' + t + '>(.*?)</' + t + '>'
        res = re.findall(rule, html)
        return res
