
# Get username and email from the user
user_name = input("Enter your username: ")
email = input("Enter your email: ")

# Clean and format the input
user_name = user_name.strip().title()
email = email.strip().lower()

# Extract username and email information
length = len(user_name)
index = user_name[0]
domain = email.split("@")[-1]

# Display the formatted user information
print("--- Formatted User Info ---")
print(f"Username: {user_name}")
print(f"Email: {email}")
print(f"Username Length: {length}")
print(f"First Character: {index}")
print(f"Email Domain: {domain}")
