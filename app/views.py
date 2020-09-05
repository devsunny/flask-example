from app import app
from flask import render_template
from flask import render_template, request, session, redirect, url_for
from flask import flash


@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "All about Flask"

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        if not len(password) >= 10:
            flash("Password must be at least 10 characters", "warning")
            return redirect(request.url)

        flash("Account created!", "success")

        return redirect(request.url)

    return render_template("public/sign_up.html")

users = {
    "julian": {
        "username": "julian",
        "email": "julian@gmail.com",
        "password": "example",
        "bio": "Some guy from the internet"
    },
    "clarissa": {
        "username": "clarissa",
        "email": "clarissa@icloud.com",
        "password": "sweetpotato22",
        "bio": "Sweet potato is life"
    },
    "sunnyliu1971": {
        "username": "sunnyliu1971",
        "email": "sunnyliu1971@icloud.com",
        "password": "sweettomato22",
        "bio": "Sweet tomato is life"
    },
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creator of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():

    if request.method == "POST":

        req = request.form

        username = req.get("username")
        password = req.get("password")

        if not username in users:
            print("Username not found")
            return redirect(request.url)
        else:
            user = users[username]

        if not password == user["password"]:
            print("Incorrect password")
            return redirect(request.url)
        else:
            session["USERNAME"] = user["username"]
            print("session username set")
            return redirect(url_for("profile"))

    return render_template("public/login.html")

@app.route("/sign-out")
def sign_out():

    session.pop("USERNAME", None)

    return redirect(url_for("sign_in"))
    
    
@app.route("/upload-file", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            file = request.files["file"]

            print(file)

            return redirect(request.url)


    return render_template("public/upload_file.html")

  
@app.route("/profile")
def profile():
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user = users[username]
        return render_template("public/profile.html", user=user)
    else:
        print("No username found in session")
        return redirect(url_for("sign_in"))

    
@app.route("/jinja")
def jinja():
    # Strings
    my_name = "Julian"

    # Integers
    my_age = 30

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Tony": 43,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description 
            self.domain = domain

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty
        
    return render_template(
        "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
        friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, 
        my_remote=my_remote, repeat=repeat
    )