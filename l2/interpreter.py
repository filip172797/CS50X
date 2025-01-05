exp = input("Filename: ")
exp = exp.lower()

exps = exp.split(" ")


match exps[1]:
    case "+":
        res = float(exps[0]) + float(exps[2]) 
    case "-": 
        res = float(exps[0]) - float(exps[2]) 
    case "/": 
        res = float(exps[0]) / float(exps[2]) 
    case "*": 
        res = float(exps[0]) * float(exps[2]) 
    case _:
        print("wowowowowo")

print(res)     