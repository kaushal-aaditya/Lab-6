def encode(password):  # encode function
    j = [*password]  # splits string into list
    newpassword = ""  # new password will be stored here
    for i in range(len(j)):
        newpassword += str(int(j[i])+3)  # each entry in list will be increased by 3 and then converted to string and appended to newpassword
    return newpassword

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
            print("The encoded password is " + enco_pass + ", and the original password is unknown.")
        elif menu_sel == 3:
            break


if __name__ == "__main__":
    main()