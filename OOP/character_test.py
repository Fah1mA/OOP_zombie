from character import Character
dave = Character("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("i like human brains")
dave.talk()

from character import Enemy
dave = Enemy("Dave", "A smelly Zombie")

dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
