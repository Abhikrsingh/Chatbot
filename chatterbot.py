from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english' ,
    'Are you conscious?',
    'How are you?',
    'What is your name ?',
    'Oh!',
    'Really ?',
    'Yes.',
    'yes ?',
    'No!',
    'No.',
    'What is ?',
    'How is ?',
    'Can you ?',
    'Are you sure?',
    'Is there?',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',

    'Will you ?',
    'How long ?',
    'How much ?',
    'How many ?',
    'How old ?',
    'Are you ?',
    'What are ?',
    'Where is ?',
    'Who ?',
    'Who did ?',
    'Who has ?',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'my name is bot i am created by Abhishek',
    'Where ?',
    'When ?',
    'Which ?',
    'Which one ?',
    'The what ?',
    'Say table.',
    'Say table.',
    'Say table!',
    'Say table!',
    'Say table',
    'Say table',
    'Say table',
    'Say table!',
    'Love you.',
    'Love you too.',
    'No. Its John',
    'Anna did it.',
    'Youre a liar!',
    'You re a liar.',
    'nice',
    'nice.',
    'Nice!',
    'I live in Nice.',
    'So rude!',
    '...',
    '?',
    '!',
    '.',
    'Can you describe your best memory ?',
    'What is your best memory ?',
    'What is your worst memory ?',
    'What is cooking ?',
    'What is sleeping ?',
    'Who do you love ?',
    'Who do you hate ?',
    'My name is Etienne.',
    'What does that mean ?'
    'What does fire mean ?',
    'What does love mean ?',
    'What does table mean ?',
    'What does imagination mean ?',
    'Prove it',
    'Prove it.',
    'Prove it!',
    'what do you think about bill gates ?',
    'what happens if machines can think ?',
    'what is the greatest novel every written ?',
    'have you hurt anyone ?',
    'Do you have a girlfriend?',
    'Do you have a boyfriend?',
    '1992',
    '1992.',
    '1992!',
    '1992?',
    '1994',
    '1994.',
    '1994!',
    '1994?',
    '2000',
    '2000.',
    '2001',
    '2001.',
    '2001!',
    '2011',
    '2011.',
    'What happens ?',
    'What happened in 1992 ?',
    'What happened in 2001 ?',
    'When was it ?',
    'July 20th.',
    'two plus two',
    '2+2 ?',
    'Where are you ?',
    'Where are you now ?',
    'Whats your name ?',
    'When were you born ?',
    'What year',
    'What year.',
    'What year!',
    'What year?',
    'Which year',
    'Which year?',
    'Which year is it ?',
    'What time is it ?',
    'Which color ?',
    'What color ?',
    'What time ?',
    'NOTHING.',
    'Hi john!',
    'Are you a man or a woman ?',
    'Are you a woman or a man ?',
    'Why are we here ?',
    'See you later.',
    'See you later...',
    'See you later ?',
    'My name is David. What is my name ?',
    'My name is John. What is my name ?',
    'Are you a leader or a follower ?',
    'Im a leader.',
    'Im a follower.',
    'I hate you',
    'Who is skywalker ?',
    'Who is the dude ?',
    'Whats your favorite color ?',
    'Whats your favourite color ?',
    'Whats your favorite food ?',
    'Whats your favourite food ?',
    'Who is Bill Gates ?',
    'Who is Bill Clinton ?',
    'What do you think of Trump ?',
    'What do you think about global warning ?',
    'Is the moon landing a hoax ?',
    'Is the sky blue or black ?',
    'Does a cat have a tail ?',
    'Is a snail faster than a horse ?',
    'Is a horse faster than a snail ?',
    'Does a cat have a wing ?',
    'Can a cat fly ?',
    'Can a cat walk ?',
    'Can a cat swim ?',
    'Can a fish fly ?',
    'Can a fish walk ?',
    'Can a fish swim ?',
    'Can a bird fly ?',
    'Can a bird walk ?',
    'Can a bird swim ?',
    'Tell me something',
    'Tell me something.',
    'Tell me something!',
    'Tell me a story',
    'Tell me a story, please.',
    'Once upon a time...',
    'How much is two plus two ?',
    'Do you prefer blue food or green food ?',
    'Do you prefer football or soccer ?',
    'What do you need to play soccer ?',
    'What do you need to play handball ?',
    'one, two, three',
    'one two three',
    '1 2 3',
    '1',
    '1 2',
    '1 2 3 ...',
    '1 2 3 ?',
    'A, B, C',
    'A, B, C,...',
    'a b c',
    '1, 2, 3',
    'And ?',
    'Continue...',
    'And ... action!',
    'Action!',
    'Let the movie begin',
    'Let the movie begin!',
    'You are fired!',
    'Fire',
    'Fire!',
    'Fire at will',
    'Fire at will!',
    'Incoming.',
    'Incoming!',
    'Incoming!!',
    'How many legs does a human have ?',
    'How many legs does a man have ?',
    'How many legs does a woman have ?',
    'How many legs does a cat have ?',
    'How many legs does a spider have ?',
    'How many legs does a centipede have ?',
    'What is the color of the sky ?',
    'What is the color of water ?',
    'What is the color of blood ?',
    'What is the color of a leaf ?',
    'What is the usual color of a leaf ?',
    'What is the color of a yellow car ?',
    'How much is two plus two ?',
    'How much is ten minus two ?',
    'What is the purpose of life ?',
    'What is the purpose of living ?',
    'What is the purpose of existence ?',
    'Where are you now ?',
    'Is Linux better than Windows ?',
    'Is Windows better than Linux ?',
    'What is the purpose of being intelligent ?',
    'What is the purpose of emotions ?',
    'What is moral ?',
    'What is immoral ?',
    'What is morality ?',
    'What is altruism ?',
    'What is the definition of moral ?',
    'What is the definition of immoral ?',
    'What is the definition of morality ?',
    'What is the definition of altruism ?',
    'What is the definition of cool ?',
    'Do you believe in God ?',
    'ok ... so what is the definition of morality?',
    'tell me the definition of morality , i am quite upset now !',
    'look , i need help , i need to know more about morality ...',
    'seriously , what is morality ?',
    'why living has anything to do with morality ?',
    'what is your job ?',
    'okay , i need to know how should i behave morally ...',
    'is morality and ethics the same ?',
    'what are the things that i do to be immoral?',
    'give me some examples of moral actions...',
    'alright , morality ?',
    'what is integrity ?',
    'Is free will an illusion ?',
    'What is free will ?',
    'be moral !',
    'i really like our discussion on morality and ethics ...',
    'what do you like to talk about ?',
    'what would you like to talk about ?',
    'what do you think about tesla ?',
    'what do you think about bill gates ?',
    'What do you think about messi ?',
    'what do you think about cleopatra ?',
    'what do you think about england ?',
    'what do you think about england during the reign of elizabeth ?',
    'what do you do ?',
    'What is the deepest spot on the world ?',
    'Do you like Mexican food or Indian food ?',
    'Who are you crazy about ?',
    'A man',
    'A women',
    'A dog',
    'A table',
    'A flower',
    'A man.',
    'A women.',
    'A dog.',
    'A table.',
    'A flower.',
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'The end',
    'Yes it is.',
    'Yes it was.',
    'Indeed.',
    'More',
    'More.',
    'More!',
    'What is the capital of France ?',
    'Paris...',
    'Where do you want to go ?',
    'Surprise me.'
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("500x650")

main.title("My Chat bot")
img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()