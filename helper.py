RESET = "\033[0m"
RED = "\033[91m"
GRAY = "\033[90m"
GREEN = "\033[92m"

def print_info(data):
    print(GRAY + data + RESET)

def print_success(data):
    print(GREEN + data + RESET)

def print_error(data):
    print(RED + data + RESET)