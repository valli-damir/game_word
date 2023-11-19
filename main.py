import time
from level2 import get_level2


def get_game():
    start_time = time.time()
    letter = '"омхр"'
    words = 4
    print(f"Даны буквы {letter}")
    user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
    letters = ["мох", "хром", "ром", "ом"]
    while True:
        if user in letters:
            letters.remove(user)
            print(f"Слово {user.upper()} есть в загаданных.")
            words -= 1
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
        elif words == 0:
            end_time = time.time()
            print(f"Level-1 пройден за {round(end_time - start_time, 2)} секунд. Поздравляем! ")
            level2 = input(
                "выберите продолжить игру игру командой 'далее' или завершите игру командой 'выход'! ").lower()
            comands = ["далее", "выход"]
            if level2 in comands[0]:
                get_level2()
                break
            elif level2 in comands[1]:
                print("Игра завершена! ")
                break
            else:
                print("Не правильно ввели данные!")
                input("Выберите продолжить игру командой 'далее' или завершите игру командой 'выход'! ").lower()
        else:
            print(f"Слова {user.upper()} нет в загаданных")
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()


if __name__ == "__main__":
    get_game()
