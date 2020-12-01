# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference

# Want to learn more: https://en.wikipedia.org/wiki/Set_theory#Basic_concepts_and_notation
# Python docs: https://docs.python.org/3.8/library/stdtypes.html#set

# Makes sense:
numb1 = 8
numb2 = -4
new_line = '\n'

# Lets make a list containing duplicate values:

duplicate_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 5, 5, 5, 5, 5, 7, 7, 7]

# Transform that list to a Set:

uniques = set(duplicate_list)

# And like always we will do a printout to check our result:

print(F'{type(duplicate_list)} {duplicate_list}', new_line)
print(F'{type(uniques)} {uniques}', new_line)

# Lets create a second Set:

set_numbers = {1, 4}  # You can see our values are surrounded by {}, this is the python syntax for a Set

# Adding a value to our Set:

set_numbers.add(numb1)
set_numbers.add(numb2)

# Print the result:
print(set_numbers, new_line)

# Removing a value from our Set:

set_numbers.remove(numb1)
set_numbers.remove(numb2)

# Print the result:
print(set_numbers, new_line)

# The whole power of a set lies within the mathematical operations that it brings you, let me show you:

first = set(range(25))
second = set(range(14, 50))

union = first | second
print(f'items of the two sets combined: {union}', new_line)

intersection = first & second
print(f'only items present in both sets: {intersection}', new_line)

difference = first - second
print(f'unique items that are stored only in set 1: {difference}', new_line)

semantic_diff = first ^ second
print(f'unique items that are stored in first or second set: {semantic_diff}', new_line)

# Because of the fact that sets are unordered the following is not possible:

# print(first[0])  # TypeError: 'set' object does not support indexing

# What we can do is check if a certain value is contained in our set, before unnecessary iterating over our set:

needed_item = 1

if needed_item in first:
    print('Our set contains the needed item, more actions follow...')
