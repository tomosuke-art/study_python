# 演習問題
# Characterクラスを作成、インスタンス変数としてname,hit,offence,defense
# を持たせ、キャラ同士を戦わせる
class CharacterAlreadyExistException(Exception):
    pass

class AllCharacters:
    all_characters = [] # 全てのキャラクター
    alive_characters = [] # 生きてるキャラクター
    dead_characters = [] # 死んでるキャラクター

    @classmethod
    # キャラ追加のメソッド
    def character_append(cls,name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターは既に存在しています。')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)
    
    @classmethod
    # キャラ削除のメソッド
    def character_delete(cls,name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)
class Character:

    def __init__(self,name,hp,offense,defense):
        AllCharacters.character_append(name) # クラスメソッドを呼ぶ
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense
    
    def attack(self,enemy, critical_point=1):
        if self.hp <= 0:
            print("キャラクターは既に死んでいます")
            return
        attack_point = self.offense - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0: # 敵キャラのhpが0以下になったら
            AllCharacters.character_delete(enemy.name)
    
    def critical_hit(self, enemy): # 2倍のダメージ
        self.attack(enemy,2)

character_a = Character("女型の巨人",10,5,3) # name,hp,offense,defense
character_b = Character("鎧の巨人",8,6,2)
print(character_b.hp)
character_a.critical_hit(character_b) # hp:8 -> 2
print(character_b.hp)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
character_a.attack(character_b) # hp:2 -> -1
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
character_b.attack(character_a) # キャラクターは既に死んでいます