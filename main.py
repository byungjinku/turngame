import random

# 캐릭터 클래스 정의
class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, target, attack_type):
        # 공격 타입에 따른 데미지 계산
        if attack_type == "일반":
            damage = random.randint(self.power - 2, self.power + 2)
        elif attack_type == "마법":
            # 마나가 부족한 경우 예외 처리
            if self.mp < 5:
                print("마나가 부족합니다.")
                return False
            self.mp -= 5
            damage = random.randint(self.magic_power - 3, self.magic_power + 3)
        else:
            print("잘못된 입력입니다.")
            return False

        # 공격 결과 출력
        print(f"{self.name}의 {attack_type} 공격! {target.name}에게 {damage}의 피해!")
        target.hp -= damage
        if target.hp <= 0:
            target.hp = 0
            print(f"{target.name}이(가) 쓰러졌습니다.")
            return True
        return False

# 플레이어 클래스 정의
class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, power=10)
        self.mp = 20
        self.magic_power = 15

# 몬스터 클래스 정의
class Monster(Character):
    def __init__(self):
        super().__init__("몬스터", hp=100, power=10)

# 공격 타입 입력 함수 정의
def get_attack_type():
    while True:
        attack_type = input("어떤 공격을 하시겠습니까? (일반, 마법): ")
        if attack_type in ("일반", "마법"):
            return attack_type
        print("잘못된 입력입니다. 다시 선택해주세요.")

# 플레이어와 몬스터의 상태 출력 함수 정의
def print_status(player, monster):
    print(f"{player.name}의 상태: HP {player.hp}, MP {player.mp}")
    print(f"{monster.name}의 상태: HP {monster.hp}")

# 게임 실행 함수 정의
def game(player, monster):
    attack_methods = {"일반": player.attack, "마법": player.attack}
    while True:
        print_status(player, monster)
        attack_type = get_attack_type()
        if attack_methods[attack_type](monster, attack_type):
            print(f"{player.name} 승리!")
            return True
        if monster.attack(player, "일반"):
            print(f"{monster.name} 승리!")
            return False

# 메인 함수 정의
def main():
    print("=== 게임 시작 ===")
    player = Player(input("플레이어의 이름을 입력하세요: "))
    monster = Monster()
    try:
        game(player, monster)
    except KeyboardInterrupt:
        print("\n게임을 종료합니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
     main()
