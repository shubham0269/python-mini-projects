# ==================================  number guessing game ==========================================




import random
attempts = 0

com = random.randint(1,100)
while True:
    user = int(input("enter your number :⇥ "))
    attempts+=1
  
    if user >com:
        print("the number is greater ")
        
    elif user < com:
        print("this number is low  ")
        
    else:
        print(f"you guess the number in {attempts} attempts congratulation !")
        break
