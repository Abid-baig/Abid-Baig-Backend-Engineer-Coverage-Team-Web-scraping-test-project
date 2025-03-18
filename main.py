from rollee.solution import get_accounts_for_user
from constants import USERNAME, PASSWORD, USER_ID

try:
    accounts = get_accounts_for_user(USERNAME, PASSWORD, USER_ID)
    accounts_json = [account.model_dump() for account in accounts]
    print(accounts_json)
except Exception as e:
    print(f"Error: {e}")