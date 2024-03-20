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

            print("Your password has been encoded and stored!")

        if choice == 2:
            continue

        if choice == 3:
            break