# variables in flask
# building dynamically url and redirect the url 
from flask  import Flask,redirect,url_for

app = Flask(__name__)
#basic url 
@app.route('/')# decorator routes
def index():
    return "hello world !"

# basic dynamically url 
@app.route('/marks/<int:page>')#pass the value with url parameter #http://127.0.0.1:5000/marks/50
def mark(page):
    return "your mark is " + str(page)#change string to avoid concatenation errors

# redirect the url dynamically 
# create a two dynamically url named in pass and fail
@app.route("/pass/<int:score>")
def pass_mark(score):
    return "Your passed in examination score is " + str(score)

@app.route("/fail/<int:score>")
def fail_mark(score):
    return "Your failed in examination score is " + str(score)
# check marks redirect the url to the correct one 
@app.route("/results/<int:marks>")
def results(marks):
    result = ""
    if marks <= 45:
        result = "fail_mark"
    else:
        result = "pass_mark"
    return redirect(url_for(result, score=marks))



if __name__ == '__main__':
    app.run(debug= True)