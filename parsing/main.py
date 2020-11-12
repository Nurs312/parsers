import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find('table', class_='table').find_all('td')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        link = 'http://kenesh.kg' + a
        links.append(link)
        uniques = links[::3]
    for unique in uniques:
        print(unique)


def main():
    url = "http://kenesh.kg/ky/deputy/list/35"
    r_text = get_html(url)
    tables = get_all_links(r_text)
    all_links = tables
    print(all_links)


if __name__ == '__main__':
    main()
