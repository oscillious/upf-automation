import requests
from bs4 import BeautifulSoup

response = requests.get("https://docs.python.org/3/")

soup = BeautifulSoup(response.text, "html.parser")
footers = soup.find_all("div", class_="footer")

for footer in footers:
    footer_part = footer.text.split("Copyright")[1].strip()
    
    print(footer_part.split("2001-")[1].split(",")[0])