
number_str = input("What is the Answer to the Great Question of Life, the Universe and Everything: ")

number_str = number_str.lower().strip()
match number_str:
    case '42' | 'forty-two' | 'forty two':
        print("Yes")
    case _:
        print("No")
