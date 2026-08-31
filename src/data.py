# Import required built‑in modules
from dataclasses import dataclass
from datetime import datetime
import json
import os


# Data model: represent one expense record
@dataclass
class Expense:
    amount: float
    date_time: datetime
    record_type: str
    counter_party: str
    category: str
    note: str


def save_records(record_list,file_path="expense_data.json"):
    """
    Persist list of Expense objects to local json file on disk
    Args:
        record_list: list of Expense instances
        file_path: target json file path
    """
    # Convert Expense objects into dictionaries, prepare for json storage
    serializable_list = []
    for record in record_list:
        item_dict = {
            "amount": record.amount,
            "date_time": record.date_time.isoformat(),
            "record_type": record.record_type,
            "counter_party": record.counter_party,
            "category": record.category,
            "note": record.note
        }
        serializable_list.append(item_dict)

    # Write dictionary list persistently to hard‑disk json file
    with open(file_path,"w",encoding="utf-8") as f:
        json.dump(serializable_list,f,indent=2)


def load_records(file_path="expense_data.json"):
    """
    Load expense data from json file and convert dictionary back to Expense objects.
    Args:
        file_path: json file path to read
    Returns:
        list[Expense]: empty list if file not found
    """
    # Handle first‑run scenario: json file does not exist on disk
    if not os.path.exists(file_path):
        return []

    # Open file in read‑mode, read raw json content
    with open(file_path,"r",encoding="utf-8") as f:
        raw_list = json.load(f)

    expense_list = []
    # Convert each raw dictionary into real Expense object
    for item in raw_list:
        # Restore datetime object from json‑saved string
        dt = datetime.fromisoformat(item["date_time"])
        exp = Expense(
            amount=item["amount"],
            date_time=dt,
            record_type=item["record_type"],
            counter_party=item["counter_party"],
            category=item["category"],
            note=item["note"]
        )
        expense_list.append(exp)

    # Return fully converted bill‑object list for upper‑level program logic
    return expense_list


if __name__ == "__main__":
    test_time = datetime.now()
    test_bill = Expense(100.5, test_time, "expense", "Shop", "Food", "Lunch")
    save_records([test_bill])
    data = load_records()
    print(data)