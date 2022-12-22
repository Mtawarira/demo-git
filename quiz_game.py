print("Welcome to Know Your Continent Better")

first_name = input("First Name: ")
last_name = input("Last Name: ")
print("Greetings",first_name,last_name)

country = input("Country: ")
citizenship = input("Citizenship: ")
user_age = input("Age: ")
user_gender = input("Gender:(M/F): ")

print("Thank you",first_name,last_name,"for you time. We are glad to know you are from",citizenship,". We wish your country more success and more peace. GoodLuck")

playing = input("Are you ready to play? ")
if playing.upper() != "YES":
    quit()

print("Okay",first_name,"! Let's Play. Good Luck")
score = 0

print("Question 1")
answer = input("Geographically, Africa is the 2nd larget continent in the world after Asia. How many countries are in Africa? ")
if answer == "54":
    print('Good')
    score += 1
else:
    print('Sorry.',answer,"Is not the correct answer. 54 is correct.")

print("Question 2")
answer = input("African countries were once colonized by European states. Which one African country that settlers tried unsuccessfully, to colonize? ")
if answer == "Ethiopia":
    print('Good')
    score += 1
else:
    print('Sorry.',answer,"Is not the correct answer. Ethiopia is correct.")

print("Question 3")
answer = input("One of the African countries is Tanzania, which hosts the highest mountain in Africa. What is the name of this mountain? ")
if answer == "Mount Kilimanjaro":
    print('Good')
    score += 1
else:
    print('Sorry.',answer,"Is not the correct answer. Mount Kilimanjaro is correct.")
print("Question 4")
answer = input("The world has 7 natural wonders. The fourth of those wonders is in Zimbabwe. What is the name of this 4th natural wondor? ")
if answer == "Victoria Falls":
    print('Good')
    score += 1
else:
    print('Sorry.',answer,"Is not the correct answer. Victoria Falls is correct.")

print("Question 5")
answer = input("South Africa was the last to gain independence in Africa from its colonial masters. Which country was the first? ")
if answer == "Ghana":
    print('Good')
    score += 1
else:
    print('Sorry.',answer,"Is not the correct answer. Ghana is correct.")



print("You Scored " +str(score)+ "points.")
print(str((score/5)*100)+"%")



