name = input("camelCase: ")
new_name = ""
for c in name:
    if c.isupper():
        add_c = "_"+c.lower()
    else:
        add_c = c
    new_name += add_c
print("snake_case:", new_name)