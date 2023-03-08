from flask import Flask , render_template

app =Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
@app.route('/cal/<num1>/<op>/<num2>')
def cal(num1, op, num2):
    n1= int(num1)
    n2= int(num2)
    if op=="+":
        result= n1+n2
    elif op== "-":
        result= n1-n2
    elif op == '/':
        result = n1 / n2
    elif op == '*':    
        result= n1*n2
    elif op == "%":
        result= n1%n2
   
    return '<h1>Result %s!</h1>' %str(result)

if __name__== '__main__':
    app.run(debug=True)