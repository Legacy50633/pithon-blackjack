import random
print("Black jack")
comp_array = []
user_array = []
user_value = 0
computer_value = 0
start_user = 0
start_computer = 0
us1 = random.randint(1,11)
us2 = random.randint(1,11)
user_array.append(us1)
user_array.append(us2)
comp1 = random.randint(1,11)
comp2 = random.randint(1,11)
comp_array.append(comp1)
comp_array.append(comp2)
l = comp_array
k= user_array
print(f"Your cards:{user_array} ,\n Computer cards :{comp_array} ")
for p in user_array:
     start_user += p
for q in comp_array:
     start_computer += q 
if start_user < 21 and start_user < start_computer :
     print(" Result for now = Computer will win")
else:
     print(" Result for now  = You will win") 
card_need = input("Enter y for another card , n for the result: ")        
if card_need == "y":
     us3 = random.randint(1,11)
     extra_user_card_value = start_user + us3
     print(f"Your  Third card {us3} and Sum is {extra_user_card_value}")
     comp3 = random.randint(1,11)
     extra_user_computer_value = start_computer + comp3
     print(f"computer's  Third card {comp3} and Sum is {extra_user_computer_value}")
     result = ""
     if extra_user_card_value >21 :
          result += "You Lost"
          print(result)
     elif extra_user_card_value <21 and extra_user_card_value >  extra_user_computer_value:
          result += "You win"
          print(result)  
     else:
          result += "Computer Wins"          
          print(result) 

''' us3 = random.randint(1,11)
    user_array.append(us3)
    user_value += us3
    comp3= random.randint(1,11)
    comp_array.append(comp3)
    computer_value += comp3
    print(f"Your cards:{user_array} ,\n Computer cards :{comp_array} ")  
    if user_value > 21:
         print("You Lost !")
    elif user_value < 21 and user_value > computer_value:
         print("You win !") 
    else:
         print("Computer Win's")       
elif card_need == "n":
     print("The result is shown in the above line itself !") 
else:
     print("Are you blind !")     '''


