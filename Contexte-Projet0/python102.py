# Classe

class GameCharacter:
    
    # constructeur
    # def __new__(self):
    #     pass
    
    # initialisateur
    def __init__(self, name, health, power):
        self._health = health #public
        self.name = name # protected
        self.power = power # private < < < MISE EN GARDE => name mangling
                            # name mangling
    
    # déclaration de propriété: accesseur (getter)
    @property
    def health(self):
        return self._health 
    
    # déclare ma propriété: mutateur (setter)
    @health.setter # décorateur de setter
    def health(self, value):
        self.health = max(0, value)
    
    # fonction
    def attack(self):
        print('attack')
    

variable = 
roger = GameCharacter('Roger', 100, 15)
william = GameCharacter('William', 150, 10)

print(f'roger a {roger.health} points de vie')
roger.attack()
GameCharacter.attack(roger)

# Pas de notions de private

# Notions de propriété sert aux programmeurs utilisateurs
# var = __h
# propriété cache le setter et le getter

# Decorateur