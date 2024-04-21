import os
import re

# Task 1
def create_file(file_path):
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            pass  # Create an empty file

# Task 2:
def read_user_names_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Task 3:
def read_user_names(file_path):
    with open(file_path, 'r') as file:
        user_names = [line.strip() for line in file]

    # Exclude 10% of users
    excluded_users = int(0.1 * len(user_names))
    user_names = user_names[excluded_users:]

    return user_names

# Task 4:
def get_users_in_even_rows(file_path):
    with open(file_path, 'r') as file:
        user_names = [line.strip() for idx, line in enumerate(file) if idx % 2 == 0]

    return user_names

# Task 5:
def read_and_validate_user_info(file_path):
    email_addresses = []
    addresses = []

    with open(file_path, 'r') as file:
        for line in file:

            user_info = line.strip().split(',')
            if len(user_info) == 3:
                name, email, address = user_info
                # Check if email is valid
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    email_addresses.append(email)

                if address:
                    addresses.append(address)

    return email_addresses, addresses

# Task 6
def filter_gmail_addresses(email_addresses):
    return [email for email in email_addresses if email.endswith('@gmail.com')]

# Task 7: Iterate through two lists and return whether each email consists of the username
def check_email_username_relation(user_names, email_addresses):
    email_username_relation = {}
    for user_name, email in zip(user_names, email_addresses):
        email_username_relation[email] = user_name.lower() in email.lower()

    return email_username_relation

# Task 8:
def check_user_in_list(user_name, user_names):
    formatted_names = [user_name.lower(), user_name.upper(), user_name.title()]

    for formatted_name in formatted_names:
        if formatted_name in user_names:
            return True

    return False

# Task
def capitalize_all_names(user_names):
    return [name.upper() for name in user_names]

# Task 10:
def calculate_total_earnings(purchase_list):
    total_earnings = 0

    for idx, customer in enumerate(purchase_list, start=1):
        if idx % 8 == 0:
            total_earnings += 200
        else:
            total_earnings += 50

    return total_earnings

# Example usage:
file_path = "user_names.txt"
create_file(file_path)

# Sample data for illustration purposes
sample_users = ["John", "Alice", "Bob", "Eve"]
with open(file_path, 'w') as file:
    file.write("\n".join(sample_users))

user_names_generator = read_user_names_generator(file_path)
user_names_array = read_user_names(file_path)
users_in_even_rows = get_users_in_even_rows(file_path)
email_addresses, addresses = read_and_validate_user_info(file_path)
gmail_addresses = filter_gmail_addresses(email_addresses)
email_username_relation = check_email_username_relation(user_names_array, email_addresses)
user_existence_check = check_user_in_list("Sara Lev", user_names_array)
capitalized_names = capitalize_all_names(user_names_array)
purchase_list = [15, 20, 76, 88, 4, 43, 19, 5, 9]
total_earnings = calculate_total_earnings(purchase_list)

# Print results for illustration
print("User Names Generator:", list(user_names_generator))
print("User Names Array:", user_names_array)
print("Users in Even Rows:", users_in_even_rows)
print("Email Addresses:", email_addresses)
print("Gmail Addresses:", gmail_addresses)
print("Email-Username Relation:", email_username_relation)

