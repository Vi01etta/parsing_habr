import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Физика'}


class Habr_article:

    def habr_text(self):
        response = requests.get(url)
        if not response.ok:
            raise ValueError('no response')
        text = response.text
        soup = BeautifulSoup(text, features='html.parser')
        articles = soup.find_all('article')
        return articles

    # def page(self):
    #     articles = self.habr_text()
    #     for article in articles:
    #         href = article.find('a', class_='post__title_link').attrs.get('href')
    #         text = requests.get(href).text
    #         soup = BeautifulSoup(text, features='html.parser')
    #         my_text = soup.find('div', id="post-content-body")

    def find_art_name(self):
        articles = self.habr_text()
        for article in articles:
            names = {n.text for n in article.find_all('a', class_="post__title_link")}
            for name in names:
                value = name.split()
                split_name = {val for val in value}
            hubs = {h.text for h in article.find_all('a', class_="hub-link")}
            if KEYWORDS & hubs or KEYWORDS & split_name:
                href = article.find('a', class_='post__title_link').attrs.get('href')
                link = article.find('a', class_='post__title_link').text
                date = article.find('span', class_='post__time').text
                print(date, '-', link, '-', href)
        return


if __name__ == '__main__':
    Habr_article().find_art_name()
