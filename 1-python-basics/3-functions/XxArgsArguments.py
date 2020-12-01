# Lets simulate some db action with python 3.7 :D:

# We can write a function for that:

# Instead of giving it an arbitrary amount of arguments,
# we use an arbitrary amount of keyword arguments.

# let me google that for you: https://duckduckgo.com/?q=python+keyword+arguments&atb=v120-7&ia=web


def save_user(**user):
    print(f'user saved: {user}')


save_user(id=1, name='Admin')  # printout holds a key/value pair


# The printout from above is actually a Python dictionary
# JS devs should recognize this format it looks like an object in JavaScript

# Okay lets wrap it up and finish our functions:

def save_by_id(**user):
    print(f"id saved: {user['id']}")


save_by_id(id=1, name='Admin')


def save_by_name(**user):
    print(f"name saved: {user['name']}")


save_by_name(id=1, name='Admin')
