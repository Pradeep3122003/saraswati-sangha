import re

def valid_mobile(number):
    pattern = r"^[0-9]{10}$"
    if re.fullmatch(pattern, number):
        return True
    else:
        return False

