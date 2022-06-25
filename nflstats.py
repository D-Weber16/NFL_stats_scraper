import requests
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def url_validate(url):
  r = requests.get(url)
  return r.status_code

all_urls = []
columns = []

def build_urls():
  url_prefix = "https://www.nfl.com/stats/player-stats/category/"
  url_suffix = "/REG/all/"

  url_holder = []

  pages = {
    'passing':'passingyards',
    'rushing':'rushingyards',
    'receiving':'receivingreceptions'
  }

  for number in range(2000, 2022):
    for key, value in pages.items():
      url = (f"{url_prefix}{key}/{number}{url_suffix}{value}/DESC")

      print('validating URL: ' + url)
      if url_validate(url) == 200:
        url_holder.append(url)
      else:
        pass


  return(url_holder)

all_urls = build_urls()

driver = webdriver.Firefox() #edit for whichever web browser being used

test_url = all_urls[0]

driver.get(test_url)
header = driver.find_elements(By.CSS_SELECTOR, ("th.header")).text
next_page = driver.find_element(By.XPATH, ("//*[@title = 'Next Page']"))
print(header)
#next_page.click()
