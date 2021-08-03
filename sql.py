import sqlite3

con = sqlite3.connect('main.db')
cur = con.cursor()

cur.execute('''CREATE TABLE Rows
               (Name text, email text, phone text, date text, item text)''')

def list_to_string(row):
    string = "INSERT INTO Rows VALUES ("
    for i in row:
        string = string + i+", "
    return string[:-2]+")"



row = [["'Name0'", "'none'",          "'88005553530'", "'2000-10-00'" ,"'0'"],
       ["'Name1'", "'mail1@mail.ru'", "'88005553531'", "'2000-10-01'" ,"'1'"],
       ["'Name2'", "'mail2@mail.ru'", "'88005553532'", "'2000-10-02'" ,"'2'"],
       ["'Name3'", "'mail3@mail.ru'", "'88005553533'", "'2000-10-03'" ,"'none'"],
       ["'Name4'", "'mail4@mail.ru'", "'88005553534'", "'2000-10-04'" ,"'none'"],]


for i in row:
 
    cur.execute(list_to_string(i))
con.commit()
con.close()
