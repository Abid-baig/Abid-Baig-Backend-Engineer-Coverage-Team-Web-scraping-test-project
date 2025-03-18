import requests
import logging
from rollee.account import Account
from constants import AUTH_URL, ACCOUNTS_URL_TEMPLATE, CLIENT_ID, SCOPE

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_access_token(username: str, password: str) -> str:
    """Fetches an access token using username and password."""
    payload = {
        'client_id': CLIENT_ID,
        'grant_type': 'password',
        "scope": SCOPE,
        'username': username,
        'password': password
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.post(AUTH_URL, data=payload, headers=headers)
    
    if response.status_code != 200:
        logger.error(f"Authentication failed: {response.text}")
        raise Exception("Invalid credentials or authentication error")
    
    return response.json().get('access_token')

def get_accounts_for_user(username: str, password: str, user_id: str) -> list[Account]:
    """Retrieves accounts associated with a given user ID."""
    access_token = get_access_token(username, password)
    accounts_url = ACCOUNTS_URL_TEMPLATE.format(user_id=user_id)
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }
    
    response = requests.get(accounts_url, headers=headers)
    logger.info(f"Accounts Response Status: {response.status_code}")
    
    if response.status_code != 200:
        logger.error(f"Error fetching accounts: {response.text}")
        raise Exception("User not found or invalid user ID")
    
    try:
        user_data = response.json()
    except ValueError:
        raise Exception("Error: The response was not valid JSON.")
    
    accounts_list = user_data.get("user", {}).get("accounts", [])
    if not accounts_list:
        raise Exception("No accounts found for the user.")
    
    accounts = []
    for account_data in accounts_list:
        if isinstance(account_data, dict):  
            mapped_data = {
                "account_id": account_data.get("id"),
                "name": account_data.get("profile", {}).get("full_name"),
                "email": account_data.get("profile", {}).get("email"),
                "platform_name": account_data.get("platform", {}).get("name"),
                "currency": account_data.get("income", {}).get("currency"),
                "gross_earnings": account_data.get("income", {}).get("gross_earnings"),
                "country": account_data.get("country"),
            }
            try:
                accounts.append(Account(**mapped_data))
            except Exception as e:
                logger.warning(f"Skipping invalid account data: {account_data} - Error: {e}")
    
    return accounts
