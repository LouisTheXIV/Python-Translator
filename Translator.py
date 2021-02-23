from translate import Translator
from tkinter import *

screen = Tk()

def translate():
    word = word_entry.get()
    lang = lang_entry.get()
    translator= Translator(to_lang=lang)
    translation = translator.translate(word)
    theTranslation = Label(screen1, text = translation)
    theTranslation.pack()

def lang_screen():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Louis's Translator")
    screen1.geometry("450x300")
    
    Label(screen1, text="Langauge").pack()
    global lang_entry
    lang_entry = Entry(screen1, width=50, fg='blue')
    lang_entry.pack()
    global word_entry
    Label(screen1, text="Word/Sentence").pack()
    word_entry = Entry(screen1, width=50, fg='blue')
    word_entry.pack()
    Label(text="").pack()
    Button(screen1, text="Translate", width=10, height=1, fg='red', command=translate).pack()
    

def main_screen():
    screen.geometry("600x350")
    screen.title("Louis's Translator Welcome")
    Label(text="Louis's Translator", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="Hello and welcome to Louis's Translator! This program only supports English to any language").pack()
    Label(text="Created by Matei Diamandi aka Louis the XIV. Software Version: 1.0").pack()
    Button(text = "Start the Translator!", height="2", width="300", command=lang_screen).pack()

    screen.mainloop()

main_screen()



##word = input("Hello and welcome to Translator 1.0! Press Enter to continue")
##while True:
##    lang = input("English to what language? ")
##    word = input("Type a word or sentece in English and it will be translated to " + str(lang) + " ")
##    translator= Translator(to_lang=lang)
##    translation = translator.translate(word)
##    print (translation)
