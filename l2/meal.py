def main():

    exp = input("What time is it? ")
    time = convert(exp)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    new_time = time.split(":")
    new_t_time = float(new_time[0])+(float(new_time[1])/60)
    return new_t_time

if __name__ == "__main__":
    main()