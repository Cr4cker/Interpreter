#Erforderliche Module importieren
from random import randint #Erforderlich beim erstellen der zufälligen Zahl
import ast #Erforderlich beim rechnen

#Willkommensgruß ;) (*Name* wird natürlich noch durch den Namen ersetzt den wir dem Interpreter geben!)
print("Hi! Dies ist *Name*. *Name* ist ein automatisches Programm zum ausführen von Eingaben! \nGeben sie 'help' ein für Hilfe")

#Die Eingabe des Benutzers mit der einfachen Variable "eingabe"
eingabe = input(">>>")

#Ewige Abfrage welcher Befehl eingegeben wurde
while True:
	
	#Hilfe
	if eingabe == "help":
		print("Geben sie 'rand' ein um eine Zufällige Zahl zu erstellen \nGeben sie 'exit' ein um *Name* zu verlassen \nGeben sie 'calc:rechnung' ein um eine Aufgabe auszurechnen Z.b. 'calc:1*1' Es wird nur + und - unterstützt!")
	
	#Zufällige Zahl erstellen
	elif eingabe == "rand":
		rand = input("Nennen sie nun den Zahlenbereich in dem die Zufällige Zahl erstellt werden soll. Z.b: '1:10' würde eine Zufällige Zahl von 1 bis 10 ausgeben!\n")
		(rand1, rand2) = rand.split(":", 1)
		print(randint(int(rand1), int(rand2)))
		
	#*Name* beenden
	elif eingabe == "exit":
		exit()
	
	#wenn ein Befehl gebraucht wird indem ein ':' vorkommt muss dieser hier eingetragen werden!
	elif ":" in eingabe:
		(befehl, inhalt) = eingabe.split(":", 1)
		#Zum benutzen eines weiteren Befehls mit ':' muss hier die Abfrage kommen nach dem Befehl kommen!
		if befehl == "calc":
			print(ast.literal_eval(inhalt))
	#Wenn etwas anderes eingegeben wurde wird ein Hinweis auf dem Bildschirm erscheinen
	else:
		print("Ein unerwarteter Fehler ist aufgetreten! Wieder holen sie bitte ihre Eingabe und achten sie auf eventuelle Fehler")
	#Letztendlich kommt nach jeder Abfrage ein neuer input
	eingabe = input(">>>")