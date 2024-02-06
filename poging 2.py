repeat = True
#The player start the game.
print("Welcome tot de wereld van pokemon!")
print("wilt u starten? (ja/nee)")
if input() == "ja":
    print("je bent nu in de wereld van pokemon!")
else:
    print("bye!")
    exit()
#The player gives a name to a charmander.
print("geef je charmander een naam")
name = input()
print("je charmander heet nu " + name)
#The charmander does its battle cry for ten times.
for i in range(10):
    print(name + " doet zijn battle cry!")
#The player can give a new name to the same charmander.
while repeat == True:
    print("wil je " + name + " een nieuwe naam geven? (ja/nee)")
    if input() == "ja":
        print("geef je charmander een nieuwe naam")
        name = input()
        print("je charmander heet nu " + name)
        for i in range(10):
         print(name + " doet zijn battle cry!")
    else:
        print("ok")
#The charmander does its battle cry for ten times.
        for i in range(10):
         print(name + " doet zijn battle cry!")
#Repeat 4 and 5 until the player quits the game.
    print("wil je stoppen? (ja/nee)")
    if input() == "ja":
        print("bye!")
        exit()
    else:
        repeat = True
