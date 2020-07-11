# importing libraries
import random
import time
import pyttsx3


# function for text to speech
def vc_cmnd(txt):
    pyttsx3.init()
    engine = pyttsx3.Engine(driverName='sapi5')
    engine.setProperty('rate', 128)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(txt)
    engine.runAndWait()


# code to time the game
t = time.localtime()
y = t.tm_year
m = t.tm_mon
d = t.tm_mday

h = t.tm_hour
min = t.tm_min

str_time = "%s - %s - %s ; %s : %s - " % (d, m, y, h, min)


# function for logging the data in file
def log_file(txt):
    with open("LOG.txt", "a") as f:
        f.write(txt + "\n")


# Function For deciding the winner
def rps(x, y):
    if x == "Rock" and y == "Paper":
        return y
    if x == "Scissor" and y == "Rock":
        return y
    if x == "Paper" and y == "Scissor":
        return y
    else:
        return x


# function for the mode: AI vs AI
def c_vs_c(a):
    w = ""
    ai_1 = random.choice(a)
    ai_2 = random.choice(a)
    print("AI_1: ", ai_1)
    vc_cmnd("AI 1 has chosen:{}".format(ai_1))
    print("AI_2: ", ai_2)
    vc_cmnd("AI 2 has chosen:{}".format(ai_2))
    if ai_1 == ai_2:
        w = "Match Tied"
    else:
        d = rps(ai_1, ai_2)
        if d == ai_1:
            w = "AI 1 Wins"
        else:
            w = "AI 2 Wins"
    vc_cmnd(w)
    log_file(str_time + w)
    return w


# Function for the mode: player vs computer
def p_vs_c(a):
    p = ""
    print("1.ROCK")
    print("2.PAPER")
    print("3.SCISSOR")
    print("Enter Your Choice")
    vc_cmnd("Enter Your Choice")
    c = input()
    if c == '1':
        p = "Rock"
    elif c == '2':
        p = "Paper"
    elif c == '3':
        p = "Scissor"
    else:
        vc_cmnd("Enter valid choice")
        return ("Enter valid choice")


    ai = random.choice(a)
    print("player: ", p)
    vc_cmnd("You have chosen:{}".format(p))
    print("AI: ", ai)
    vc_cmnd("AI has chosen:{}".format(ai))
    if p == ai:
        w = "Match Tied"
    else:
        d = rps(p, ai)
        if d == p:
            w = "CONGRATULATIONS....YOU WIN"
        else:
            w = "You LOSE......Better Luck Next Time"
    vc_cmnd(w)
    log_file(str_time + w)
    return w


# function to start the game
def ply_gm():
    vc_cmnd("Welcome to Rock   Paper  Scissor")
    ch = 'y'
    while ch == 'Y' or ch == 'y':
        print("....WELCOME TO....")
        print("ROCK..PAPER..SCISSOR")
        print("SELECT THE MODE")
        print("1.AI1 vs AI2")
        print("2.player vs AI")
        print("3.show Log")
        ch = input()

        a = ["Rock", "Paper", "Scissor"]
        if ch == '1':
            print(c_vs_c(a))
        elif ch == '2':
            print(p_vs_c(a))
        elif ch == '3':
            with open("LOG.txt") as f:
                content = f.read()
                print(content)
        else:
            print("Enter Valid Mode")
        print("Do you want to play again (Y/N)")
        ch = input()
        if ch not in['y','Y']:
            print('GAME OVER')
            vc_cmnd("GAME OVER")
            return


# calling the function to start the game
ply_gm()