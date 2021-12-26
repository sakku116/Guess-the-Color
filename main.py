from tkinter import *
import random
import time

root = Tk()
root.resizable(False, False)
root.title('Color Game')

######################### CONFIGURATOR VARIABLE #########################
headerFont = ('Moon', 22, 'bold')
standartFont = ('Sagoe UI', 13)
colorFont = ('Arial Rounded MT Bold', 20, 'bold')
colors = ['red',
    'blue',
    'yellow',
    'gray',
    'cyan',
    'green',
    'orange',
    'purple',
    'silver']
score = 0
scoreMinPlus = 5
scoreLimit = 100
counter = 60
timeLimit = 0
randomColor = colors[random.randint(0, len(colors)-1)]
randomText = colors[random.randint(0, len(colors)-1)]
scoreDefaultText = 'Score: ' + str(score) + '/' + str(scoreLimit)

######################### MAIN FUNCTION #########################
def start():
    resetText() #resetting score and counter
    resetColor() #resetting color and randomized color
    timer() #start the timer
    labelResult.grid_forget()
    inputButton.config(text='Stop', bg='pink', command=stop)

def stop():
    labelTimer.after_cancel(loop) #stopping the timer
    finish() #make it finish
    buttonC1.config(text='', state=DISABLED)
    buttonC2.config(text='', state=DISABLED)
    buttonC3.config(text='', state=DISABLED)

def colorGuess(txt):
    entryField.delete('0', END)
    entryField.insert('0', txt) #getting the input from randomized button color
    entryGet = entryField.get().replace(' ', '') #and applying them to get the answer
    if entryGet == '':
        pass
    else:
        if entryGet == randomColor:
            result = 'true'
        else:
            result = 'false'
        updateScore(result)

def finish():
    labelColor.config(text='')
    labelResult.config(text=('Your score: ' + str(score)))
    labelResult.grid(row=5, column=0, padx=5, ipadx=15, ipady=6, columnspan=3)
    inputButton.config(text='Start', bg='lavender', command=start)

######################### SUB FUNCTION / THE MACHINE OF THIS PORJECTS MACHINE / custom module for my main function :u #########################
def updateScore(scr):
    global score
    if scr == 'true':
        score += scoreMinPlus
        scoreResultText = 'Score: ' + str(score) + '/' + str(scoreLimit)
        labelScore.config(text=str(scoreResultText))
    else:
        if score == 0:
            scoreResultText = 'Score: ' + str(score) + '/' + str(scoreLimit) + '!!!'
            labelScore.config(text=str(scoreResultText))
        elif score >= scoreMinPlus:
            score -= scoreMinPlus
            scoreResultText = 'Score: ' + str(score) + '/' + str(scoreLimit)
            labelScore.config(text=str(scoreResultText))
    resetColor()
    if score == scoreLimit:
        stop()

def resetText():
    global score
    global counter
    counter = 60
    score = 0
    scoreDefaultText = 'Score: ' + str(score) + '/' + str(scoreLimit)
    labelScore.config(text=scoreDefaultText)
    labelTimer.config(text=('time: ' + str(counter)))

def resetColor():
    global randomColor
    global randomText
    randomColor = colors[random.randint(0, len(colors)-1)]
    randomText = colors[random.randint(0, len(colors)-1)]
    labelColor.config(text=randomText.upper(), fg=randomColor, font=colorFont, width=10)
    entryField.delete('0', END)
    randomizedButton()

def randomizedButton():
    def randomButtonColor(n1, n2):
        ran = random.randint(0, len(colors)-1)
        if ran == n1:
            ran = random.randint(0, len(colors)-1)
            return ran
        elif ran == n2:
            ran = random.randint(0, len(colors)-1)
            return ran
        else:
            return ran
    r1 = randomButtonColor(None, None)
    r2 = randomButtonColor(r1, None)
    r3 = randomButtonColor(r1, r2)
    threeButton = [colors[r1], colors[r2], colors[r3]]
    if threeButton[0] == randomColor or threeButton[1] == randomColor or threeButton[2] == randomColor:
        threeButton = threeButton
    else:
        threeButton[random.randint(0,2)] = randomColor
    buttonC1.config(text=threeButton[0], state=NORMAL, command=lambda:colorGuess(threeButton[0]))
    buttonC2.config(text=threeButton[1], state=NORMAL, command=lambda:colorGuess(threeButton[1]))
    buttonC3.config(text=threeButton[2], state=NORMAL, command=lambda:colorGuess(threeButton[2]))

def timer():
    global counter
    global loop
    counter -= 1
    labelTimer.config(text=str('time: ' + str(counter)))
    loop = labelTimer.after(1000, timer) #tkinter func, parameters: milisecond, and the main function without ()
    if counter == timeLimit or score == scoreLimit:
        stop()

######################### GUI #########################
labelHeader = Label(
    root, 
    text= 'GUESS THE COLOR', 
    fg= 'orange', 
    font= headerFont
)
labelScore = Label(
    root, 
    text= str(scoreDefaultText),
    font= standartFont
)
labelTimer = Label(
    root, 
    text= ('time: ' + str(counter)), 
    font= standartFont
)
labelCommand = Label(
    root, 
    text='Guess the color:'
)
labelColor = Label(
    root, 
    text='', 
    fg=randomColor, 
    bg='white', 
    font=colorFont, 
    width=10, 
    relief=GROOVE, 
    borderwidth=2
)
labelResult = Label(
    root, 
    text='', 
    font=standartFont, 
    bg='white'
)
entryField = Entry(
    root, 
    font=('Consolas',13)
)
inputButton = Button(
    root, 
    text='Start', 
    width=10, 
    bg='lavender', 
    command=start, 
    relief=RIDGE, 
    borderwidth=1
)
buttonC1 = Button(
    root, 
    text='', 
    font=standartFont, 
    bg='linen', 
    width=12, 
    height=1, 
    relief=RIDGE, 
    borderwidth=1, 
    state=DISABLED
)
buttonC2 = Button(
    root, 
    text='', 
    font=standartFont, 
    bg='linen', 
    width=12, 
    height=1, 
    relief=RIDGE, 
    borderwidth=1, 
    state=DISABLED
)
buttonC3 = Button(
    root, 
    text='', 
    font=standartFont, 
    bg='linen', 
    width=12, 
    height=1, 
    relief=RIDGE, 
    borderwidth=1, 
    state=DISABLED
)

# LAYOUTING
labelHeader.grid(row=0, column=0, columnspan=3, padx=5, pady=8)
labelScore.grid(row=1, column=1, padx=5)
labelTimer.grid(row=2, column=1, padx=5)
inputButton.grid(row=3, column=1, padx=5, pady=10)
labelCommand.grid(row=4, column=1, padx=5)
labelColor.grid(row=5, column=0, padx=5, ipadx=15, ipady=6, columnspan=3)
buttonC1.grid(row=6, column=0, padx=10, pady=20, ipady=5, sticky=N)
buttonC2.grid(row=6, column=1, padx=10, pady=20, ipady=5, sticky=N)
buttonC3.grid(row=6, column=2, padx=10, pady=20, ipady=5, sticky=N)

root.mainloop()
