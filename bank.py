
#simple interest
money=int(input("enter the amount of loan:"))
rate =int(input("enter the amount of rate:"))
time=int(input("enter the amount of duration:"))
simple = money*rate*time/100
amount = money+simple
print("amount of interest",simple)
print("total amount",amount)
