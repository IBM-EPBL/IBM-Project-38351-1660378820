from flask import Flask,render_template

app = Flask(__name__)



@app.route("/")
def base():
    return render_template('base.html')

@app.route("/about")
def about():
    return render_template('about.html')

   
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')


@app.route("/profiles/<username>")

@app.route("/index")
def index():
    return render_template('index.html')