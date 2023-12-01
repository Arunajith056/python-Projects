#jinja 2 template engine
'''
{% ---  %} conditional statements
{{ expression}}
{# comments #}
'''
from flask  import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



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
        exp={'AVG':total,'total_score':total_score,}
    return render_template('jinja.html',result=exp)#conditional statements in html file

if __name__ == '__main__':
    app.run(debug=True)