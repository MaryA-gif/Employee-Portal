## DATABASE
import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor , conn
    try:
        conn = pymysql.connect(host="localhost", user='root', passwd='',database='emply_data',cursorclass=pymysql.cursors.DictCursor)
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Something is wrong')
        return
        
    mycursor.execute('USE emply_data')  
    mycursor.execute('CREATE TABLE IF NOT EXISTS Edata(Id VARCHAR(10), Name VARCHAR(50), Phone VARCHAR(15), Role Varchar(50),Gender VARCHAR(10),Experenice INT)')

def id_exist(id):
    mycursor.execute('SELECT COUNT(*) FROM Edata WHERE Id=%s',id)
    result = mycursor.fetchone()
    return result['COUNT(*)'] > 0

def fetch_employees():
    mycursor.execute('SELECT * FROM Edata')
    result=mycursor.fetchall()
    return result
def insert (id,name,phone,role,gen,exp):
    mycursor.execute('INSERT INTO Edata VALUES (%s,%s,%s,%s,%s,%s)', (id,name,phone,role,gen,exp))
    conn.commit()

def update(id,new_name,new_phone,new_role,new_gen,new_exp):
    mycursor.execute('UPDATE Edata SET name=%s,phone=%s,role=%s,gender=%s,experenice=%s WHERE id=%s',(new_name,new_phone,new_role,new_gen,new_exp,id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM Edata WHERE id=%s',id)
    conn.commit()

def search(option,value):
    mycursor.execute(f'SELECT * FROM Edata WHERE {option}=%s',value)
    result = mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE Edata')
    conn.commit()


connect_database()