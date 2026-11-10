"""
Simple Interest Calculator

Collects principal, interest rate, and time.
Validates the values and calculates simple interest.
"""

import math


def get_positive_number(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt).strip())

            if not math.isfinite(value):
                print("Please enter a finite number.")
            elif allow_zero and value >= 0:
                return value
            elif not allow_zero and value > 0:
                return value
            else:
                print("Please enter a valid positive number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


principal = get_positive_number("Enter principal amount: $")
rate = get_positive_number("Enter annual interest rate (%): ", allow_zero=True)
time = get_positive_number("Enter time in years: ")

interest = (principal * rate * time) / 100
total_amount = principal + interest

print("\n--- Simple Interest Results ---")
print(f"Principal: ${principal:.2f}")
print(f"Interest rate: {rate:.2f}%")
print(f"Time: {time:.2f} years")
print(f"Simple interest: ${interest:.2f}")
print(f"Total amount: ${total_amount:.2f}")
