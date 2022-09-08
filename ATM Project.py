import time

print("\033[91m {}\033[00m" .format("PLEASE INSERT YOUR ATM CARD "))


time.sleep(7)

password=1017

pin = int(input("\033[91m {}\033[00m" .format("Enter Your ATM Pin : ")))

balance = 5000

if pin == password:
    while True:

        print("\033[91m {}\033[00m" .format(""""
        1 == Account Balance Check
        2 == Cash Withdraw
        3 == Cash Deposit
        4 == Pin Change
        5 == Exit
        """))
        try:
            option = int(input("Please Enter Your Choice "))

        except:
            print("\033[91m\033{}033m[".format("Please Enter Valid Option "))

        if option ==1:
            print(f"Your Current Balance is :Rs.{balance}")


        if option ==2:
            withdraw_amount=int(input("Please Enter withdraw Amount "))

            balance = balance - withdraw_amount

            print(f"Your Updated Balance is :Rs.{balance}")

        if option == 3:
            deposit_amount = int(input("Please Enter deposit_amount "))

            balance = balance + deposit_amount

            print(f"Your Updated Balance is :RS.{balance} ")

        if option == 4:
            def change_pin(old_pin,New_pin):
                global current_pin

                if not old_pin == current_pin:
                    print("Invalid old PIN ,please try again or visit Your Nearest bank branch")
                else:
                    current_pin = New_pin
                    print("ATM card PIN Ending with xxxx is Updated Successfully..!")

        if option == 4:
                print("Thank You very much...! Visit Again")
                break
else:
    print("You Entered Wrong Pin. Please try again...!")