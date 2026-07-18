# validating_credit_card_number.py

import re

for _ in range(int(input().strip())):
    card = input().strip()

    pattern = r"^[456]\d{3}(-?\d{4}){3}$"

    if re.match(pattern, card):
        digits = card.replace("-", "")

        if re.search(r"(\d)\1{3,}", digits):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
