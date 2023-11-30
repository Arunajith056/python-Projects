# integrate the Html  with flask 
#http verb get and post methods
#import render_template from flask and create templates folder main directory place the html file inside the templates folder
from flask import Flask,render_template,request

app= Flask(__name__)

#basic html template rendering
@app.route('/')
def home():
    return render_template('index.html')

#dynamic template rendering
#get the post value from html page in form 
def score(total):
    if total <= 35:
        msg ="your average score is "+ str(total) + " and u failed"
        return msg
    else: 
        msg ="your average score is "+ str(total) + " and u passed"
        return msg

@app.route('/submit', methods=['POST' , 'GET'])
def submit():
    total_score = 0
    if request.method == 'GET':# change it to POST try 
        tamil = float(request.args.get('tamil')) #request.form['tamil'] for "post"
        english = float(request.args.get('english'))#request.args.get('english') for "get"
        maths = float(request.args.get('maths'))
        chemistry = float(request.args.get('chemistry'))
        physics = float(request.args.get('physics'))
        total_score = (tamil + english + physics + maths + chemistry)
        total = total_score / 5
    return render_template('results.html',total=score(total),total_score=total_score)


if  __name__ == '__main__':
    app.run(debug=True)

#