from flask import Flask, render_template, request
import sqlite3 as sql



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/addemploye' , methods=['GET'])
def add_employee():
    return render_template('add_employe.html')

@app.route('/addrec' , methods=['POST','GET'])
def addrec():
    if request.method=='POST':
        try:
            nm = request.form['nm']
            password=request.form['pass']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
         
            with sql.connect("emp_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO employes (name,password,addr,city,pin)VALUES (?,?,?,?,?)",(nm,password,addr,city,pin) )
                
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            return render_template("result.html",msg = msg)
            con.close()



@app.route('/delemploye',methods=['POST','GET'])
def delete_records():
    return render_template("del_records.html")

@app.route('/delete',methods=['POST','GET'])
def delete():
    if request.method=='POST':
        try:
            nm = request.form['nm']
            with sql.connect("emp_database.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM employes WHERE name=?", (nm,))
                con.commit()
                
                msg = "Record successfully deleted"

        except:
            con.rollback()
            msg = "error in deletion operation"
        finally:
            con.close()
            return render_template("result.html",msg = msg)
            

@app.route('/upemploye',methods=['POST','GET'])
def update_records():
    return render_template("upd_employe.html")

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method=='POST':
        nm = request.form['nm']
        password=request.form['pass']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        with sql.connect("emp_database.db") as con:
            cur = con.cursor()
            cur.execute('SELECT name FROM employes')
            names=cur.fetchall()
            nms=[]
            for i in names:
                nms.append(i[0])
                
            if nm in nms:
                cur.execute('''UPDATE employes SET password=? , addr=? , city=? , pin=?  WHERE name = ?''', (password,addr,city,pin,nm))
                con.commit()
                msg = "Record successfully Updated"
                
                return render_template("result.html",msg = msg)
            
            else:
                msg = "User Doesn't Exist"
                
                return render_template("result.html",msg = msg) 
            
@app.route('/login',methods=['POST','GET'])
def login():
    return render_template("login.html")            


@app.route('/logindetails',methods=['POST','GET'])
def logindetails():
    
    if request.method=='POST':
        name=request.form['nm']
        password=request.form['pass']
        con = sql.connect("emp_database.db")
        cur = con.cursor()
        cur.execute('SELECT name FROM employes')
        names=cur.fetchall()
        nms=[]
        cur.execute('SELECT password FROM employes WHERE name=?',(name,))
        for i in names:
            nms.append(i[0])
        if name in nms :
            cur = con.cursor()
            cur.execute('SELECT password FROM employes WHERE name=?',(name,))
            pass_word=cur.fetchall()
            if pass_word==password:
                cur = con.cursor()
                cur.execute("SELECT * FROM employes WHERE name=?",(name,))
                rows=cur.fetchall()
                return render_template("login_details.html",rows = rows)
            else:
                msg = "Incorrevt Password"
                return render_template("result.html",msg = msg)
        else:
            msg = "User Doesn't Exist"
            return render_template("result.html",msg = msg) 
            
@app.route('/addelectronic' , methods=['GET'])
def add_electronic():
    return render_template('add_electronic.html')

@app.route('/addelec' , methods=['POST','GET'])
def addelec():
    if request.method=='POST':
        try:
            nm = request.form['nm']
            item_id = request.form['id']
            quantity = request.form['quan']
         
            with sql.connect("stk_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO stocks (id,item,quantity)VALUES (?,?,?)",(item_id,nm,quantity) )
                
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            return render_template("result.html",msg = msg)
            con.close()

            
@app.route('/upstock',methods=['POST','GET'])
def update_electronic_records():
    return render_template("upd_electronic.html")

@app.route('/update_ele',methods=['POST','GET'])
def update_ele():
    if request.method=='POST':
        nm = request.form['nm']
        item_id = request.form['id']
        quantity = request.form['quan']
        with sql.connect("stk_database.db") as con:
            cur = con.cursor()
            cur.execute('SELECT item FROM stocks')
            names=cur.fetchall()
            nms=[]
            for i in names:
                nms.append(i[0])
                
            if nm in nms:
                cur.execute('''UPDATE stocks SET id=? , quantity=? WHERE item = ?''', (item_id,quantity,nm))
                con.commit()
                msg = "Record successfully Updated"
                
                return render_template("result.html",msg = msg)
            
            else:
                msg = "Item Doesn't Exist"
                
                return render_template("result.html",msg = msg) 

@app.route('/stock')
def stock():
   con = sql.connect("stk_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from stocks")
   
   rows = cur.fetchall()
   return render_template("stock.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
    

