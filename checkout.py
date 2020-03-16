#Shopify Checkout Script

import requests
import json

def getProducts():
    #Website you want to use the script on (put before /products.json)
    r = requests.get('https://kith.com/products.json')

    #Getting all the products 
    products = json.loads((r.text))['products']

    return products

def checkAvailability(products, keywords):

    #Going through each product from products
    for product in products:

        #Getting product title from Products
        productname = product['title']

        #Insert Keywords here
        if productname == keywords:
            return product
    return ('Product Unavailable')

def getVariant(product, size):

    #Going through each variants(sizes) of the product
    for variants in product['variants']:
        
        #Getting the actual size from the variants
        size = variants['title']

        #If the size match, it will get the variant_id which is needed for carting
        if size == '11.5':
            variant = variants['id']
        return variant

# def addToCart():

# def cartLink():

# def autofill_info():



keywords = 'Kith x Converse Chuck Taylor All Star 1970 Classics - Salsa / Egret / Natural'
products = getProducts()
product = checkAvailability(products, keywords)
getVariant(product, 11.5)



