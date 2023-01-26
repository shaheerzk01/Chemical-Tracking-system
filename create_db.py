import sqlite3
def create_db():
    con=sqlite3.connect(database=r'CMS.db')
    cur=con.cursor()
    #======EMPLOYEE==============
    cur.execute('CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)')
    con.commit()
    
    #========SUPPLIER==========
    cur.execute('CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)')
    con.commit()
    
    #=========CATEGORY=======
    cur.execute('CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)')
    con.commit()  
    
    #========PRODUCT==========
    cur.execute('CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,Name text,price text,qty text, status text)')
    con.commit()
create_db()