import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.naver?code=KPI200"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="type_1")
if table:
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 7 and cols[0].find("a"):
            name = cols[0].get_text(strip=True)
            price = cols[1].get_text(strip=True)
            change = cols[2].find("span", class_="tah").get_text(strip=True) if cols[2].find("span", class_="tah") else ""
            rate = cols[3].find("span", class_="tah").get_text(strip=True) if cols[3].find("span", class_="tah") else ""
            volume = cols[4].get_text(strip=True)
            amount = cols[5].get_text(strip=True)
            market_cap = cols[6].get_text(strip=True)
            print(f"{name} | 현재가: {price} | 전일비: {change} | 등락률: {rate} | 거래량: {volume} | 거래대금: {amount} | 시가총액: {market_cap}")
else:
    print("데이터를 찾을 수 없습니다.")