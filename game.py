from random import randint
number=randint(1,10)
UserName=input("What is your name player 1")
print("Hello there",UserName,". are you ready to guess?")
print(number)
usernumber=eval(input("Guess a number:"))
count=0
while count<10:
    if usernumber>number:
        print("Your number is greater than the correct number")
        usernumber=eval(input("Guess again:"))
    elif usernumber<number:
        print("Your number is lesser than the correct number")
        usernumber=eval(input("Guess again:"))
    elif usernumber==number:
        print("You guessed right,you win!")
        break
    count=count+1
    print("you have",10-count,"tries remaining")

