from api import (
    get_status,
    get_all_products,
    get_product_info,
    save_executive_report_by_scan_id,
    save_executive_details_report_by_scan_id,
    save_engineering_report_by_scan_id
)

# All the three endpoints are tested here
def main():
    get_status()
    
    products = get_all_products()
    first_product = products[0]
    scan_id = first_product["scans"][0]["id"]
    
    get_product_info(first_product["id"])
    
    save_executive_report_by_scan_id(scan_id)
    save_executive_details_report_by_scan_id(scan_id)
    save_engineering_report_by_scan_id(scan_id)


if __name__ == "__main__":
    main()
