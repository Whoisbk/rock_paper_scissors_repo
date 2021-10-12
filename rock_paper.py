
import random
import pyttsx3

options = ['rock','paper','scissors']

aiScore = 0
pScore = 0

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



while True:

    p1 = input('type in rock / paper / scissor or Q to quit: ' )

    if p1 == 'Q':
        print("Game Over")
        speak("Game Over")
        break
    random_num = random.randint(0,2)

    aiChoice = options[random_num]

    if p1 == 'rock' and aiChoice == 'scissors':
        speak('P1 wins')
        print('P1 wins')
        speak(f'ai chose: {aiChoice}')
        print(f'ai chose: {aiChoice}')
        pScore+=1
       
    
    elif p1 == 'paper' and aiChoice == 'rock':
        speak('P1 wins')
        print('P1 wins')
        speak(f'ai chose: {aiChoice}')
        print(f'ai chose: {aiChoice}')
        pScore+=1
       

    elif p1 == 'scissors' and aiChoice == 'paper':
        speak('P1 wins')
        print('P1 wins')
        speak(f'ai chose: {aiChoice}')
        print(f'ai chose: {aiChoice}')
        pScore+=1
        
     
    elif p1 == 'paper' and aiChoice == 'paper':
        speak('Draw')
        print('Draw')
       

    elif p1 == 'scissors' and aiChoice == 'scissors':
        speak('Draw')
        print('Draw')

       
    elif p1 == 'rock' and aiChoice == 'rock':
        speak('Draw')
        print('Draw')
 

    else:

        speak("you lose!!")
        print("You lose!!")
        speak(f'ai chose: {aiChoice}')
        print(f'ai chose: {aiChoice}')
        
        aiScore += 1

speak(f'Player 1 score: {pScore}')
print(f'Player 1 score: {pScore}')
speak(f'ai score: {aiScore}')
print(f'ai score: {aiScore}')


if pScore > aiScore:
    speak("Player 1 wins the game")
    print("Player 1 wins the game")
elif pScore == aiScore:
    speak("The game ended with a draw")
    print("The game ended with a draw")
else:
    speak("AI wins the game")
    print("AI wins the game")






    




    





    