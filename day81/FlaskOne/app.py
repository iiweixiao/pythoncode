from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add/user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    name = request.form.get('name')
    password = request.form.get('passwd')
    mobile = request.form.get('mobile')
    print(name, password, mobile)
    return redirect('/')


if __name__ == '__main__':
    app.run()
