"""
@author: danyil
"""
import json
import requests
from bs4 import BeautifulSoup

start_url = "https://www.1a.ee/c/arvutitehnika-burootarbed/sulearvutid-ja-tarvikud/sulearvutid/373"
res = []


def parse(start_urls):
    """
    Parser method for getting all laptops.

    Parser finds laptop name, price and image.
    """
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Get a list of computers
    computers_list = soup.find_all("div", class_='catalog-taxons-product__hover')

    for computer in computers_list:
        # Extract data
        data = {'Product name': '', 'Price': '', 'Picture href': ''}

        # Get laptop name
        c = computer.find('img', alt=True)
        data['Product name'] = c['alt'].strip().rstrip('"').strip()

        # Get laptop price
        data['Price'] = computer.find("span", class_='catalog-taxons-product-price__item-price').find_next(
            "span").get_text()

        # Get laptop image href
        data['Picture href'] = c['src']
        res.append(data)

    # Recursive call to find computers from next page
    try:
        next_page = soup.find("a", class_='paginator__next')['href']
        if next_page:
            parse('https://www.1a.ee/' + next_page)
    except:
        print("No more pages")

    # Write into json file
    with open("data2.json", "w") as writeJSON:
        json.dump(res, writeJSON, indent=8)


if __name__ == '__main__':
    parse(start_url)
