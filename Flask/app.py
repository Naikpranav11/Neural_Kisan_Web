from flask import Flask,render_template,request,url_for,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return(redirect(url_for("login")))

@app.route('/Login' , methods=["POST","GET"])
def login():
    Usernames=['Rhys','Sai','Pranav','Kapil','Ralph',]
    Passwords=['123','123','123','123']
    if request.method == "POST":   
        Username=request.form['Username']
        Password=request.form['Password']

        for i in range(len(Usernames)):
            if(Username == Usernames[i] and Password==Passwords[i]): 
                return(redirect(url_for("Dash",Username=Username)))
        else:
          return render_template("login.html")
    return render_template('login.html')


@app.route('/Admin=<Username>')
def Dash(Username):
    return render_template('Dashboard.html',Username=Username)
    
