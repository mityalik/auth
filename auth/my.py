import time
f = open('student.txt','r+')
try:
    ans = int(input("Выберите действите:\n1- Регистрация\n2- Вход\n"))
    if ans == 1:
        flag = False
        log = input("Введите логин: ")
        for x in f.readlines():
            if x.split(",")[0] == log:
                flag = True
        if flag == False:
            print("Логин свободен")
            pas = input("Введите пароль: ")
            age =int(input("Введите возраст: "))
            name = input("Введите ФИ: ")
            f.write(f"\n{log},{age},{name},{pas}")
        else:
            print("Логин занят")
    elif ans == 2:
        flag = False
        log = input("Введите логин: ")
        for x in f.readlines():
            if x.split(",")[0] == log:
                flag = True
                print("Логин найден, введите пароль: ")
                pas = input()
                if (x.split(",")[3] == pas):
                    print(f"Вход выполнен, добро пожаловать, {log}")
                else:
                    print(f"Прошу прощения, {log}, пароль введен неверно.")
                    break
        if flag == False:
            print("Логин не найден в Базе Данных!")
        time.sleep(1)
    else:
        print("Неверный ввод! Повторите попытку позже")
        time.sleep(1)
        f.close()




finally:
    f.close()
