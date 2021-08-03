from flask import Flask,  request
import sqlite3
import re

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

def StringNone(item):
    if item == None:
        return 'none'
    else:
        return item
    
app = Flask(__name__)

@app.route('/')
def show_by_filtr():
    email = StringNone(request.args.get('email'))
    item = StringNone(request.args.get('item'))
    phone = StringNone(request.args.get('phone'))
    date = StringNone(request.args.get('date'))
    if CheckNumber(phone) and CheckDate(date):
    
        string_request = "SELECT * FROM Rows WHERE (email='"+email+"' or email='none') AND (phone='"+phone+"' or phone='none') AND (date='"+date+"' or date='none') AND (item='"+item+"' or item='none')"
        con = sqlite3.connect('main.db')
        return_string = list(con.cursor().execute(string_request)) 
        con.close()
        
        if len(return_string) > 0:return return_string[0][0]
        else:return "None"
        
    else:return "None"

if __name__ == '__main__':
    app.run(threaded=True)
