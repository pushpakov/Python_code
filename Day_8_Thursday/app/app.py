# to print table for the number provied by the user in my url 

from flask import Flask, render_template

class InvalidInputError(Exception):
    pass

app = Flask(__name__)

@app.route('/table/<int:num>')
def table(num: int) -> str:
    try:
        if num < 1:
            raise InvalidInputError("Number must be positive")
        return render_template('table.html', n=num)
    except InvalidInputError as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
