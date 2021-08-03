# Web
Web

Так как в задание не указано какой веб сервис использовать я выбрал Flask т.к. он проще и понятней и производительней и красивее чем Django)

файл sql.py создает тестовую базу
файл web.py запускает сервис
файл testWeb.py проверяет тестовую базу запрашивая от сервиса ее данные

Используется тестовая sqllite база из 5 колон:

    Name       email              phone           date            item

[["'Name0'", "'none'",          "'88005553530'", "'2000-10-00'" ,"'0'"],
 ["'Name1'", "'mail1@mail.ru'", "'88005553531'", "'2000-10-01'" ,"'1'"],
 ["'Name2'", "'mail2@mail.ru'", "'88005553532'", "'2000-10-02'" ,"'2'"],
 ["'Name3'", "'mail3@mail.ru'", "'88005553533'", "'2000-10-03'" ,"'none'"],
 ["'Name4'", "'mail4@mail.ru'", "'88005553534'", "'2000-10-04'" ,"'none'"],]

Если вы хотите проверить сервис через testWeb.py то нужно запустить web.py и testWeb.py в разных потоках т.е. в разных окнах.
По умолчанию сервис работает по запросу http://127.0.0.1:5000

Можно указать каждый из столбцов
Пример запроса : http://127.0.0.1:5000/?email=mail0@mail.ru&phone=88005553530&date=2000-10-00&item=0

Если какой то из столбцов должен отсуствовать его можно просто не указывать.
Пример запроса : http://127.0.0.1:5000/?phone=88005553530&date=2000-10-00&item=0

Так же если последний из столбцов не требуется его можно не указывать
Пример запроса : http://127.0.0.1:5000/?email=mail4@mail.ru&phone=88005553534&date=2000-10-04

Проводится проверка номера и даты функциями:

def CheckNumber(item):
    if item == 'none':
        return True
    regex = re.compile('[0-9]{11}', re.I)
    return bool(regex.match(str(item)))

def CheckDate(item):
    if item == 'none':
        return True
    regex = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}', re.I)
    return bool(regex.match(str(item)))
