#program principal calculator
rate=input("enter rate")
time=input("enter time")
interest=input("enter interest")
principal=float(interest)*100/float(rate)*float(time)
print("principal is {}".format(principal))
