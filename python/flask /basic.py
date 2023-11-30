#Basic config  flask application
from flask import Flask #WSGI SERVER APPLICATION

app = Flask(__name__)


@app.route('/') #HOME 0R MAIN URL U CAN ADD MORE URL PATH AS REQUIRED,http://127.0.0.1:5000
def hello():
    return 'Hello, World!'

@app.route('/products')#http://127.0.0.1:5000/products
def products():
    return "products page"

if  __name__ == '__main__':
    app.run(debug=True) #DEBUG TRUE FOR ANY CHANGES IN CODE AND SAVE IT AUTOMATICALLY REFLECT IN WEB APP 