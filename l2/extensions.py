file = input("Filename: ")
file = file.lower().strip()

if "." in file:
    # file = file[-1].replace("\n", "")
    # print(file)
    filename = file.split(".")
    match filename[-1]:
        case ("gif" |
              "jpeg" | 
              "png"):
            print("image/"+filename[-1].replace("\n", ""), end="")
        case "jpg":
            print("image/jpeg")
        case ("pdf" |
              "zip"):
            print("application/"+filename[-1].replace("\n", ""), end="")
        case ("txt"):
            print("text/plain")     
        case _: 
            print("application/octet-stream")
else:
    print("application/octet-stream")
