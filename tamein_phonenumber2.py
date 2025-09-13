print("phone_number_list")
print("ver 1.0")
print("crator Rafael")
print("_" * 20)

number_list = []
while True:
    print("1) Add Phone Number")
    print("2) Show List ")
    print("3) Find Phone Number")
    print("4) Count")
    print("5) Delete Phone Number")
    print("0) Exit")

    print("_" * 20)
    obtion = input("choose obtion :")

    match obtion:
        case "1":
            phone_number = input("Enter Phone Number: ")
            if len(phone_number) == 11:
                if phone_number not in number_list:
                    number_list.append(phone_number)
                    print("Phone Number Add In The List")
                else:
                    print("Phone Number Already Exist In The List!!")
            else:
                print("Phone Number Must Have Exactly 11 Digits!")

        case "2":
            number_list.sort()
            print("Phone Number In The List :")
            for number in number_list:
                print(number)
        case "3":
            num = input("Enter Phone Number For Found :")
            if num in number_list:
                print("Phone Number Found In The List :", num)
            else:
                print("Phone Number Not In The List!!")
        case "4":
            print("Phone Number In The List :", len(number_list))

        case "5":
            number_del = input("Enter Phonen Number For Deleted as List :")
            if number_del in number_list:
                number_list.remove(number_del)
                print("Phone Number Deleted as in The List :", number_del)
            else:
                print("Phone Number Not in the List!!")
        case "0":
            print("Do You Whant to Exit app if :")
            khoroj = input("y or n ? :")
            if khoroj == "y":
                print("Exit")
                break
            elif khoroj == "n":
                print("you in the app.")
        case _ :
             print("error : add vared shode eshtebah ast")
    print("_" * 20)