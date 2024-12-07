#add import
from question_c import get_stock_list

if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Display stock list")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            stocks = get_stock_list()
            for stock in stocks:
                print(f"{stock.get_symbol()} - {stock.get_company_name()}")
        elif choice == "2":
            break
        else:
            print("Invalid option.")
