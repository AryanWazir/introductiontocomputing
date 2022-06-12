#Q.1
   # Getting the input from the user
m=int(input("Enter Marks :"))      
   # Assigning Grade according to the range in which the marks lies
if(m<25):                          
    print(" Grade F ")
elif(m>=25 and m<45):
    print(" Grade E ")
elif(m>=45 and m<50):
    print(" Grade D ")
elif(m>=50 and m<60):
    print(" Grade C ")
elif(m>=60 and m<80):
    print(" Grade B ")
elif(m>=80):   
    print(" Grade A ")
else:
    print(" No result ")

#Q.2
   # Taking an input year from the user
year = int(input("Enter a year: "))      
   #Checking if the given year is leap year
if year % 4 == 0 :                        
    print("Given year is a Leap Year")
elif year % 100 == 0 :
    print("Given year is not a Leap Year")
elif year % 400 == 0 :
    print("Given year is a Leap Year")
   # Else it is not a leap year
else :
    print("Given year is not a Leap Year")

#Q.3
import random
for i in range(10):
   # Generating random number num1
    num1 = random.randint(1,10)
   # Generating random numbe rnum2
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
   # Getting the user's answer
    user_answer = int(input(f"{num1}X{num2}="))
   # Checking if the user's answer matches the actual answer
    if user_answer == (num1*num2):
   # Printing correct if answer matches
        print("Correct!")
   # Else printing wrong and displaying the correct answer
    else:
        print(f"Wrong.The correct answer is {num1*num2}")
    

#Q.4
x=200

for candies in range(x):
   #Conditions for determining the number of candies
    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies, 'candies are in the bowl!')
             break

