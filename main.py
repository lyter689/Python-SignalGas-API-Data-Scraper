import requests

# Login
login_url = 'https://app.signalgas.io/api/v1/customer/signin'
login_payload = {
    "email": "travismuley@gmail.com",
    "password": "123"
}
login_response = requests.post(login_url, json=login_payload)
login_data = login_response.json()

# Check login success and extract token (if successful)
if login_data.get('message') == 'Sign-in successful':
    token = login_data.get('token')  # Extract token from successful login response
else:
    print("Login failed:", login_data.get('error'))
    token = None  # Set token to None if login fails

# Products (access only if login successful)
if token:  # Only proceed if login token exists
    products_url = 'https://app.signalgas.io/api/v1/products'
    headers = {
        'Authorization': f'Bearer {token}'  # Include retrieved token in Authorization header
    }
    products_response = requests.get(products_url, headers=headers)
    products_data = products_response.json()
    print(products_data)

# Currencies (access only if login successful)
if token:  # Only proceed if login token exists
    currencies_url = 'https://app.signalgas.io/api/v1/countries/'
    currencies_response = requests.get(currencies_url, headers=headers)
    currencies_data = currencies_response.json()
    print(currencies_data)

# Remove signup call (commented out)
# Signup attempt is unnecessary after successful login

# print(signup_data)