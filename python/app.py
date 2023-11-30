from flask import Flask
app =Flask(__name__)

@app.route('/')
def index():
    msg ='hello welcome all'
    return msg

if __name__ == '__main__':
    app.run(debug=True)

print(__name__)