from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql

app=Flask(__name__)

@app.route('/')
def home():
    conn=sql.connect("users.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from student")
    data=cur.fetchall()
    return render_template("home.html",datas=data)

@app.route("/add_user",methods=["POST","GET"])
def add_user():
    if request.method=="POST":
        Student_Name=request.form["Name"]
        Student_Age=request.form["Age"]
        Student_Gender=request.form["Gender"]
        Student_Language=request.form["Language"]
        Student_Preference=request.form["Preference"]
        conn=sql.connect("users.db")
        cur=conn.cursor()
        cur.execute("insert into student(NAME,AGE,GENDER,LANGUAGE,PREFERENCE) values(?,?,?,?,?)",
                    (Student_Name,Student_Age,Student_Gender,Student_Language,Student_Preference))
        conn.commit()
        return redirect(url_for("home"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:id>",methods=["POST","GET"])
def edit_user(id):
    if request.method=="POST":
        Student_Name=request.form["Name"]

        Student_Age=request.form["Age"]
        Student_Gender=request.form["Gender"]
        Student_Language=request.form["Language"]
        Student_Preference=request.form["Preference"]
        conn=sql.connect("users.db")
        cur=conn.cursor()
        cur.execute("update student set NAME=?, AGE=?,Gender=?, Language=?, Preference=? where ID=?", 
        (Student_Name,Student_Age,Student_Gender,Student_Language,Student_Preference,id))
        conn.commit()
        return redirect(url_for("home"))
    conn=sql.connect("users.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from student where ID=?",(id,))
    data= cur.fetchone()
    return render_template("edit_user.html",datas=data)

@app.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):
        conn=sql.connect("users.db")
        cur=conn.cursor()
        cur.execute("delete from student where ID=?",(id,))
        conn.commit()
        return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)