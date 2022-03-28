<<<<<<< HEAD
import requests
=======
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

soup = BeautifulSoup(
<<<<<<< HEAD
    html_text,
=======
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    "<html><head><title>Test</title></head>" "<body><h1>Parse me!</h1></body></html>",
)

print(soup.get_text())
