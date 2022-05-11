"""
Exercise
Add logging to the program below. The program
uses the new `secrets` module to create a token:
https://docs.python.org/3/library/secrets.html

Implement info messages for every function and
a debug message with the value of the token.
For more information about logging:
https://docs.python.org/3/library/logging.html
"""

import secrets
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(process)s %(module)s %(levelname)-8s %(message)s",
    filename="token.log"
)

def main():
    """Run program to email a secret token"""
    logging.info("Run generate token.")
    token = generate_token()
    logging.debug(f"Received token: {token}")    
    logging.info("Send token via mail.")
    email_token(token)

def generate_token():
    """Return a token for password reset"""
    logging.info("Create token using hex")
    token = secrets.token_hex()
    logging.debug(f"Token created is {token}")
    return token

def email_token(token):
    """Email the token"""
    logging.info("Email the token")
    body = f"The token to reset your password: {token}"
    pass

if __name__ == "__main__":
    main()
