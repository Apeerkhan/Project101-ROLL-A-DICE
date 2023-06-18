import random

def rolldice(min, max):
    while True:
        print("Rolling dice....")
        print(f"your number:{random.randint(min, max)}")
        choice = input("Press y to roll again and n to exit :y(y/n)")
        if choice.lower() == 'n':
         break
       
rolldice(1, 6)