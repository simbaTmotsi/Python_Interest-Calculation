#Interest=(Principal*Rate*Time)/100)
#Author: Simbarashe Timothy Motsi R157674D
#Computer SCience(CTH)
loop=0# this is the value for that can be changed to stop our program from continuously repeating
while loop==0:#this is to check the value of loop is still relevent for a loop cycle to occur
    while True:
        try:
            Time = float(input("Enter Time: "))#this assigns a value to Time
            while Time <=0:#this is to make sure that all values entered are positive
                print("please try again, only positive numbers can be entered")#the error message for 0 or negative numbers
                Rate = (input("enter Time: "))#this lets the user re-enter the accurate value
            break
        except ValueError:#this lets the program know what to do with with the errors by entering non-numeric data
            print("Non-numeric characters are invalid, please enter a positive number for Time")
            
    while True:
            try:
                Rate = float(input("Enter Rate: "))#this assigns a value to Rate
                while Rate <=0:#this is to make sure that all values entered are positive
                    print("please try again, only positive numbers can be entered")#the error message for 0 or negative numbers
                    Rate = float(input("enter Rate: "))#this lets the user re-enter the accurate value
                break
            except ValueError:#this lets the program know what to do with with the errors by entering non-numeric data
                print("Non-numeric characters are invalid, please enter a positive number for Rate")

     while True:
            try:
                Principal = float(input("Enter Principal "))#this assigns a value to Principal
                while Principal <=0:#this is to make sure that all values entered are positive
                    print("please try again, only positive numbers can be entered")#the error message for 0 or negative numbers
                    Principal = float(input("enter Principal: "))#this lets the user re-enter the accurate value
                break
            except ValueError:#this lets the program know what to do with with the errors by entering non-numeric data
                print("Non-numeric characters are invalid, please enter a positive number for Principal")

    
    Interest=(100*Time)/(Principal*Rate)#This formula calcutaes the Interest
    Print("your Interest is")
    print(Interest)
