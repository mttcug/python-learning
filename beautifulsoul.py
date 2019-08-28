from bs4 import BeautifulSoup
import requests

class Movie():

    def __init__(self, _url, page):
        self.url = _url
        self.page = page

    def get_urls(self):
        _list = []
        for _sum in range(0, 25*4, 25):
            _url = self.url.format(_sum)
            _list.append(_url)
        return _list

    def get_html(self, _url):
        try:
            response = requests.get(_url)
            if response.status_code == 200:
                return response.content
        except requests.RequestException:
            return None

    def run(self):
        urls = self.get_urls()
        for _url in urls:
            print(_url)
            html = self.get_html(_url)
            index = urls.index(_url) + 1
            with open('./movie/movie{}.html'.format(index), 'wb') as f:
                f.write(html)


if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start={}&filter='
    movie = Movie(url, 25)
    movie.run()