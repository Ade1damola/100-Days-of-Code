name = input("Enter your name: ")
eng = float(input("Enter your English score over 100: "))
math = float(input("Enter your Mathematics score over 100: "))
phy = float(input("Enter your Physics score over 100: "))
chem = float(input("Enter your Chemistry score over 100: "))
bio = float(input("Enter your Biology score over 100: "))

total_score = eng + math + phy + chem + bio
average_score = total_score / 5 

print("--------------------------")
print("Report Card for", name)
print("--------------------------")
print("Total Score:", total_score)
print("Average Score", average_score, "%")
if average_score >= 40:
    print("Congratulations! You passed the semester")
else:
    print("Sorry, you failed the semester")
print("--------------------------")