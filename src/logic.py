from datetime import datetime
from src.data import Expense, load_records


def create_bill(
        amount: float,
        trans_time: datetime,
        trans_type: str,
        category: str,
        payer: str,
        remark: str
) ->Expense:
    """
    Create and return a new Expense object with basic business check.
    """
    # Simple business rule validation
    if amount <= 0:
        raise ValueError("Amount cannot be zero or negative.")
    
    if trans_type not in ("income","expense"):
        raise ValueError("Transaction type must be 'income' or 'expense'.")

    # Use the Expense template defined in data.py to create a real bill
    new_expense = Expense(
        amount=amount,
        date_time=trans_time,
        record_type=trans_type,
        counter_party=payer,
        category=category,
        note=remark
    )
    return new_expense


def get_all_records():
    """
    Fetch all billing records from data layer
    return: list of Expense objects
    """
    all_bills = load_records()
    return all_bills


def calculate_total() -> tuple[float, float, float]:
    # Calculate total income, expense and net balance
    records = get_all_records()
    total_income = 0.0
    total_expense = 0.0

    # Accumulate amounts by record type
    for record in records:
        if record.record_type == "income":
            total_income += record.amount
        elif record.record_type == "expense":
            total_expense += record.amount

    balance = total_income - total_expense
    return total_income, total_expense, balance