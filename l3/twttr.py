strng = input("Input:")
chars1 = ["A", "E", "I", "O", "U"]
p_string=""
for c in strng:
    if c not in (chars1 + list(map(str.lower, chars1))):
        p_string += c

print("Output:", p_string)

