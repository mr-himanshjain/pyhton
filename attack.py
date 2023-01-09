# import random

# class Enemy:
#     hp = 200

#     def __init__(self, atkl, atkh):
#         self.atkl = atkl
#         self.atkh = atkh


#     def getAtk(self):
#         print(self.atkl)
#         # print(self.atkh)

#     def getHp(self):
#         print("Hp is",self.hp)

# enemy1 = Enemy(40, 49)
# enemy1.getAtk()
# enemy1.getHp()

# enemy2 = Enemy(75, 90)
# enemy2.getAtk()
# enemy2.getHp()

# -----------------------------------
# # playerhp = 260
# # enemyatkl = 60
# # enemyatkh = 80

# # while playerhp > 0:
# #     dmg = random.randrange(enemyatkl, enemyatkh)
# #     playerhp = playerhp - dmg
# #     if playerhp <= 30:
# #         playerhp = 30
# #         print()
# #     print("enemy strike for ",dmg,"point of dmage. current HP is",playerhp)
# #     # if playerhp == 0:
# #     #     print("you can not respawn as you are dead")
# #     if playerhp == 30:

# #         print("your health is very low. you have been teleported nearest inn.")
# #         break


from classes.enemy import enemy

enemy = enemy(200, 60)
print("Hp = ",enemy.get_hp())