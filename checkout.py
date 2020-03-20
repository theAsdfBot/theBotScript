#Shopify Checkout Script

import requests
import json
import urllib3


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
            variant = str(variants['id'])
    return variant

def addToCart(session, variant):
    atclink = 'https://kith.com' + '/cart/add.js?quantity=1&id=' + variant

    response = session.get(atclink, verify=False)
    return response

def cartLink(variant):

    #Getting the cart link by putting variant_id to the shopify site
    link = 'https://kith.com' + '/cart/' + variant + ':1'

    return link

def getPaymentToken(card_number, cardholder, expiry_month, expiry_year, cvv):

    # POST information to get the payment token
    link = "https://elb.deposit.shopifycs.com/sessions"

    payload = {
        "credit_card": {
            "number": card_number,
            "name": cardholder,
            "month": expiry_month,
            "year": expiry_year,
            "verification_value": cvv
        }
    }

    r = requests.post(link, json=payload, verify=False)

    # Get the payment token
    payment_token = json.loads(r.text)["id"]

    return payment_token
    
#def autofill_info():


#_________USER SETTING__________________#
email = "test@test.com"
fname = "TestFirst"
lname = "TestLast"
addr1 = "123 St"
addr2 = ""  # Can be left blank
city = "Brooklyn"
state = "NY"
country = "US"
postal_code = "11111"
phone = "7181231234"
card_number = "1234432112344321"  # No spaces
cardholder = "TestFirst TestLast"
exp_m = "02"  # 2 digits
exp_y = "2026"  # 4 digits
cvv = "123"  # 3 digits


#___________________________________________________________________________#
session = requests.session()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


keywords = 'Converse WMNS CPX70 High - White / Blue'
products = getProducts()
product = checkAvailability(products, keywords)
variant = getVariant(product, 11.5)
cartResponse = addToCart(session, variant)
cookies = cartResponse.cookies
payment_token = getPaymentToken(card_number, cardholder, exp_m, exp_y, cvv)

print(payment_token)


