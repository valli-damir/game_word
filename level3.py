import time
from level4 import get_level4


def get_level3():
    start_time = time.time()
    letter = '"арсед"'
    words = 3
    print(f"Даны буквы {letter}")
    user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
    letters = ["адрес", "сад", "среда"]
    while True:
        if user in letters:
            letters.remove(user)
            print(f"Слово {user.upper()} есть в загаданных.")
            words -= 1
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
        elif words == 0:
            end_time = time.time()
            print(f"Level-3 пройден за {round(end_time - start_time, 2)} секунд. Поздравляем! ")
            level_4 = input(
                "выберите продолжить игру игру командой 'далее' или завершите игру командой 'выход'! ").lower()
            comands = ["далее", "выход"]
            if level_4 in comands[0]:
                get_level4()
                break
            elif level_4 in comands[1]:
                print("Игра завершена! ")
                break
            else:
                print("Не правильно ввели данные!")
                input(
                    "выберите продолжить игру игру командой 'далее' или завершите игру командой 'выход'! ").lower()
        else:
            print(f"Слова {user.upper()} нет в загаданных")
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
