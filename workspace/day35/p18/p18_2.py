#%% 네이버 영화2
from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
result_list = soup.find_all('div',class_='tit3')

movie_in = []
for result in result_list:
    movie_in.append(result.text.strip())
    
for person in movie_in:
    print(person)






