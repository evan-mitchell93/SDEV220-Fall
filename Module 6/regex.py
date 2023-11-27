import re

print(re.match("me","Welcome to Menards"))
print(re.match("We","Welcome to Menards"))

#compile creates regex object
my_pattern = re.compile("me")

print(my_pattern.match("menards"))

test_str = "Welcome to menards"
match = re.search("me",test_str)
print(test_str[match.span()[0]:match.span()[1]])

print(re.findall("me",test_str))

print(re.sub("me","\U0001F602",test_str))

