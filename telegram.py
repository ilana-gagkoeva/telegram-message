from time import *
username = ''
password = ''
tours = [
        "Экскурсия по городу Владикавказ - стоимость без доп. услуг. 50 000 рублей",
        "Тур по популярным местам - стоимость без доп. услуг. 100 000 рублей",
        "Поход в горы - стоимость без доп. услуг. 70 000 рублей"
    ]
prices = [
    50000,
    100000,
    70000
]
history = []

def registration():
    global username, password
    print("Для выбора тура необходима регистрация.")
    sleep(2)
    username = input("Укажите имя пользователя:")
    password = input("Придумайте пароль:")
    repeat_password = input("Повторите пароль:")
    if password == repeat_password:
        print("Регистрация прошла успешно!")
        sleep(2)
    else:
        print("Пароли не совпадают. Попробуйте еще раз.")
        sleep(2)

def dashboard():
    sleep(2)
    print("Выберите нужное действие:")
    print("1 - Сменить имя пользователя,")
    print("2 - Изменить пароль,")
    print("3 - Забронировать тур,")
    print("4 - Посмотреть историю заказов.")
    choice = int(input("Введите номер действия:"))
    if choice == 1:
        rename()
    elif choice == 2:
        change_password()
    elif choice == 3:
        tour = reservation()
        history.append([tours[tour[0]-1], f'Дата поездки: {tour[1]}'])
        message = notification(tour)
        print("Сообщение администатору: ",message)
        send_tg(message)
    elif choice == 4:
        show_history()

def rename():
    global username
    username = input("Укажите новое имя пользователя:")
    print("Имя пользователя успешно изменено на:", username)

def change_password():
    global password
    old_password = input("Введите старый пароль:")
    if old_password == password:
        pass
    else:
        print("Пароль не соответствует.")
        forgot = input("Вы забыли пароль?")
        if forgot == "да":
            reset_password()
        return
    password = input("Придумайте новый пароль:")
    repeat_password = input("Повторите новый пароль:")
    if password == repeat_password:
        print("Пароль успешно изменен!")
    else:
        print("Пароли не совпадают. Попробуйте еще раз.")

def reset_password():
    login = input("Введите имя пользователя, привязанное к аккаунту:")
    if login == username:
        print("Отправили вам на почту ссылку для сброса пароля.")
    else:
        print("Пользователь не найден.")
  
def reservation():
    show_all_tours()
    tour = int(input("Выберите номер тура:"))
    itogo = prices[tour-1]

    date = input("Введите дату, когда хотите поехать:")
    time = input("Выберите время поездки:")
    adults = int(input("Сколько будет взрослых?"))
    kids = int(input("Сколько будет детей?"))
    nutrition = input("Нужно ли питание? (стоимость: 8000 руб.)")
    if nutrition == "да" or nutrition == "+":
        itogo += 8000
    transfer = input("Нужен ли трансфер от и до аэропорта? (стоимость: 5000 руб.)")
    if transfer == "да" or transfer == "+":
        itogo += 5000
    residence = input("Нужно ли проживание? (стоимость: 3000 руб/сутки)")
    days = int(input("Сколько дней?"))
    if residence == "да" or residence == "+":
        itogo += 3000 * days
    print("Тур забронирован успешно!")
    return tour, date, time, adults, kids, nutrition, transfer, residence, days, itogo

def show_history():
    sleep(2)
    print("История ваших заказов:")
    number = len(history)
    for i in range(len(history)-1, -1, -1):
        print("Тур", number)
        print(history[i][0])
        print(history[i][1])
        number -= 1

def show_all_tours():
    sleep(2)
    print("Список доступных туров:")
    number = 1
    for tour in tours:
        print(number, "-", tour)
        number += 1   

def notification(tour):
    message = 'Получен новый заказ! \n'
    message += "Заказчик: " + username + "\n"
    message += "Выбранный тур: "+ str(tours[tour[0]-1]) + "\n"
    message += "Дата поездки: "+ str(tour[1]) + "\n"
    message += "Выбранное время: "+ str(tour[2]) + "\n"
    message += "Количество взрослых: "+ str(tour[3]) + "\n"
    message += "Количество детей: "+ str(tour[4]) + "\n"
    message += "Нужно ли питание: "+ str(tour[5]) + "\n"
    message += "Нужен ли трансфер от и до аэропорта: "+ str(tour[6]) + "\n"
    message += "Нужно ли проживание: "+ str(tour[7]) + "\n"
    message += "Дней:" + str(tour[8]) +"\n"
    message += "Итоговая стоимость:" + str(tour[9]) +"\n"

    # Добавить подсчет итоговой суммы
    return message

token = ""
id = 1

import requests
def send_tg(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": id,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

# 1 шаг. в поиске находим бота BotFather
# 2 шаг. запускаем
# 3 - пишем команду /newbot
# 4 - выбираем любое имя для бота
# 5 - выбираем username , оно должно быть на англ, и заканчиваться на bot
# 6 - получите ссылку на бота и токен, токен копируйте и вставьте в код
# 7 - перейдите по ссылке в боте и запустите его (нажмите start)
# 8 - @userinfobot получите свой айди
# ID: 8558634705

def start():
    print("Добро пожаловать в приложение для бронирования туров по Северной Осетии.")
    sleep(2)
    registration()
    while True:
        dashboard()   

start()
