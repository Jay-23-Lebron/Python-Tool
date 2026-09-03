from src.data import Expense
from datetime import datetime


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