users = set()

# Create a set with the two users sporia123 and clarko919
users = {"sporia123","clarko919"}
print("Current users: {}\n".format(users))

# Add harrise1 to the set
users.add("harrise1")
print("Added user to the set: {}\n".format(users))

# Add clarko919 to the set again
users.add("clarko919")
print("After adding user again: {}\n".format(users))


# Check for login status and remove clarko919 from the set (log them out)
find_user = input("Enter a name: ")
if find_user in users:
    print("Logged in.\n")
else:
    print("Not logged in.\n")
selection = input("Enter user to log out\n->")
users.remove("clarko919")
print("User logged out.\nCurrent users logged in: {}\n".format(users))

