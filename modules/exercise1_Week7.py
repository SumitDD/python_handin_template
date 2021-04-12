import bs4
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def soup_from_url():
    # Create a BeautifulSoup Object from the link given above

    r = requests.get('https://www.dba.dk/', headers={'User-Agent': 'Mozilla/5.0'})
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify()[:100])

    # Find all the "Kategorier"

    all_categories = soup.select("li.single")
    for c in all_categories:
        print(c.text)
    
    # Find all the links

    for link in soup.findAll('a'):
        if not str(link.get('href')).startswith('https'):
            continue
        print(link.get('href'))

    # Use selenium to press the "Kategory" link with the name "biler"

    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get("https://www.dba.dk/")
    #browser.implicitly_wait(3)
    link_biler = browser.find_elements_by_link_text('Biler')
    print(link_biler)
    link_biler[0].click()

    # In the category "biler" theres a list with cities to see where the sales of cars is located. 
    # Make a bar plot from lowest to highest showing the amount of car sale in each city
    
    request = requests.get('https://www.dba.dk/biler', headers={'User-Agent': 'Mozilla/5.0'})
    request.raise_for_status()
    soup = bs4.BeautifulSoup(request.text, 'html.parser')

    all_cities = soup.select('nav.row-fluid a')
    print(all_cities)

    all_cars = soup.select('nav.row-fluid small')
    all_cars.pop(0)

    array = []
    for car in all_cars:
        array.append(car.text.split("(")[1].split(")")[0])

    print(array)

soup_from_url()



