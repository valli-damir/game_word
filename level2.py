import time
from level3 import get_level3


def get_level2():
    start_time = time.time()
    letter = '"рткаук"'
    words = 3
    print(f"Даны буквы {letter}")
    user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
    letters = ["куртка", "утка", "акр"]
    while True:
        if user in letters:
            letters.remove(user)
            print(f"Слово {user.upper()} есть в загаданных.")
            words -= 1
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
        elif words == 0:
            end_time = time.time()
            print(f"Level-2 пройден за {round(end_time - start_time, 2)} секунд. Поздравляем! ")
            level_3 = input(
                "выберите продолжить игру игру командой 'далее' или завершите игру командой 'выход'! ").lower()
            comands = ["далее", "выход"]
            if level_3 in comands[0]:
                get_level3()
                break
            elif level_3 in comands[1]:
                print("Игра завершена! ")
                break
            else:
                print("Не правильно ввели данные!")
                input(
                    "выберите продолжить игру игру командой 'далее' или завершите игру командой 'выход'! ").lower()
        else:
            print(f"Слова {user.upper()} нет в загаданных")
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
