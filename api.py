import os
import json
import requests
from dotenv import load_dotenv
from helper import print_success, print_error , print_info
# Read environment variables from .env file
load_dotenv()

first_product_id=None
# Set up headers
headers = {
    "Authorization": f"Basic {os.environ['BEARER_TOKEN']}", 
    "CwtLicenseKey": f"{os.environ['CWT_LICENSE_KEY']}"
    }

base_url = os.environ['BASE_URL']
version = os.environ["VERSION"]

def make_request(endpoint, method="GET", data=None):

    url = f"{base_url}{version}{endpoint}"
    print_info("\nFetching " + url)
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data)
    elif method == "PUT":
        response = requests.put(url, headers=headers, json=data)
    else:
        raise ValueError("Invalid HTTP method")
    return response

def get_status():
    endpoint = "/Status"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        result = json.loads(response.text)
        if result['status'] == "OK": 
            print_success(f"Success - GET {endpoint}")

def get_all_products():
    global first_product_id
    endpoint = "/Products"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        products = json.loads(response.text)
        print_success(f"Success - GET {endpoint}")
        first_product_id = products[0]['id']
        for idx, product in enumerate(products):
            print_success(str(idx+1)+". "+ product['title'])

def get_first_product_id():
    global first_product_id
    endpoint = "/Products/s"+str(first_product_id)
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        products = json.loads(response.text)
        print_success(f"Success - GET {endpoint}")
        print_success("Title:- " + products['title'])
        print_success("Lines Of Code:- " + str(products['linesOfCode']))
