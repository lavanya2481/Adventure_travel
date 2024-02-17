from flask import Flask,render_template,flash,session,request,redirect

import sqlite3

app=Flask(__name__)
app.secret_key="123"


sqlconnection =sqlite3.connect("travel.db")
sqlconnection.execute("create table if not exists users(id integer primary key,username text,password integer, email text)")
sqlconnection.close()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register',methods=["GET","POST"])
def register():
 if request.method =="POST":
        try:
            name=request.form['username']
            psswd=request.form['password']
            mail=request.form['email']
            sqlconnection=sqlite3.connect('travel.db')
            cur=sqlconnection.cursor()
            cur.execute("insert into users(username,password,email)values(?,?,?)",(name,psswd,mail))
            sqlconnection.commit()
            flash("Record added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:   
           return redirect('/login')
           sqlconnection.close()


 return render_template("register.html")

@app.route('/booking')
def booking():
    return render_template("booking.html")

@app.route('/log',methods =["GET","POST"])
def log():
    if request.method =="POST":
        name=request.form['username']
        psswd=request.form['password']
        sqlconnection= sqlite3.connect('travel.db')
        sqlconnection.row_factory=sqlite3.Row
        cur=sqlconnection.cursor()
        
        cur.execute("select * from users where username =? and password =?",(name,psswd))
        data=cur.fetchone()
        if (data):
          session['name']=data["username"] 
          session['mail']=data["email"] 
          flash("Welcome to Adventure Travel ","logged")
          return redirect("/")
        else:
            flash("Invalid Username and Password","danger")
            return redirect('/login')
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)



@app.route('/goa')
def goa():
    return render_template("goa.html")


@app.route('/ladakh')
def ladakh():
    return render_template("ladakh.html")


@app.route('/maldives')
def maldives():
    return render_template("maldives.html")


@app.route('/agra')
def agra():
    return render_template("agra.html")


@app.route('/munnar')
def munnar():
    return render_template("munnar.html")


@app.route('/ooty')
def ooty():
    return render_template("ooty.html")