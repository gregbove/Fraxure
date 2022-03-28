import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

soup = BeautifulSoup(
    html_text,
    "<html><head><title>Test</title></head>" "<body><h1>Parse me!</h1></body></html>",
)

print(soup.get_text())
