def encode(password):  # encode function
    j = [*password]  # splits string into list
    newpassword = ""  # new password will be stored here
    for i in range(len(j)):
        newpassword += str(int(j[i])+3)  # each entry in list will be increased by 3 and then converted to string and appended to newpassword
    return newpassword


def decode(user_password):  # decodes function
    user_password = [*user_password]
    decoded_password = ""  # stores the decoded password
    for a in range(len(user_password)):
        decoded_password += str(int(user_password[a]) - 3)
    return decoded_password


x = 0  # variable for while loop

def main():
    while x < 10:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        print("Please enter an option: ")
        menu_sel = int(input())

        if menu_sel == 1:
            print("Please enter your password to encode: ")
            base_pass = input()  # user input, base password
            enco_pass = encode(base_pass)  # encoded pasword
            print("Your password has been encoded and stored!")
        elif menu_sel == 2:
            decode_pass = decode(enco_pass)
            print("The encoded password is " + enco_pass + ", and the original password is " + decode_pass + ".")
        elif menu_sel == 3:
            break


if __name__ == "__main__":
    main()