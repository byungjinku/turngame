import random

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, target):
        damage = random.randint(self.power - 2, self.power + 2)
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 피해!")
        target.hp -= damage
        if target.hp <= 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
            return True
        return False

class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, power=10)
        self.mp = 20
        self.magic_power = 15

    def magic_attack(self, target):
        if self.mp < 5:
            print("마나가 부족합니다.")
            return False
        self.mp -= 5
        damage = random.randint(self.magic_power - 3, self.magic_power + 3)
        print(f"{self.name}의 마법공격! {target.name}에게 {damage}의 피해!")
        target.hp -= damage
        if target.hp <= 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
            return True
        return False

class Monster(Character):
    def __init__(self):
        super().__init__("몬스터", hp=100, power=10)

def print_status(player, monster):
    print(f"{player.name}의 상태: HP {player.hp}, MP {player.mp}")
    print(f"{monster.name}의 상태: HP {monster.hp}")

def get_attack_type():
    while True:
        attack_type = input("어떤 공격을 하시겠습니까? (일반, 마법): ")
        if attack_type in ("일반", "마법"):
            return attack_type
        print("잘못된 입력입니다. 다시 선택해주세요.")

def main():
    print("=== 게임 시작 ===")
    player = Player(input("플레이어의 이름을 입력하세요: "))
    monster = Monster()
    attack_methods = {"일반": player.attack, "마법": player.magic_attack}
    while True:
        print_status(player, monster)
        attack_type = get_attack_type()
        if attack_methods[attack_type](monster):
            print(f"{player.name} 승리!")
            break
        if monster.attack(player):
            print(f"{monster.name} 승리!")
            break

if __name__ == "__main__":
    main()
