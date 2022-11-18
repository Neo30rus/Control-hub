print("== Задание 4 ==")

users = [
    {"login": "admin", "password": "admin"},
    {"login": "cat", "password": "1234"},

]


def main():
    while True:
        print("Выберите действие:")
        print("1) Авторизация")
        print("2) Регистрация")
        print("3) Выход")
        print("4) Библиотека")
        print("5) Кредитный калькулятор")
        print("6) Викторина")

        act = input()
        if act == "1":
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            ok = False
            for user in users:
                if user["login"] == login:
                    if user["password"] == password:
                        ok = True
            if ok:
                print("Вход разрешён")
            else:
                print("Неправильный пароль")
        elif act == "2":
            login = input("Введите логин: ")
            password1 = input("Введите пароль: ")
            password2 = input("Повторите пароль: ")

            if password1 != password2:
                print("Пароли не совпадают")
                continue

            ok = True
            for user in users:
                if user["login"] == login:
                    ok = False
                    break

            if not ok:
                print("Пользователь с таким логином уже существует")
                continue

            users.append({
                "login": login,
                "password": password1,
            })

            print("Регистрация завершена")
        elif act == "4":
            inp = input("Введите банковский термин: ")
            with open("banking_ library.txt", "r", encoding="utf8") as file:
                library = file.read().split("\n")
                for banking in library:
                    words = banking.split(" – ")
                    if len(words) == 2:
                        term = words[0]
                        defn = words[1]
                        if inp.lower() == term.lower():
                            print(defn)
        elif act == "5":
            inp_sum = input("На какую сумму вы хотите сделать расчет?")
            inp_per = input("На какой период вы хотите взять кредит")
            inp_proc = input("Под какой процент вы хотите взять кредит")

            period = int(inp_per)
            summ = int(inp_sum)
            perc = int(inp_proc)
            print("1)Дифференцированная формула, 2)Аннуитентная формула")
            inp = input("Выберите какую формулу будете использовать: ")
            if inp == "1":
                arr = []
                mp_cnt = period * 12
                rest = summ
                mp_real = summ / (period * 12.0)
                while mp_cnt != 0:
                    mp = mp_real + (rest * perc / 1200)
                    arr.append(round(mp, 2))
                    rest = rest - mp_real
                    mp_cnt = mp_cnt - 1
                print(arr, round(sum(arr), 2))

            elif inp == "2":
                mp_cnt = period * 12
                r = perc / 1200.0
                ak = (r * (1 + r) ** mp_cnt) / (((1 + r) ** mp_cnt) - 1)
                mp = summ * ak
                total = mp * mp_cnt
                print( round(mp, 2), round(total, 2))
        elif act == "6":
            viktory()
        elif act == "3":
            break



def viktory():
    points = 0
    print(
        "1. Большая часть Банков явлется какой  организацией? Выберите правильный вариант ответа. \n 1)Кредитная \n 2) Государственная")
    q = input("Введите номер ответа: ")
    if q == "1":
        print("Верно! +5 баллов")
        points = points + 5
    elif q == "2":
        print("Ошибка! -3 балла")
        points = points - 3
    else:
        print("Выбрана неизвестная операция!")
        print("Ошибка! -1 балл")
        points = points - 1

    print("2.Сбербанк является какой организацией  \n 1)Частная  \n 2)Кредитная")
    q2 = input("Введите номер ответа: ")
    if q2 == "1":
        print("Ошибка! -3 балла")
        points = points + 5
    elif q2 == "2":
        print("Верно! +5 баллов")
        points = points - 3

    else:
        print("Выбрана неизвестная операция!")
        print("Ошибка! -1 балл")
        points = points - 1

    print(
        "3.Что такое надзор банка за банковским рынком: \n 1)анализ банковского рынка \n 2)систематическое изучение рыночной ситуации")
    q3 = input("Введите номер ответа: ")
    if q3 == "2":
        print("Ошибка! -3 балла")
        points = points + 5
    elif q3 == "1":
        print("Верно! +5 баллов")
        points = points - 3
    else:
        print("Выбрана неизвестная операция!")
        print("Ошибка! -1 балл")
        points = points - 1

    print(
        "4.Выделить определяющие характеристики стратегии проникновения на рынок: \n 1)предложения нового, ранее непредлагаемой услуги \n 2)предложение рынка традиционных услуг (кассовых, расчетных, кредитных); "
        )
    q4 = input("Введите номер ответа: ")
    if q4 == "2":
        print("Верно! +5 баллов")
        points = points + 5
    elif q4 == "1":
        print("Ошибка! -3 балла")
        points = points - 3
    else:
        print("Выбрана неизвестная операция!")
        print("Ошибка! -1 балл")
        points = points - 1

    print("5.Что чаще всего берут клиенты в банках дайте свой правильный ответ: ")
    q5 = input("Введите свой ответ: ")
    if q5 == "Кредиты":
        print("Верно! +10 баллов")
        points = points + 10
    else:
        print("Ошибка! -5 баллов")
        points = points - 5

    if 10 > points:
        print(
            " Вы не прошли викторину:( \n Пожалуйста,попробуйте еще раз! \n Ваш результат: " + str(points) + " баллов")
    else:
        print(
            "Вы прошли викторину вот вам подарок ваша кредитная карта с бесплатным обслуживанием! Ваш результат: " + str(
                points) + " баллов, Поздравляем!")
    input()


main()
