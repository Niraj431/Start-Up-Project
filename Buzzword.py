#erforderliche Module
import random
import sys
import os
from prettytable import PrettyTable
import tkinter as tk
from colorama import init, Fore
init(autoreset=True) 
from playsound import playsound


def Karte_Erstellen(breite,liste):
                
        Karte = {}
        
        for elem in range(0,breite):
            Karte[str(elem+1)]=[random.sample(liste,k=breite)]
            
        for Zahl in Karte:
            if Zahl == '3':
                if breite == 5:
                    Karte[Zahl][0][2] = '\033[40m'+'\033[31m' + "       X       " + '\033[39m' + '\033[49m'
            elif Zahl == '4':
                if breite == 7:
                    Karte[Zahl][0][3] = '\033[40m'+'\033[31m' + "       X       " + '\033[39m' + '\033[49m'
        return Karte


def Karte_Ausgeben(Karte):
    if höhe == 3 & breite == 3:
        t = PrettyTable(['1', '2', '3'])
    elif höhe == 5 & breite == 5:
       t = PrettyTable(['1', '2', '3', '4', '5'])
    elif höhe == 7 & breite == 7:
        t = PrettyTable(['1', '2', '3', '4', '5', '6', '7'])

    for Zahl in Karte:
        t.add_row((Karte[Zahl][0]))
    print(t)

def gezogenes_wort(Karte, liste,wort_eingabe):
    for Zahl in Karte:
        y = 0
        if wort_eingabe == "exit":
                quit()
        elif wort_eingabe != "exit":
            for wort in Karte[Zahl][0]:         
                if wort.casefold() == wort_eingabe.casefold():
                    Karte[Zahl][0][y] = '\033[40m'+'\033[31m' + "       X       " + '\033[39m' + '\033[49m'
                    playsound('damn.mp3')
                    return wort_eingabe

                y += 1 


    if wort.casefold() != wort_eingabe.casefold():
        print(Fore.GREEN + "Geben sie bitte ein Wort aus der Liste ein")

    return wort_eingabe    

def Prüfen(Karte,höhe,breite):

    sieg = False
    #horizontaler Gewinn

    for Zahl in Karte:
        counter = 0   
        for x in range(0,int(höhe)):
            if Karte[Zahl][0][x]=='\033[40m'+'\033[31m' + "       X       " + '\033[39m' + '\033[49m':
                counter+= 1

        if counter is int(höhe):
            sieg = True
            return sieg

    #vertikaler Gewinn
    for x in range(0,int(höhe)):
        counter=0

        for Zahl in Karte:
            if Karte[Zahl][0][x]=='\033[40m'+'\033[31m' + "       X       " + '\033[39m' + '\033[49m':
                counter+=1
        if counter==int(höhe):
            sieg=True
            return sieg

    #diagonaler Gewinn links oben nach rechts unten
    for x in range (0,int(höhe)):
        y=0
        counter=0
        for Zahl in Karte:
            if Karte[Zahl][0][y]=='\033[40m'+'\033[31m' + "       X       " + '\033[39m' + '\033[49m':
                counter+=1
            y+=1
        if counter==int(höhe):
            sieg=True
            return sieg

    #diagonaler Gewinn von rechts oben nach links unten
    for x in range (int(höhe)):
        y=int(höhe)-1
        counter=0
        for Zahl in Karte:
            if Karte[Zahl][0][y]=='\033[40m'+'\033[31m' + "       X       " + '\033[39m' + '\033[49m':
                counter+=1
            y-=1
        if counter==int(höhe):
            sieg=True
        return sieg

#Methode, um Spiel bei Fehinput neuzustarten
def restart():
    print("Spiel startet neu aufgrund von eines FehlInputs" + "\n" + "------------------------" + "\n")
    os.execv(sys.executable, ['/bin/python3'] + sys.argv) 
#Methode, um Spiel bei Fehlinput speziell bei der Eingabe von Höhe & Breite neuzustarten
def restarthöhebreite():
    print("Spiel startet neu aufgrund von eines FehlInputs")
    print("Bitte geben sie nur 3 x 3, 5 x 5, 7 x 7 ein" + "\n" + "------------------------" + "\n")
    os.execv(sys.executable, ['/bin/python3'] + sys.argv) 
def beenden():
    user_input = input()
    if user_input == "exit":
        quit()



###MAINMETHODE###
print('\033[40m'+
"""
 ____                                       _   ____  _                   
|  _ \                                     | | |  _ \(_)                  
| |_) |_   _ __________      _____  _ __ __| | | |_) |_ _ __   __ _  ___  
|  _ <| | | |_  /_  /\ \ /\ / / _ \| '__/ _` | |  _ <| | '_ \ / _` |/ _ \ 
| |_) | |_| |/ / / /  \ V  V / (_) | | | (_| | | |_) | | | | | (_| | (_) |
|____/ \__,_/___/___|  \_/\_/ \___/|_|  \__,_| |____/|_|_| |_|\__, |\___/ 
Fuat, Duc und Niraj                                            __/ |      
                                                              |___/       """+'\033[49m') 
print('\033[40m'+'\033[31m' +"In diesem Spiel sind Audiodateien enthalten. Bitte Lautstärke regulieren! " )

#Textdatei wird ausgelesen, Wörter werde in der Datei mit ";" getrennt
datei = open('wörter.txt','r')
liste=[]
liste = datei.read().split(';')

#Fehlererkennung bei Userinput#
while True:
    try:
        höhe=int(input("\n" +"Es gibt nur die Spielfeldgrößen " + '\033[96m' + '\033[40m'+ "3x3, 5x5" '\033[39m'+'\033[49m'+ " und " 
        +'\033[96m' + '\033[40m'+ "7x7"+ '\033[39m'+'\033[49m'+ "\n"+"Geben sie die Höhe der Bingokarte ein:" + "\n"))
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
'\033[96m' + '\033[40m'+ "3x3, 5x5" '\033[39m'+'\033[49m'
while True:
    try:
        modi = int(input("Wählen sie zwischen Zwei Spiel Modi aus Tippen sie die jeweilige Zahl ein:" + "\n"

+'\033[96m' + '\033[40m' + "1: Einzelspieler"  +'\033[39m'+'\033[49m' + "\n"
'\033[96m' + '\033[40m' + "2: Mehrspieler"  +'\033[39m'+'\033[49m' + "\n"))

        break

    except ValueError:
        print("\n" + "Bitte geben Sie NUR die Ziffern 1 oder 2 ein und kein Buchstabe. Versuchen sie es erneut")
        restart() 

#################

spielfeld=[]

#Spielstart im Eizelspielermodus
if modi == 1:
    einzelspieler = Karte_Erstellen(breite,liste)
    spielfeld.append(einzelspieler)
    anzahl_spieler = 1
    for x in range(0,anzahl_spieler):
        Karte = Karte_Ausgeben(spielfeld[x])

#Spielstart in Mehrspielermodus
elif modi == 2: 
    while True:
        try:
            anzahl_spieler=int(input('Bitte geben Sie an, wie viele Personen am Bingospiel teilnehmen möchten!'+ "\n"))
            break
        except ValueError:
            restart()


    for x in range(0,int(anzahl_spieler)):
        spielfeld.append(Karte_Erstellen(breite,liste))
    if höhe == 3 & breite == 3:
        t = PrettyTable(['1', '2', '3'])
    elif höhe == 5 & breite == 5:
       t = PrettyTable(['1', '2', '3', '4', '5'])
    elif höhe == 7 & breite == 7:
        t = PrettyTable(['1', '2', '3', '4', '5', '6', '7'])



    #Karten werden basierend auf der Anzahl der Spieler exportiert (Exportfunktion)
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
Es wurden """ + str(anzahl_spieler) + """ Bingo Karten generiert und in dem Verzeichnis gespeichert, wo sich das Projekt befindet.
""")

    quit()
    #Spiel wird beendet, nachdem die Karten exportiert wurden. 


elif modi != 1 or 2:

    print("\n" + "Bitte geben Sie NUR die Ziffern 1 oder 2 ein. Versuchen sie es erneut")
    print("Das Spiel wird neugestartet" + "\n")
    restart() 


print('''
Viel spaß beim Spielen wünschen euch Fuat, Duc und Niraj :)
''')

#Einzelspielermodus Gewinnbekanntgabe mit Detail(wie viele Wörter gezogen wurden)
sieg = False

for x in range(0,int(anzahl_spieler)):

        sieg=Prüfen(spielfeld[x],int(höhe),int(breite))
        words_till_win = 0
        wort_eingabe = input("Bitte geben sie das Wort ein was sie Markiert haben wollen" + "\n")
        while not sieg and wort_eingabe != "exit":
            wort_eingabe = gezogenes_wort(spielfeld[x], liste, wort_eingabe)
            words_till_win += 1
            #Solange das Spiel noch nicht gewonnen ist, wird jedes eingegebene Wort mitgezählt

            print(f"\nGeschriebenes Wort: {wort_eingabe}.")
            print(f"Anzahl der eingegeben Wörtern: {words_till_win}.\n")
            Karte_Ausgeben(spielfeld[x])

            #Gewinn wird überprüft, wenn True --> Laufschrift
            sieg=Prüfen(spielfeld[x],int(höhe),int(breite))

            #Laufschrift bei Sieg
            if sieg==True:
                
                print("\033[1;35;40m\n"+'\033[35m'+f"\nSie haben Gewonnen!\nSoviele Wörter wurden eingegeben: {words_till_win}."+
                '\033[39m' + "\033[1;35;40m\n")
                APP_TITEL = "LAUFSCHRIFT - GEWINN"
                xposition = 300
                yposition = 300
                weite_fenster = 300
                höhe_fenster = 300
                SCROLLEN_TEXT = "GLÜCKWUNSCH! Sie haben GEWONNEN!"

                class Application(tk.Frame):

                    def __init__(self, master):
                        self.master = master
                        tk.Frame.__init__(self, master)

                        self.canvas = tk.Canvas(self, bg='cyan', highlightthickness=0)
                        self.canvas.pack(expand=True)

                        xpos = weite_fenster
                        ypos = 100
                        self.canvas.create_text(xpos, ypos, anchor='w', text=SCROLLEN_TEXT,
                            font=('Helvetica 30 bold'), tags='text')

                        text_anfang = self.canvas.bbox('text')[0]
                        text_ende = self.canvas.bbox('text')[2]
                        self.text_länge = text_ende - text_anfang

                        self.scroll_text()

                    def scroll_text(self):
                        self.canvas.move('text', -2, 0)
                        text_ende = self.canvas.bbox('text')[2]
                        if text_ende < 0:
                            self.canvas.move('text', weite_fenster + self.text_length, 0)

                        self.canvas.after(20, self.scroll_text)

                def anwenden():
                    app_win = tk.Tk()
                    app_win.title(APP_TITEL)
                    app_win.geometry("+{}+{}".format(xposition, yposition))
                    app_win.geometry("{}x{}".format(weite_fenster, höhe_fenster))

                    app = Application(app_win).pack(fill='both', expand=True, padx=0, pady=0)
                    playsound('youwin.mp3')
                    app_win.mainloop()
                    quit()
                if __name__ == '__main__':
                    anwenden()
                beenden()

            wort_eingabe = input("Bitte geben sie das Wort ein was sie Markiert haben wollen" + "\n") 
