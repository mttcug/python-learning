import requests, re

class book():

    def __init__(self, url, page):
        self.url = url
        self.page = page

    def get_urls(self):
        url_list = []
        for index in range(1, 26):
            url_link = self.url.format(index)
            url_list.append(url_link)
        return url_list

    def get_book_html(self, _url):
        try:
            response = requests.get(_url)
            if response.status_code == 200:
                return response.content
        except requests.RequestException:
            return None

    def get_books_from_html(self, html):
        pattern = re.compile(
            '<li>.*?list_num.*?(\d+).</div>.*?< img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a >.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
            re.S)
        item = re.findall(pattern, html)
        return item


    def run(self):
        urls = self.get_urls()
        for _url in urls:
            res = self.get_book_html(_url)
            item = self.get_books_from_html(res)
            index = urls.index(_url) + 1
            with open('./books/book{}.html'.format(index), 'wb') as f:
                f.write(res)

if __name__ == '__main__':
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{}'
    spider = book(url, 25)
    spider.run()