import time


def get_level4():
    start_time = time.time()
    letter = '"таубн"'
    words = 3
    print(f"Даны буквы {letter}")
    user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
    letters = ["табун", "бунт", "тан"]
    while True:
        if user in letters:
            letters.remove(user)
            print(f"Слово {user.upper()} есть в загаданных.")
            words -= 1
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
        elif words == 0:
            end_time = time.time()
            print(f"Level-4 пройден за {round(end_time - start_time, 2)} секунд. Поздравляем! ")
            level_5 = input(
                "выберите продолжить игру игру командой 'далее' или завершите игру командой 'выход'! ").lower()
            comands = ["далее", "выход"]
            if level_5 in comands[0]:
                print("Вы прошли игру! ")
                break
            elif level_5 in comands[1]:
                print("Игра завершена! ")
                break
            else:
                print("Не правильно ввели данные!")
                input(
                    "выберите продолжить игру игру командой 'далее' или завершите игру командой 'выход'! ").lower()
        else:
            print(f"Слова {user.upper()} нет в загаданных")
            user = input(f"Необходимо из букв {letter.upper()} составить слово. Осталось {words} слов ").lower()
