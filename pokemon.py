class pokemon:
    def __init__(self,name,nickname,types,weakness):
        self.name = name
        self.nickname = nickname
        self.types = types
        self.weakness = weakness
charmander = pokemon("Charmander", "Char", "Fire", "Water")
while True:
    for i in range(11):
        print(charmander.nickname, "says:", charmander.name)
    newName = input("What is the new name of Charmander? ('quit' to quit) ")
    if newName == "quit":
        print("Thank you for playing")
        break
    else:
        charmander.nickname = newName

