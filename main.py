from api import get_status, get_all_products, get_first_product_id

#All the three endpoints are tested here
def main():
    get_status()
    get_all_products()
    get_first_product_id()

if __name__ == "__main__":
    main()