#Manav Shardha
#ICS4U
#October 9th, 2018
#Discount Skyrim V1

import random
import time

class player:
#add power 
    def __init__(self, name, health, shield, attack, heal, fire_attack, water_attack, snow_attack, description):

        self.name = name
        self.health = health
        self.attack = attack
        self.heal = heal
        self.shield = shield
        self.fire_attack = fire_attack
        self.water_attack = water_attack
        self.snow_attack = snow_attack
        self.description = description

'''
    def battle(self,other):
        if player.hp >= 0 and other.health >0:
            
'''
class Dragon:
    def __init__(self, health,attack, attack_damage, special_attack, special_attack_damage):
        self.health = health
        self.attack = attack
        self.attack_damage = attack_damage
        self.special_attack = special_attack
        self.special_attack_damage = special_attack_damage
        
      
    def battle(self, other):
        while self.health > 0 and other.health > 0:
            print("====================================================\n"+
                  "           " + str(player_name)+ "'s turn               \n"+
                  "====================================================\n")
            player_selection()
            opponent_selection()
            
            
    
            

def player_stats():
    print("\n\n"+
          str(player.name)+ " 's current stats are: \n" + "Health: " + str(player.health) + "\nAttack: " +
          str(player.attack) + "\nHeal: " +str(player.heal)+ "\nShield: " + str(player.shield) +" \n\n") 

def player_stat_upgrade():
    global player
    player_stat_points = 10
    while not player_stat_points == 0:
        player_stats()
        print(player_name +" has " +str(player_stat_points)+" points to improve attributes \n") 
        while True:
            try:
                user_choice = int(input("\nWhat attribute do you wish to improve: \n 1. Health \n 2. Attack \n"+
                                        " 3. Heal \n 4. Shield \n Selection:"))
                if user_choice == 1: 
                    player.health += 1
                    player_stat_points -= 1
                elif user_choice == 2:
                    player.attack += 1
                    player_stat_points -= 1
                elif user_choice == 3:
                    player.heal += 1
                    player_stat_points -= 1
                elif user_choice == 4:
                    player.shield += 1
                    player_stat_points -= 1
                else:
                    print("Invalid selection")        
                break
            
            except ValueError:
                print("The user must enter an integer of 1, 2 ,3 or 4")


        
            
def player_selection():
    user_choice = 0
    while not(0 < user_choice < 4):
        try:
            user_choice = int(input("Would you like to: \n1. Attack, \n2. Defend \n3. Heal \nSelection: "))
        
        except ValueError:
            print("The user must enter either 1, 2 or 3 as an input")

        if user_choice == 1:
            pass
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        else:
            print("Invalid input")
        


    


def random_opponent():
    pass

def opponent_selection():
    pass

                            

player_name = input("Please enter the name you wish to play with: ")

player = player(player_name, 15, 0, 5, 2, "Inferno", "Flood", "Frostbite"," Fire attacks are strong against snow dragrons,"
              "Water attacks are strong against fire dragons and Lighning attacks are strong against Water dragons")

player_selection()
#player_stat_upgrade()
                  

