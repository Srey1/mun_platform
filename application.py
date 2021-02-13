import os


from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
#from tempfile import mkdtemp
#from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

#from functions import login_required
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from datetime import timedelta
# Configure application
app = Flask(__name__)
#app.secret_key = os.urandom(24)
app.config['SECRET_KEY'] = "This_is_the_seeeecccccreeet_thingzmagingz"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
#login_manager.init_app(app)

app.permanent_session_lifetime = timedelta(days=1)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))



# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response




amt = 0

forr = 0
agains = 0
obstain = 0

counter = []
counter1 = []
counter2 = []

final_count = []
final_vote = []

countries = []

# For Hand Raising
number_track = 0
number_hand = []
country_hand = []
type_hand = []

#x = False



@app.route("/voting", methods=["GET", "POST"])
#@login_required
def voting():

    global amt
    global forr
    global agains
    global obstain
    global counter
    global counter1
    global counter2
    global final_count
    global final_vote
    global countries
    global number_track
    global number_hand
    global country_hand
    global type_hand


    options = ["In Favor", "Abstention", "Against"]


    if request.method == "GET":
        return render_template("voting.html", counter = counter, counter1 = counter1, counter2 = counter2, options = options)

    else:

        vote = request.form.get("vote")

        the_current_user = session["user_id"]

        acountry = User.query.filter_by(id=the_current_user).first()
        country = acountry.username


        print(country)
        print(acountry)



        #countries[country] = vote

        inside = False

        """

        for items in countries:
            for things in final_count:
                if things == items:
                    inside = True
                    break
            else:
                inside = False
                final_count.append(items)

        if inside == False:
            for items in countries.values():
                final_vote.append(items)
        """

        #print(countries)
        #print("!!!!!")
        #print(country)
        #print("!!!!!")


        for items in final_count:
            if str(items) == str(country):
                y = final_count.index(country)
                earlier_vote = final_vote[y]
                final_vote[y] = vote
                inside = True

        if inside == False:
            countries.append(country)
            final_count.append(country)
            final_vote.append(vote)

            if vote == "In Favor":
                counter.append("a")
            elif vote == "Abstention":
                counter1.append("a")
            elif vote == "Against":
                counter2.append("a")

        print(countries)
        print(final_vote)
        print(final_count)

        if inside == True:
            if earlier_vote == "In Favor":
                counter.pop()
            elif earlier_vote == "Abstention":
                counter1.pop()
            elif earlier_vote == "Against":
                counter2.pop()
            if vote == "In Favor":
                counter.append("a")
            elif vote == "Abstention":
                counter1.append("a")
            elif vote == "Against":
                counter2.append("a")






            #print(countries)

                #for items in countries.values():
                 #   final_vote.append(items)s



            #amt = len(final_vote)




        forr = len(counter)
        agains = len(counter2)
        obstain = len(counter1)

        amt = len(final_vote)

        return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)


@app.route("/", methods=["GET", "POST"])
def vot():


    if request.method == "GET":
        global amt
        global forr
        global agains
        global obstain
        global counter
        global counter1
        global counter2
        global final_count
        global final_vote
        global countries
        global number_track
        global number_hand
        global country_hand
        global type_hand
        print(country_hand)
        print(type_hand)
        print(final_count)
        print(final_vote)
        return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)




@app.route("/login", methods=["GET", "POST"])
def login():




    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "GET":
        #print(generate_password_hash("33hello45"))

        return render_template("login.html")


    # User reached route via POST (as by submitting a form via POST)
    else:


        #global country
        #country = request.form.get("username"):

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html")

        gg = request.form.get("username")

        aa = request.form.get("password")

        print(f"USERNAME IS {gg} and PASSWORD is {aa}")


        # Query database for username
        rows = User.query.filter_by(username=gg).first()
        if rows == None:
            print("Type SOMETHING")
            return render_template("login.html")
        print(rows.id)
        print(rows.username)
        print(rows.password)



        #print(rows)

        # Ensure username exists and password is correct
        #if len(rows) != 1:
         #   return redirect("/login")

        #if request.form.get("password") != rows[0]["password"]:
        #    return redirect("/login")
        # Ensure username exists and password is correct
        #y = check_password_hash(rows[0]["password"], request.form.get("password"))
        if (str(rows.password) == str(aa)):
            print("FOUND")
            session["user_id"] = rows.id
            print(session["user_id"])
            if rows.username == "Chair":
                return redirect("/c")
            else:
                return redirect("/")


        print("NOT FOUND")
        return render_template("login.html")




        #if rows != "shouldnotbethis" or not check_password_hash(rows[0]["password"], request.form.get("password")):
        #    return render_template("login.html")

        #if rows[0]["password"] != request.form.get("password")):
           # return apology("invalid", 403)

        # Remember which user has logged in



@app.route("/c", methods=["GET", "POST"])
#@login_required
def ccc():
    global amt
    global forr
    global agains
    global counter
    global counter1
    global counter2
    global final_count
    global final_vote
    global countries
    global number_track
    global number_hand
    global country_hand
    global type_hand


    return redirect("/")



@app.route("/chair", methods=["GET", "POST"])
#@login_required
def chair():
    if request.method == "POST":
        global amt
        global forr
        global agains
        global counter
        global counter1
        global counter2
        global final_count
        global final_vote
        global countries
        global number_track
        global number_hand
        global country_hand
        global type_hand
        counter = []
        counter1 = []
        counter2 = []
        final_count = []
        final_vote = []
        countries = []
        amt = 0
        forr = 0
        agains = 0
        obstain = 0
        return redirect("/c")


@app.route("/quickrefresh", methods=["GET", "POST"])
#@login_required
def refresh():
    global amt
    global forr
    global agains
    global counter
    global counter1
    global counter2
    global final_count
    global final_vote
    global countries
    global number_track
    global number_hand
    global country_hand
    global type_hand
    if request.method == "POST":
        return redirect("/c")

@app.route("/raise", methods=["GET", "POST"])
#@login_required
def raise_hand():
    global amt
    global forr
    global agains
    global counter
    global counter1
    global counter2
    global final_count
    global final_vote
    global countries
    global number_track
    global number_hand
    global country_hand
    global type_hand
    if request.method == "GET":
        return render_template("raise.html")
    elif request.method == "POST":
        isit = False
        reason = request.form.get("raise_type")
        tho_user = session["user_id"]
        before_country_raise = User.query.filter_by(id=tho_user).first()
        country_raise = before_country_raise.username


        for items in country_hand:
            if str(items) == str(country_raise):
                print("TRY 2 REPLICA FOUND")
                h = country_hand.index(country_raise)
                country_hand.pop(h)
                type_hand.pop(h)
                print(country_hand)
                print(type_hand)
                print(final_count)
                print(final_vote)
                return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)


        if isit == False:
            country_hand.append(country_raise)
            type_hand.append(reason)
            number_track = len(country_hand)

        print(country_hand)
        print(type_hand)
        print(final_count)
        print(final_vote)

        return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)


@app.route("/quickraise", methods=["GET", "POST"])
#@login_required
def quick_raise():
    global amt
    global forr
    global agains
    global counter
    global counter1
    global counter2
    global final_count
    global final_vote
    global countries
    global number_track
    global number_hand
    global country_hand
    global type_hand
    if request.method == "POST":
        #sure = False
        the_user = session["user_id"]
        before_country_raise = User.query.filter_by(id=the_user).first()
        current_count = before_country_raise.username

        for items in country_hand:
            if str(items) == str(current_count):
                r = country_hand.index(current_count)
                country_hand.pop(r)
                type_hand.pop(r)
                print("REPLICA FOUND")
                print(country_hand)
                print(type_hand)
                print(final_count)
                print(final_vote)
                return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)


        print("REPLICA NOT FOUND")
        print(country_hand)
        print(type_hand)
        print(final_count)
        print(final_vote)
        return render_template("raise.html")

@app.route("/alldown", methods=["GET", "POST"])
#@login_required
def quick_close():
    global amt
    global forr
    global agains
    global counter
    global counter1
    global counter2
    global final_count
    global final_vote
    global countries
    global number_track
    global number_hand
    global country_hand
    global type_hand
    if request.method == "POST":
        global type_hand
        global country_hand
        global number_track
        number_track = 0
        country_hand = []
        type_hand = []
        return redirect("/c")
