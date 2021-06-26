import random
import sys
import os
from tkinter.constants import TRUE
from prettytable import PrettyTable
import tkinter as tk
from colorama import init, Fore, Style
init()

def Karte_Erstellen(höhe,breite,liste):
        Karte = { 

            } 
        for x in range(0,höhe):
            Karte[str(x+1)]=[random.sample(liste,k=breite)]
        for Zahl in Karte:
            if Zahl =='3':
                if höhe==5 and breite==5:
                    Karte[Zahl][0][2] = "X"
            elif Zahl=='4':
                if höhe==7 and breite==7:
                    Karte[Zahl][0][3] = "X"

        return Karte

def Karte_Ausgeben(Karte):
    if höhe==3 & breite==3:
        t = PrettyTable(['1', '2', '3'])
    elif höhe==5 & breite==5:
       t = PrettyTable(['1', '2', '3', '4', '5'])
    elif höhe==7 & breite==7:
        t = PrettyTable(['1', '2', '3', '4', '5', '6', '7'])

    for Zahl in Karte:
        t.add_row((Karte[Zahl][0]))
    print(t)

import curses

"""def mouse(stdscr):
    curses.curs_set(0)
    curses.mousemask(1)

    key = stdscr.getch()

    if key == curses.KEY_MOUSE:
        stdscr.addstr(0,0, "Klick")
        stdscr.refresh()
    stdscr.getch()

curses.wrapper(mouse)"""
def gezogenes_wort(Karte, liste,wort_ziehen):
    for Zahl in Karte:
        y = 0
        z = 1
        l = 2
        for wort in Karte[Zahl][0]:
            if Karte[Zahl][0][y].casefold() != wort_ziehen.casefold():

                print(Fore.GREEN + "Geben sie bitte ein Wort aus der Liste ein")
                print(Style.RESET_ALL, end="")
                break

            elif Karte[Zahl][0][z].casefold() != wort_ziehen.casefold():

                print(Fore.GREEN + "Geben sie bitte ein Wort aus der Liste ein")
                print(Style.RESET_ALL, end="")
                break

            elif Karte[Zahl][0][l].casefold() != wort_ziehen.casefold():

                print(Fore.GREEN + "Geben sie bitte ein Wort aus der Liste ein")
                print(Style.RESET_ALL, end="")
                break 

        for wort in Karte[Zahl][0]:
            if Karte[Zahl][0][y].casefold() == wort_ziehen.casefold():
                Karte[Zahl][0][y] = "X"

            y += 1

        for wort in Karte[Zahl][0]:
            if Karte[Zahl][0][z].casefold() == wort_ziehen.casefold():
                Karte[Zahl][0][z] = "X"

            z -= 1
        for wort in Karte[Zahl][0]:
            if Karte[Zahl][0][l].casefold() == wort_ziehen.casefold():
                Karte[Zahl][0][l] = "X"

            l -= 2 
    return wort_ziehen     

def Prüfen(Karte,höhe,breite):

    sieg = False
    #Zunächst werden die horizontalen Gewinne nachgeprüft

    for Zahl in Karte:
        counter = 0   
        for x in range(0,int(höhe)):
            if Karte[Zahl][0][x]=='X':
                counter+= 1

        if counter is int(höhe):
            sieg = True
            return sieg

    #jetzt werden die vertikalen Gewinne nachgeprüft
    for x in range(0,int(höhe)):
        counter=0

        for Zahl in Karte:
            if Karte[Zahl][0][x]=='X':
                counter+=1
        if counter==int(höhe):
            sieg=True
            return sieg

    #jetzt werden die diagonalen Gewinne nachgeprüft
    for x in range (0,int(höhe)):
        y=0
        counter=0
        for Zahl in Karte:
            if Karte[Zahl][0][y]=='X':
                counter+=1
            y+=1
        if counter==int(höhe):
            sieg=True
            return sieg

    for x in range (int(höhe),-1,-1):
        y=int(höhe)-1
        counter=0
        for Zahl in Karte:
            if Karte[Zahl][0][y]=='X':
                counter+=1
            y-=1
        if counter==int(höhe):
            sieg=True
        return sieg


def restart():
    print("Spiel startet neu aufgrund von eines FehlInputs" + "\n" + "------------------------" + "\n")
    os.execv(sys.executable, ['/bin/python3'] + sys.argv) 
def restarthöhebreite():
    print("Spiel startet neu aufgrund von eines FehlInputs")
    print("Bitte geben sie nur 3 x 3, 5 x 5, 7 x 7 ein" + "\n" + "------------------------" + "\n")
    os.execv(sys.executable, ['/bin/python3'] + sys.argv) 


#Mainmethode
print(""" 
 ____                                       _   ____  _                   
|  _ \                                     | | |  _ \(_)                  
| |_) |_   _ __________      _____  _ __ __| | | |_) |_ _ __   __ _  ___  
|  _ <| | | |_  /_  /\ \ /\ / / _ \| '__/ _` | |  _ <| | '_ \ / _` |/ _ \ 
| |_) | |_| |/ / / /  \ V  V / (_) | | | (_| | | |_) | | | | | (_| | (_) |
|____/ \__,_/___/___|  \_/\_/ \___/|_|  \__,_| |____/|_|_| |_|\__, |\___/ 
Fuat, Duc und Niraj                                            __/ |      
                                                              |___/       """)   

datei = open('text.txt','r')
liste=[]
liste = datei.read().split(';')

#Fehlererkennung bei Userinput#
while True:
    try:
        höhe=int(input("\n" + "Geben sie die Höhe der Bingokarte ein:" + "\n"))
        breite=int(input('Geben sie die Breite der Bingokarte ein:' + "\n"))
        acceptable_values = list((3, 5, 7))
        if höhe and breite in acceptable_values and höhe == breite:
            break
        else:
            restarthöhebreite()
    except ValueError:
        print("\n" + "Bitte geben Sie NUR die Ziffern ein. Versuchen sie es erneut")
        print("Das Spiel wird neugestartet" + "\n")
        restart()

while True:
    try:
        modi = int(input('''Wählen sie zwischen Zwei Spiel Modi aus Tippen sie die jeweilige Zahl ein:

1: Einzelspieler
2: Mehrspieler''' + "\n"))

        break

    except ValueError:
        print("\n" + "Bitte geben Sie NUR die Ziffern 1 oder 2 ein und kein Buchstabe. Versuchen sie es erneut")
        restart() 

#################

spielfeld=[]


if modi == 1:
    einzelspieler = Karte_Erstellen(höhe,breite,liste)
    spielfeld.append(einzelspieler)
    anzahl_spieler = 1
    for x in range(0,anzahl_spieler):
        Karte = Karte_Ausgeben(spielfeld[x])
elif modi == 2: 
    anzahl_spieler=input('Bitte geben Sie an, wie viele Personen am Bingospiel teilnehmen möchten!'+ "\n")
    for x in range(0,int(anzahl_spieler)):
        spielfeld.append(Karte_Erstellen(höhe,breite,liste))
    if höhe == 3 & breite == 3:
        t = PrettyTable(['1', '2', '3'])
    elif höhe == 5 & breite == 5:
       t = PrettyTable(['1', '2', '3', '4', '5'])
    elif höhe == 7 & breite == 7:
        t = PrettyTable(['1', '2', '3', '4', '5', '6', '7'])




    for x in range(0,int(anzahl_spieler)):
        f = open("Karte"+str(x+1), 'w')#karten erzeugt
        Karte=spielfeld[x]

        for Zahl in Karte:

            t.add_row(Karte[Zahl][0])
        f.write(str(t))

        for Zahl in Karte:
            for Zahl in range(0,1):
                t.del_row(Zahl)



        f.close

    print("""
Es wurden """ + anzahl_spieler + """ Bingo Karten generiert und in dem Verzeichnis gespeichert, wo sich das Projekt  befindet.
Schreiben sie "quit" um das Spiel zu beenden.""")

    user_input=input()
    if user_input=='quit':
        print('Viel Spaß beim Spielen!!!')
        quit()


elif modi != 1 or 2:

    print("\n" + "Bitte geben Sie NUR die Ziffern 1 oder 2 ein. Versuchen sie es erneut")
    print("Das Spiel wird neugestartet" + "\n")
    restart() 




print('''
Das Spiel beginnt jetzt!
ES wird immer wieder aus einer Liste Wörter gezogen, und wenn diese
in deiner Bingokarte vorkommen, so werden diese durch ein X ersetzt.
Drücken sie Enter um das erste Wort einzugeben
''')

sieg = False


for x in range(0,int(anzahl_spieler)):

        sieg=Prüfen(spielfeld[x],int(höhe),int(breite))
        words_till_win = 0
        wort_ziehen = input("Bitte geben sie das Wort ein was sie Markiert haben wollen" + "\n")
        while not sieg and wort_ziehen != "quit":
            wort_ziehen = gezogenes_wort(spielfeld[x], liste, wort_ziehen)
            words_till_win += 1



            print(f"\nGeschriebenes Wort: {wort_ziehen}.")
            print(f"Anzahl der eingegeben Wörtern: {words_till_win}.\n")
            Karte_Ausgeben(spielfeld[x])

            sieg=Prüfen(spielfeld[x],int(höhe),int(breite))


            if sieg==True:
                print(f"\nSie haben Gewonnen!\nSoviele Wörter wurden gezogen: {words_till_win}.")
                print("\033[1;35;40m\n")
                print(f"\nSie haben Gewonnen!\nSoviele Wörter wurden gezogen: {words_till_win}.")
                APP_TITLE = "TkTemplate_Idiom_01"
                APP_XPOS = 300
                APP_YPOS = 300
                APP_WIDTH = 300
                APP_HEIGHT = 300
                SCROLL_TEXT = "GLÜCKWUNSCH! Sie haben GEWONNEN!"

                class Application(tk.Frame):

                    def __init__(self, master):
                        self.master = master
                        tk.Frame.__init__(self, master)

                        self.canvas = tk.Canvas(self, bg='cyan', highlightthickness=0)
                        self.canvas.pack(expand=True)

                        xpos = APP_WIDTH
                        ypos = 100
                        self.canvas.create_text(xpos, ypos, anchor='w', text=SCROLL_TEXT,
                            font=('Helvetica 30 bold'), tags='text')

                        text_begin = self.canvas.bbox('text')[0]
                        text_end = self.canvas.bbox('text')[2]
                        self.text_length = text_end - text_begin

                        self.scroll_text()

                    def scroll_text(self):
                        self.canvas.move('text', -2, 0)
                        text_end = self.canvas.bbox('text')[2]
                        if text_end < 0:
                            self.canvas.move('text', APP_WIDTH + self.text_length, 0)

                        self.canvas.after(20, self.scroll_text)

                def anwenden():
                    app_win = tk.Tk()
                    app_win.title(APP_TITLE)
                    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
                    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))

                    app = Application(app_win).pack(fill='both', expand=True, padx=0, pady=0)

                    app_win.mainloop()
                if __name__ == '__main__':
                    anwenden()
            wort_ziehen = input("Bitte geben sie das Wort ein was sie Markiert haben wollen" + "\n")
            if wort_ziehen=='quit':
                print('Das Spiel wurde vom Benutzer beendet')
                quit()