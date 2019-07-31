import requests
import bs4


url = 'https://community.quali.com/ideabox'
ideas = requests.get(
    url=url
)
x = bs4.BeautifulSoup(markup=ideas.content)
x.find_all(
    name
)
pass