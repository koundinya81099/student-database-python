import sqlite3
#import project1_frontend

def studentData():
        con = sqlite3.connect("student.db")
        cur=con.cursor()
       
        cur.execute("CREATE TABLE IF NOT EXISTS student(id integer primary key ,StdID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
        con.commit()
        con.close()              
def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con = sqlite3.connect("student.db")
        cur=con.cursor()
        
        cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?)",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close() 
def viewData():
        con = sqlite3.connect("student.db")
        cur=con.cursor()
        
        cur.execute("select * from student")
        row=cur.fetchall()
        con.close()       
        return row
def deleteRec(id):
        con = sqlite3.connect("student.db")
        cur=con.cursor()
        
        cur.execute("DELETE FROM student WHERE id=?",(id,))
        con.commit()
        con.close()         
def searchData(StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
        con = sqlite3.connect("student.db")
        cur=con.cursor()
      
        cur.execute("SELECT * FROM student WHERE StdID=? or Firstname=? or Surname=? or DoB=? or Age=?or Gender=? or Address=? or Mobile=?",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        rows=cur.fetchall()
        con.close()        
        return rows
def dataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
        con = sqlite3.connect("student.db")
        cur=con.cursor()
        
        cur.execute("UPDATE student SET StdID=?,Firstname=?,Surname=?,DoB=?,Age=?,Gender=?,Address=?,Mobile=? WHERE id=?",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile,id))
        con.commit()
        con.close()    
