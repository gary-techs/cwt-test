import re
RESET = "\033[0m"
GRAY = "\033[90m"
GREEN = "\033[92m"

def print_info(data):
    print(GRAY + data + RESET)

def print_success(data):
    print(GREEN + data + RESET)

def get_file_name_from_header(headers):
    # Extract the file_name from the Content-Disposition header using regex
    match = re.search(
        r"filename=(.*?)(?:;|$)", headers.get("content-disposition")
    )
    return f"{match.group(1)}"

