from flask import Flask,render_template, render_template, redirect, request
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    date=datetime.now()
    date_time = date.strftime("%m/%d/%Y, %H:%M")
    Strawberry = request.form['strawberry']
    Raspberry = request.form['raspberry']
    Apple=request.form['apple']
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    id=request.form['student_id']

    return render_template("checkout.html",Strawberry=Strawberry,Raspberry=Raspberry,
                           Apple=Apple,first_name=first_name,last_name=last_name,id=id,date=date_time,)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    