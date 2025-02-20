
while True:
    inpt = input("Fraction:")
    try:

        Nominator, Denominator = inpt.split("/")

        x = int(Nominator)
        y = int(Denominator)

        p = x/y

        if p < 1:
            break

    except (ZeroDivisionError, ValueError):
        pass

f = int (p * 100)

if f > 99:
    print("F")
elif f < 1:
    print("E")
else:
    print(f"{f}%")



