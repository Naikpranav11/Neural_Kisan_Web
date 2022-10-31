from flask import Flask,render_template,request,url_for,redirect
import string
import random
app = Flask(__name__)
GlobalHash='2e'
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Login' , methods=["POST","GET"])
def login():
    Usernames=['Rhys','Sai','Pranav','Kapil','Ralph']
    Passwords=['123','123','123','123']
    if request.method == "POST":   
        Username=request.form['Username']
        Password=request.form['Password']

        for i in range(len(Usernames)):
            if(Username == Usernames[i] and Password==Passwords[i]): 
                Hash= ''.join(random.choices(string.ascii_lowercase +string.digits, k=10))
                GlobalHash=Hash
                return(redirect(url_for("username",Hash=Hash)))
        else:
          return render_template("login.html")
    return render_template('login.html')


@app.route('/<Hash>')
def username(Hash):
    return render_template('admin.html')
    