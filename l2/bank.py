greetins_str = input("Greeting: ")
greetins_str = greetins_str.lower().strip()
if "hello" in greetins_str:
    amount = "0"
elif greetins_str[0] == "h":
    amount = "20"
else:
    amount = "100"

print("$" + amount)