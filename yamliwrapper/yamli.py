import json
import requests


class Transliterator(object):
    def __init__(self, word):
        self.word = word
        self.candidates = self.transliterate(word)

    def transliterate(self, word):
        path = "https://api.yamli.com/transliterate.ashx?word={}&tool=api&account_id=000006&prot=https&hostname=AliMZaini&path=yamli-api&build=5515".format(
            word)
        response = requests.get(path)
        html = response.content
        candidates = json.loads(html.decode("utf-8"))["r"].split("|")
        candidates = list(map(lambda x: x[:-2], candidates))
        return candidates