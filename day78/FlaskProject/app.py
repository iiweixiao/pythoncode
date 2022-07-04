from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/add')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')

    username = request.form.get("user")
    password = request.form.get("pwd")
    mobile = request.form.get("mobile")
    print(username, password, mobile)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
