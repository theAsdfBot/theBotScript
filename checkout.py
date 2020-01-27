#Shopify Checkout Script

import requests
import json

def availabilitycheck():

    r = requests.get('https://kith.com/products.json')

    products = json.loads((r.text))['products']

    for product in products:
        productname = product['title']

        if productname == 'Nike Air Huarache Run DNA - White / University Red':

            producturl = 'https://kith.com/products/' + product['handle']

            return producturl

    return False