import requests

class TiebaSpider():

    def __init__(self,kw,maxPage):
        self.maxpage = maxPage
        self.kw = kw
        self.url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko)"
        }
        pass

    def get_urls(self):
        list = []
        for pn in range(0, self.maxpage, 50):
            url = self.url.format(self.kw, pn)
            list.append(url)
        return list

    def get_content(self, url):
        response = requests.get(
            url=url,
            headers=self.headers
        )
        return response.content

    def get_items(self, content, index):
        with open('tieba-{}.html'.format(index), 'wb') as f:
            f.write(content)
        return None

    def run(self):
        urls = self.get_urls()
        for url in urls:
            content = self.get_content(url)
            items = self.get_items(content, urls.index(url) + 1)


if __name__ == '__main__':
    spider = TiebaSpider('英雄联盟', 150)
    spider.run()