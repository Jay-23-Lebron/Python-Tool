# Python‑Tools

## Planned Tools
### 1. Bookkeeping Tool
‑ Read & write expense records from local json file
‑ Add new income / expense entries
‑ Filter and query transaction records
‑ Calculate total income and expenditure

### 2. Word‑Frequency Statistics Tool
‑ Read text file content
‑ Count word occurrence frequency
‑ Sort words by frequency
‑ Output top‑N high‑frequency words

## Project Structure
src/
├─ __init__.py
├─ main.py        # Program entry & menu
├─ logic.py       # Core business functions
├─ data.py        # Expense data model, file save & load IO functions
├─ env_verify.py  # Environment verification script
└─ learning_demo.py # Practice script: string, dict, file IO exercises

## Development Status
> Status: Data persistence module finished with error handling, business logic in progress.

## How to Test Data Module
Run the self‑test code of data.py to verify save & load function
```bash
python src/data.py
```

## Update Log
- Refactor `data.py` code format
- Add self‑test block for JSON save & load validation
- Complete basic file persistence for expense records
- Add type hints for save_records and load_records
- Add try-except exception handling for file IO
- Improve docstring and code robustness
- Implement menu option 1: add new expense / income record
- Implement menu option 2: view all billing records, add .gitignore for local data exclusion
- Implement menu option 3: calculate total income, expense and net balance