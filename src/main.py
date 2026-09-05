# Main entry file for the book-keeping tool
from src import logic
from src import data
from datetime import datetime


def main():
    # Load saved bill records from local JSON file when program starts
    record_list = data.load_records()
    # Print startup success message for user
    print("===== Book-keeping Tool Started =====")

    # Keep showing menu until user chooses exit
    while True:
        print("\n===== Main Menu =====")
        print("1. Add a new bill record")
        print("2. View all records")
        print("3. Calculate total income & expense")
        print("4. Filter records by condition")
        print("0. Exit program")
        # Get user menu selection
        choice = input("Please enter your option number: ")

        # Judge which function user selects
        if choice == "1":
            # Get every field from user input
            try:
                amount = float(input("Enter amount: "))
                trans_type = input("Enter type (income / expense): ")
                category = input("Enter category: ")
                payer = input("Enter payer name: ")
                remark = input("Enter remark: ")
                current_time = datetime.now()

                # Call logic function to create a new bill
                new_bill = logic.create_bill(amount, current_time, trans_type, category, payer, remark)
                record_list.append(new_bill)
                data.save_records(record_list)
                print("New bill added successfully!")
            except ValueError:
                print("Amount must be a valid number!")
            
        elif choice == "2":
            # Fetch latest bills
            bill_list = logic.get_all_records()

            if not bill_list:
                print("No billing records found.")
            else:
                print("\n===== All Billing Records =====")
                # Print each bill detail
                for bill in bill_list:
                    print(
                        f"Time: {bill.date_time} | "
                        f"Type: {bill.record_type} | "
                        f"Amount: {bill.amount} | "
                        f"Category: {bill.category} | "
                        f"Payer: {bill.counter_party} | "
                        f"Remark: {bill.note}"
                    )
        elif choice == "3":
            # Get summary data from business logic layer
            total_income, total_expense, balance = logic.calculate_total()

            print("\n===== Income & Expense Summary =====")
            print(f"Total Income: {total_income:.2f}")
            print(f"Total Expense: {total_expense:.2f}")
            print(f"Net Balance: {balance:.2f}")
            
            print("You choose to calculate statistics.")
        elif choice == "4":
            print("You choose to filter records.")
        elif choice =="0":
            print("Program will exit. Goodbye!")
            # Stop the while loop
            break
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    # Trigger the main function to run our program
    main()