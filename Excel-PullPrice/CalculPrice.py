import requests
from bs4 import BeautifulSoup


class Calculate:
    def __init__(self):
        pass

    def CalculateCurrency(self):
        r = requests.get("https://bigpara.hurriyet.com.tr/doviz/merkez-bankasi-doviz-kurlari/")
        soup = BeautifulSoup(r.content, "html.parser")


        ev = soup.find("div",attrs={"id":"content"})

        ev2 = ev.find("div", attrs = {"class":"contentLeft"})

        ev3 = ev2.find("div", attrs = {"class":"contentLeft"})

        ev4 = ev3.find("div", attrs = {"class":"tableCnt"})

        ev5 = ev4.find("div", attrs = {"class":"table wide"})
        ev6 = ev5.find("div", attrs = {"class":"tableBox"})
        ev7 = ev6.find("div", attrs = {"class":"tBody"})

        value = ev7.find("li", attrs={"class":"cell015"}).text

        value = value.replace(",", ".")
        value = float(value)


        return value









