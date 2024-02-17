given_str = "teeter"

for char in given_str:
        print(char)
        if given_str.count(char) == 1:
                print("Char is: ", char)
                break
