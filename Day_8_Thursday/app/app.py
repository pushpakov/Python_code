from flask import *

class InvalidInputError(Exception):
    pass

app = Flask(__name__)
user = Flask(__name__)

@app.route('/table/<int:num>')
def table(num: int) -> str:
    try:
        if num < 1:
            raise InvalidInputError("Number must be positive")
        return render_template('table.html', n=num)
    except InvalidInputError as e:
        return f"Error: {str(e)}"
    
@user.route('/')  
def customer():  
   return render_template('user.html')  
  
@user.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("user_data.html",result = result)  


if __name__ == '__main__':
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.serving import run_simple

    dispatcher = DispatcherMiddleware(None, {
        '/app': app,
        '/user': user,
    })

    run_simple('localhost', 5000, dispatcher, use_reloader=True)
