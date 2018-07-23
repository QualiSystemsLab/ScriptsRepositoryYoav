import random
import string
import re

def check_random_password(password):
    # searching for digits
    digit_error = re.search(r"\d", password) is None
    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None
    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None
    # overall result
    password_ok = not (digit_error or uppercase_error or lowercase_error)
    return password_ok

passed = 0
failed = 0
for i in range (1, 50):
    qq = False
    while qq == False:
        random_generated_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
        qq = check_random_password(random_generated_password)
pass