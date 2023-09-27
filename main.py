from api import get_status, get_all_products, get_product_info

#All the three endpoints are tested here
def main():
    get_status()
    first_product_id = get_all_products()
    get_product_info(first_product_id)

if __name__ == "__main__":
    main()