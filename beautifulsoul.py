from bs4 import BeautifulSoup
import requests
import xlwt

class Movie():

    def __init__(self, _url, page):
        self.url = _url
        self.page = page

    def get_urls(self):
        _list = []
        for _sum in range(0, 25, 25):
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

    def get_content(self, html):
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.select('.article li')
        for li in lis:
            index = lis.index(li) + 1
            pic_link = li.a['href']
            movie_name = li.img['alt']
            img = li.img['src']
            outline = li.select('.inq')[0].get_text()
            self.save_to_excel(index, movie_name, img, outline)

    def save_to_excel(self, index, name, img, outline):
        movie = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = movie.add_sheet('电影top250' ,cell_overwrite_ok=True)

        sheet.write(0, 0, '名称')
        sheet.write(0, 1, '图片')
        sheet.write(0, 2, '简介')

        sheet.write(index, 0, name)
        sheet.write(index, 1, img)
        sheet.write(index, 2, outline)

        movie.save(u'豆瓣最受欢迎的250部电影.xlsx')

    def run(self):
        urls = self.get_urls()
        for _url in urls:
            html = self.get_html(_url)
            self.get_content(html)
            index = urls.index(_url) + 1
            with open('./movie/movie{}.html'.format(index), 'wb') as f:
                f.write(html)


if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start={}&filter='
    movie = Movie(url, 25)
    movie.run()