import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.toyotacertified.com/inventory;zipCode=97206;model=Avalon%20Hybrid,Camry%20Hybrid,RAV4%20Hybrid;radius=50")
page_html = BeautifulSoup(response.text, "html.parser")
body = page_html.find_all('body')


print(body)