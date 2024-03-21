if __name__ == "__main__":
    notDone = True
    while notDone:

        encryptedPassword = ""
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            tempPassword = input("Please enter your password to encode: ")
            for i in range(0, len(tempPassword)):
                tempNum = int(tempPassword[i])
                tempNum += 3
                encryptedPassword += str(tempNum)
                new_encryptedPassword = encryptedPassword

            print("Your password has been encoded and stored!")


        if choice == 2:
            new_password = ""
            for char in new_encryptedPassword:
                num = int(char)
                new_num = num - 3
                if new_num < 0:
                    new_num = new_num + 10
                new_password += str(new_num)
            print(f"The encoded password is {new_encryptedPassword}, and the original password is {new_password}.")


        if choice == 3:
            break