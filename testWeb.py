import requests
import sqlite3
##r = requests.get('http://127.0.0.1:5000/email=mail0@mail.ru&phone=88005553530&date=2000-10-00&item=0')
##
##print(r.text)
RowsCheck = 0
con = sqlite3.connect('main.db')
sql = list(con.cursor().execute("SELECT * FROM Rows"))
for i in sql:
    string = 'http://127.0.0.1:5000/?email='+i[1]+'&phone='+i[2]+'&date='+i[3]+'&item='+i[4]
    if i[0] == requests.get(string).text:
        RowsCheck+=1
    else:
        print('Следющая строка запроса дала не правильный ответ:')
        print(string)
        
    
con.close()
if len(sql) == RowsCheck:
    print("Все строки из базы проверены и дали правильный ответ")
else:
    print('Строки запросов выше дали не правильный ответ')


