from random import randint
number=randint(1,10)
UserName=input("What is your name player 1")
print("Hello there",UserName,". are you ready to guess?")
print(number)
usernumber=eval(input("Guess a number:"))
count=0
while usernumber!= number:
    print("Wrong")
    usernumber=eval(input("Guess again"))
    count=count+1
    if count>5:
        print("You have guessed",count,"times.You can do better than that",UserName)
    if count==7:
        print("Here's a hint: The number is a real number less than 10")

if usernumber==number:
    print("You guessed right")