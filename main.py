import requests
from bs4 import BeautifulSoup

# Url to crawl
url = "https://knowthychoice.in/blog/"
req = requests.get(url)
# Variable for final result store
final_res = {}
# Create soup of html content
soup = BeautifulSoup(req.content, 'html.parser')
# get all anchor tags in articles
anchor_soup = soup.select('article a')
href_list = set()
for anchor in anchor_soup:
    href_list.add(anchor.get('href'))
# Similarly, then we will go each url we got.
for e in href_list:
    url = e
    r = requests.get(url)
    # creating soup of each page
    soup = BeautifulSoup(r.content, 'html.parser')
    # get title of each soup
    soup_title = soup.title.string
    concepts_soup = list(
        soup.find(string='Concepts Covered').find_all_next('ul')[0].find_all('li'))
    # Get concepts list from each url using map function
    concepts_list = list(map(lambda x: x.string, concepts_soup))
    # storing result in final_res variable
    final_res[soup_title] = concepts_list

# Finally here's the output
print(final_res)