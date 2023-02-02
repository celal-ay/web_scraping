
import requests
from bs4 import BeautifulSoup

def getting_page(url):
    
    headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0'}
    response = requests.get(url, headers=headers)
    
    


