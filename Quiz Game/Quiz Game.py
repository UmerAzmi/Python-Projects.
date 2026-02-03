score=0
print('Welcome to Quizimania.')
answer = input('Do you wanna play the quiz game? ')
if answer.lower() == 'yes':
    print("\n\tOkay let's play")
else:
    print('\n\tWhy did you run the program then?')
    quit()
    
answer = input('\nWhat is 5 + 3? \nAns: ')
if answer == '8':
    print("Correct")
    score+=1
else:
    print('Incorrect')
    
answer = input('\nWhat is the capital of India? \nAns: ')
if answer.lower() == 'delhi':
    print("Correct")
    score+=1
else:
    print('Incorrect')

answer = input('\nIf you mix red and yellow, what color do you get? \nAns: ')
if answer.lower() == 'orange':
    print("Correct")
    score+=1
else:
    print('Incorrect')

answer = input('\nWhat is 10 divided by 2? \nAns: ')
if answer == '5':
    print("Correct")
    score+=1
else:
    print('Incorrect')

print("\n\tLet's move to difficult questions.")
print('\nWhich animal says "meow"? ')
print('a) Vampire')
print('b) Cat')
print('c) Sky Blue Color')
print('d) Random Access Memory')

answer = input('Ans: ')
if answer.lower() == 'b':
    print("Correct")
    score+=1
else:
    print('Incorrect')

print('\nWhich one is a fruit? ')
print('a) Dog')
print('b) Water Colours')
print('c) Watermelon')
print('d) Harry Potter')

answer = input('Ans: ')
if answer.lower() == 'c':
    print("Correct")
    score+=1
else:
    print('Incorrect')

print('\nWhich is heavier: 1 kg of cotton or 1 kg of iron? ')
print('a) Cotton')
print('b) Iron')
print('c) Both are the same')
print('d) None of the above')

answer = input('Ans: ')
if answer.lower() == 'c':
    print("Correct")
    score+=1
else:
    print('Incorrect')

percentage = score/7 *100

print('\nWell Done! You have completed the quiz.')
print(f"You've got {score} correct answers")
print(f"You got {percentage}%.\n")
if percentage > 80:
    print('Well done! You have smashed the Quiz')
elif percentage > 35:
    print('Well done! You have passed the Quiz. Try again if you want to smash it')
else:
    print('Well done! You have failed the Quiz. You should be proud of your self. Go study!')
