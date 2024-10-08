class Player:
    
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur",pseudo, "/ Points de vie:", health, "/ Attaque: ", attack)
        
    def get_pseudo(self):
        return self.pseudo
        
    def get_health(self):
        return self.health
    
    def get_attack_value(self):
        return self.attack
    
    def damage(self,damage):
        self.health -= damage
        
    def attack_player(self, target_player):
        target_player.damage(self.attack)
        
player1 = Player("John", 20, 3)
player2 = Player("Marie", 20, 5)
player1.attack_player(player2)

print(player1.get_pseudo(), "attaque ", player2.get_pseudo())

print("Bienvenue au joueur",player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque: ", player1.get_attack_value())
print("Bienvenue au joueur",player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque: ", player2.get_attack_value())
