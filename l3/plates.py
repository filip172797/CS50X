def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    res = True
    res &= start_with_two_letters(s) if correct_length(s) else False
    res &= numbers_in_end(s)
    res &= no_weird_signs(s)
    return res


def start_with_two_letters(s: str):
    return s[0].isalpha() and s[1].isalpha()


def correct_length(s: str):
    return 1 < len(s) < 7


def numbers_in_end(s: str):
    allowed_to_be_num = True
    last_num_is_zero = False
    for c in s[::-1]:
        if c.isnumeric():
            last_num_is_zero = c == "0"

        if c.isnumeric() and not allowed_to_be_num:
            return False
        elif c.isalpha():
            allowed_to_be_num = False        
    
    return True and not last_num_is_zero


def no_weird_signs(s: str):
    for c in s:
        if c in [".", " ", "-"]:
            return False
    return True


main()
