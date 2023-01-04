import requests
import pandas as pd
from bs4 import BeautifulSoup

Titles = []

Stars = []

Prices = []

Instocks = []


for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html".format(
        page=page)
    req = requests.get(url)
    soup = BeautifulSoup(req.text)

    for books in soup.find_all("article", {"class": "product_pod"}):

        # print(books.find_all('a')[-1]['title'])
        Titles.append(books.find_all('a')[-1]['title'])

        if books.find("p", {"class": "star-rating One"}):
            #print(1, ": star")
            Stars.append(1)
        elif books.find("p", {"class": "star-rating Two"}):
            #print(2, ": stars")
            Stars.append(2)
        elif books.find("p", {"class": "star-rating Three"}):
            #print(3, ": stars")
            Stars.append(3)
        elif books.find("p", {"class": "star-rating Four"}):
            #print(4, ": stars")
            Stars.append(4)
        elif books.find("p", {"class": "star-rating Five"}):
            #print(5, ": stars")
            Stars.append(5)

        #print(books.find("p", {"class": "price_color"}).text.strip())
        Prices.append(books.find("p", {"class": "price_color"}).text.strip().replace(
            'Â£', ""))

        #print(books.find('p', {"class": "instock"}).text.strip())
        Instocks.append(books.find('p', {"class": "instock"}).text.strip())

    d = {'title': Titles, 'stars': Stars, "prices": Prices, "instock": Instocks}

    df = pd.DataFrame(data=d)

df.astype({"prices": "float"})

df = df.reset_index()

df = df.rename(columns={"index": "id"})

df.to_csv('df_books.csv', index=False)

print(df)
