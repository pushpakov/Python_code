from flask import *  
user = Flask(__name__)  
  
@app.route('/')  
def customer():  
   return render_template('user.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("user_data.html",result = result)  
   
if __name__ == '__main__':  
   user.run(debug = True) 



