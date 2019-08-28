from bs4 import BeautifulSoup
import requests
import xlwt

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

    def get_html(self, urls):
        htmls = []
        try:
            for url in urls:
                response = requests.get(url)
                if response.status_code == 200:
                    htmls.append(response.content)
            return htmls
        except requests.RequestException:
            return None

    def get_content(self, htmls):
        list = []
        for html in htmls:
            soup = BeautifulSoup(html, 'lxml')
            lis = soup.find(class_='article').find_all('li')
            for _li in lis:
                name = _li.find('img').get('alt')
                img = _li.find('img').get('src')
                intro = _li.find(class_='inq').string
                detail_link = _li.find('a').get('href')
                rating = _li.find(class_='rating_num').string
                temp = {'name': name, 'img': img, 'intro': intro, 'detail': detail_link, 'rating': rating}
                list.append(temp)
        return list

    def save_to_excel(self, contents, sheet):
        sheet.write(0, 0, '名称')
        sheet.write(0, 1, '图片')
        sheet.write(0, 2, '简介')
        sheet.write(0, 3, '详情链接')
        sheet.write(0, 4, '评价分数')

        for item in contents:

            _index = contents.index(item) + 1
            sheet.write(_index, 0, item['name'])
            sheet.write(_index, 1, item['img'])
            sheet.write(_index, 2, item['intro'])
            sheet.write(_index, 3, item['detail'])
            sheet.write(_index, 4, item['rating'])


    def run(self):
        movieSheet = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = movieSheet.add_sheet('电影top250' ,cell_overwrite_ok=True)

        urls = self.get_urls()
        htmls = self.get_html(urls)
        contents = self.get_content(htmls)
        self.save_to_excel(contents, sheet)
        movieSheet.save(u'豆瓣最受欢迎的250部电影.xlsx')


if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start={}&filter='
    movie = Movie(url, 25)
    movie.run()
