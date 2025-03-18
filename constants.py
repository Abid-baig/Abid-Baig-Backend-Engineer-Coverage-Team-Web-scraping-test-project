import os
from dotenv import load_dotenv

load_dotenv()

AUTH_URL = os.getenv("AUTH_URL", "https://keycloak.getrollee.com/realms/rollee/protocol/openid-connect/token")
ACCOUNTS_URL_TEMPLATE = os.getenv("ACCOUNTS_URL_TEMPLATE", "https://api.sand.getrollee.com/api/dashboard/v0.1/views/user/{user_id}?start_date=1268385035&end_date=1741770635")
CLIENT_ID = os.getenv("CLIENT_ID", "dashboard")
SCOPE = os.getenv("SCOPE", "openid profile email")
USERNAME=os.getenv("USERNAME", "engr.abidbaig@gmail.com")
PASSWORD=os.getenv("PASSWORD", "Abid@rollee")
USER_ID=os.getenv("USER_ID", "f1e13e83-fcd6-4990-b18b-022c6fc1ab80")