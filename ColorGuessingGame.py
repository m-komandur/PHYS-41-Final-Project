import matplotlib.pyplot as plt
import numpy as np

rawSet = np.random.randint(4, size = 4)

colorSet = []
def assignColors(numArray):
    for i in range(len(numArray)):
        if numArray[i] == 0:
            colorSet.append('blue')
        elif numArray[i] == 1:
            colorSet.append('red')
        elif numArray[i] == 2:
            colorSet.append('yellow')
        elif numArray[i] == 3:
            colorSet.append('green')
        
        
    return colorSet
assignColors(rawSet)

inputs =[]

print("Hello there, gamer! Ready to crack a puzzle? \nYour goal in this game is to find the correct sequence of colors generated by the code\nusing your superior deduction skills and just a little bit of guess work.")
print("After your guess for each attempt, you'll be able to see which colors from your input\nmatched correctly, like this:")
plt.figure().set_figheight(2)
plt.ylim(0.5,2.5)
plt.xlim(0.5,4.5)
plt.title('For example:\nIf the color in the hidden sequence matches your guess, you cracked that color!', size = 20, style = 'oblique')

plt.yticks([1,2],['Your guess','Hidden sequence'],fontsize=20)
plt.xticks([1,2,3,4],['Color 1','Color 2','Color 3','Color 4'],fontsize=20)
plt.scatter(1,1, s=2000, c = 'red')
plt.scatter(2,1, s=2000, c = 'blue')
plt.scatter(3,1, s=2000, c = 'yellow')
plt.scatter(4,1, s=2000, c = 'green')
plt.scatter(1,2, s=2000, c = 'red')
plt.scatter(2,2, s=2000, c = 'black')
plt.scatter(3,2, s=2000, c = 'black')
plt.scatter(4,2, s=2000, c = 'green')
plt.show()
print("Don't worry, for every color you don't pick correctly, you'll get a hint. Each sequence has four items and is made of the following colors: red, yellow, green, and blue.")
print("Remember: a color can appear more than once in the same sequence and sometimes isn't involved in the correct sequence at all.")
print("Good luck!")
def plotColors(attemptNum):
    
    guess = None
    
    item = 0
    print('------Attempt ', i+1, '------')
    
    while guess != 'red' and guess != 'blue' and guess != 'yellow' and guess != 'green' and item<len(rawSet):
        print('Color ', item+1)
        guess = input('Enter color: ')
        if guess.islower() == False:
            guess = guess.lower()
        if guess != 'red' and guess != 'blue' and guess != 'yellow' and guess != 'green':
            print('Oops! Looks like you either misspelled your color or entered a color outside of the choices given above. Try again!\n')
        else:
            inputs.append(guess)
            guess = None
            item+=1
        
    k = 0
    x = 1
    plt.figure().set_figheight(2)
    plt.ylim(0.5,2.5)
    plt.xlim(0.5,4.5)
    plt.title('If the color in the hidden sequence matches your guess, you cracked that color!',size = 15)
    plt.yticks([1,2],['Your guess','Hidden sequence'],fontsize=20)
    plt.xticks([1,2,3,4],['Color 1','Color 2','Color 3','Color 4'],fontsize=20)
    for k in range(len(rawSet)):
        if colorSet[k] == inputs[k]:
            plt.scatter(x,2,s=2000, c=inputs[k])            
            k+=1
            x+=1
        elif colorSet[k] != inputs[k]:
            plt.scatter(x,2,s=2000, c='black')    
            print('')
            print('Hint:')
            if inputs[k] in colorSet:
                print('Color ', k+1,' exists in list, but in wrong place')
            else:
                print('Color ', k+1, ' does not exist in list')
            k+=1
            x+=1
    plt.scatter(1,1, s=2000, c = inputs[0])
    plt.scatter(2,1, s=2000, c = inputs[1])
    plt.scatter(3,1, s=2000, c = inputs[2])
    plt.scatter(4,1, s=2000, c = inputs[3])
    plt.show()    
    
playerAttemptChoice = 0
while playerAttemptChoice>15 or playerAttemptChoice<3:
    playerAttemptChoice = int(input('How many attempts would you like to have? \nThe least number of attempts you are allowed is 3 and the most is 15.\nPlease do not spell out the number! Keep it as an integer.\n'))
    if playerAttemptChoice>15 or playerAttemptChoice<3:
        print('Oops! Looks like you entered an invalid number of attempts. Please keep your choice between 3 and 15!') ## what if user enters a string?
    else:
        print('You have chosen', playerAttemptChoice, 'attempt(s)!')

for i in range(playerAttemptChoice+1):
    if i == playerAttemptChoice:
        print('Oh no! You have used all of your attempts!')
        lastQuest = input('Would you like to view the answer? Enter "y" or "n"\n')
        if lastQuest == 'y':
            plt.figure().set_figheight(2)
            plt.yticks([1],['Correct answer'],fontsize=20)
            plt.ylim(0.5,1.5)
            plt.xlim(0.5,4.5)
            plt.xticks([1,2,3,4],['Color 1','Color 2','Color 3','Color 4'],fontsize=20)
            plt.scatter(1,1, s=2000, c = colorSet[0])
            plt.scatter(2,1, s=2000, c = colorSet[1])
            plt.scatter(3,1, s=2000, c = colorSet[2])
            plt.scatter(4,1, s=2000, c = colorSet[3])
            plt.show()  
            break
        elif lastQuest == 'n':
            print('Better luck next time!')
            break
        elif lastQuest != 'y' and lastQuest != 'n':
            print('Invalid response')
            break
    plotColors(i)
    if inputs != colorSet:
        inputs.clear()
        if i+3 == playerAttemptChoice:
            print('Reminder: you have 2 attempts left!')
        if i+2 == playerAttemptChoice:
            print('Reminder: you have 1 attempt left!')
        
    elif inputs == colorSet:
        print('Congratulations! You found the color sequence in ', i+1, 'attempt(s)!')
        break