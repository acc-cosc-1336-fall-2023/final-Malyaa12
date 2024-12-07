#add import
from question_a import create_multiplication_table, display_multiplication_table

if __name__ == "__main__":
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)
        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
