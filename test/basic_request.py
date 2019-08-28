import requests
import json

url = 'https://movie.douban.com/j/search_subjects'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

for page_start in range(0, 100, 20):
    params = {
        "type": 'movie',
        "tag": '热门',
        "sort": 'recommend',
        "page_limit": '20',
        "page_start": page_start
    }
    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )

    content = response.content
    string = content.decode('utf-8')
    results = json.loads(string)

    for movie in results["subjects"]:
        print(movie['title'], movie['rate'])