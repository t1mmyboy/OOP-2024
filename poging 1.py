class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type

    def attack(self):
        print(f"{self.name} attacks with a powerful move!")

# Create two Pokemon instances
pokemon1 = Pokemon("Pikachu", 10, "Electric")
pokemon2 = Pokemon("Charmander", 15, "Fire")

# Simulate a battle
print(f"A wild {pokemon2.name} appeared!")
print(f"Go, {pokemon1.name}!")

print(f"gemaakt in de Jorgon branch")

pokemon1.attack()
pokemon2.attack()
