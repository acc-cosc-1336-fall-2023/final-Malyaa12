#add import
from question_b import stock_purchase_history

if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Display stock purchase history")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            break
        else:
            print("Invalid option.")
