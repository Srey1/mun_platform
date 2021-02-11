import os


from flask import Flask, flash, jsonify, redirect, render_template, request, session
#from flask_session import Session
#from tempfile import mkdtemp
#from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from functions import login_required
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))

    def __init__(self, name):
        self.username = username
        self.password = password

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#FOR VOTE HTML


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

@app.route("/voting", methods=["GET", "POST"])
@login_required

def voting():

    global counter
    global counter1
    global counter2


    options = ["In Favor", "Abstention", "Against"]


    if request.method == "GET":
        return render_template("voting.html", counter = counter, counter1 = counter1, counter2 = counter2, options = options)

    else:

        vote = request.form.get("vote")

        first_country = User.query.filter_by(id=session["user_id"]).first()
        country = first_country.username

        global countries

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

        for items in countries:
            if str(items) == str(country):
                x = countries.index(country)
                earlier_vote = final_vote[x]
                final_vote[x] = vote
                inside = True

        if inside == False:
            countries.append(country)

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




        if inside == False:
            final_count.append(country)
            final_vote.append(vote)

            #print(countries)

                #for items in countries.values():
                 #   final_vote.append(items)s

            global amt
            global forr
            global agains
            global obstain
            global type_hand
            global country_hand
            global number_track

            amt = len(final_vote)


            if vote == "In Favor":
                counter.append("a")
            elif vote == "Abstention":
                counter1.append("a")
            elif vote == "Against":
                counter2.append("a")

        forr = len(counter)
        agains = len(counter2)
        obstain = len(counter1)

        return redirect("/")
@app.route("/", methods=["GET", "POST"])
@login_required
def vot():

    global forr
    global agains
    global obstain
    global type_hand
    global country_hand
    global number_track
    before_country_raise = User.query.filter_by(id=session["user_id"]).first()
    current_country = before_country_raise.username

    if request.method == "GET":
        if current_country == "Chair":
            return render_template("chair.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)
        else:
            return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)




@app.route("/login", methods=["GET", "POST"])
def login():




    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "GET":
        person0 = User(username = 'Afghanistan', password = generate_password_hash('33Afghanistan45'))
        db.session.add(person0)
        db.session.commit()
        person1 = User(username = 'Albania', password = generate_password_hash('33Albania45'))
        db.session.add(person1)
        db.session.commit()
        person2 = User(username = 'Algeria', password = generate_password_hash('33Algeria45'))
        db.session.add(person2)
        db.session.commit()
        person3 = User(username = 'American-Samoa', password = generate_password_hash('33American-Samoa45'))
        db.session.add(person3)
        db.session.commit()
        person4 = User(username = 'Andorra', password = generate_password_hash('33Andorra45'))
        db.session.add(person4)
        db.session.commit()
        person5 = User(username = 'Angola', password = generate_password_hash('33Angola45'))
        db.session.add(person5)
        db.session.commit()
        person6 = User(username = 'Anguilla', password = generate_password_hash('33Anguilla45'))
        db.session.add(person6)
        db.session.commit()
        person7 = User(username = 'Antarctica', password = generate_password_hash('33Antarctica45'))
        db.session.add(person7)
        db.session.commit()
        person8 = User(username = 'Antigua-and-Barbuda', password = generate_password_hash('33Antigua-and-Barbuda45'))
        db.session.add(person8)
        db.session.commit()
        person9 = User(username = 'Argentina', password = generate_password_hash('33Argentina45'))
        db.session.add(person9)
        db.session.commit()
        person10 = User(username = 'Armenia', password = generate_password_hash('33Armenia45'))
        db.session.add(person10)
        db.session.commit()
        person11 = User(username = 'Aruba', password = generate_password_hash('33Aruba45'))
        db.session.add(person11)
        db.session.commit()
        person12 = User(username = 'Australia', password = generate_password_hash('33Australia45'))
        db.session.add(person12)
        db.session.commit()
        person13 = User(username = 'Austria', password = generate_password_hash('33Austria45'))
        db.session.add(person13)
        db.session.commit()
        person14 = User(username = 'Azerbaijan', password = generate_password_hash('33Azerbaijan45'))
        db.session.add(person14)
        db.session.commit()
        person15 = User(username = 'Bahamas', password = generate_password_hash('33Bahamas45'))
        db.session.add(person15)
        db.session.commit()
        person16 = User(username = 'Bahrain', password = generate_password_hash('33Bahrain45'))
        db.session.add(person16)
        db.session.commit()
        person17 = User(username = 'Bangladesh', password = generate_password_hash('33Bangladesh45'))
        db.session.add(person17)
        db.session.commit()
        person18 = User(username = 'Barbados', password = generate_password_hash('33Barbados45'))
        db.session.add(person18)
        db.session.commit()
        person19 = User(username = 'Belarus', password = generate_password_hash('33Belarus45'))
        db.session.add(person19)
        db.session.commit()
        person20 = User(username = 'Belgium', password = generate_password_hash('33Belgium45'))
        db.session.add(person20)
        db.session.commit()
        person21 = User(username = 'Belize', password = generate_password_hash('33Belize45'))
        db.session.add(person21)
        db.session.commit()
        person22 = User(username = 'Benin', password = generate_password_hash('33Benin45'))
        db.session.add(person22)
        db.session.commit()
        person23 = User(username = 'Bermuda', password = generate_password_hash('33Bermuda45'))
        db.session.add(person23)
        db.session.commit()
        person24 = User(username = 'Bhutan', password = generate_password_hash('33Bhutan45'))
        db.session.add(person24)
        db.session.commit()
        person25 = User(username = 'Bolivia', password = generate_password_hash('33Bolivia45'))
        db.session.add(person25)
        db.session.commit()
        person26 = User(username = 'Bosnia-and-Herzegovina', password = generate_password_hash('33Bosnia-and-Herzegovina45'))
        db.session.add(person26)
        db.session.commit()
        person27 = User(username = 'Botswana', password = generate_password_hash('33Botswana45'))
        db.session.add(person27)
        db.session.commit()
        person28 = User(username = 'Bouvet-Island', password = generate_password_hash('33Bouvet-Island45'))
        db.session.add(person28)
        db.session.commit()
        person29 = User(username = 'Brazil', password = generate_password_hash('33Brazil45'))
        db.session.add(person29)
        db.session.commit()
        person30 = User(username = 'Bulgaria', password = generate_password_hash('33Bulgaria45'))
        db.session.add(person30)
        db.session.commit()
        person31 = User(username = 'Burkina-Faso', password = generate_password_hash('33Burkina-Faso45'))
        db.session.add(person31)
        db.session.commit()
        person32 = User(username = 'Burundi', password = generate_password_hash('33Burundi45'))
        db.session.add(person32)
        db.session.commit()
        person33 = User(username = 'Cambodia', password = generate_password_hash('33Cambodia45'))
        db.session.add(person33)
        db.session.commit()
        person34 = User(username = 'Cameroon', password = generate_password_hash('33Cameroon45'))
        db.session.add(person34)
        db.session.commit()
        person35 = User(username = 'Canada', password = generate_password_hash('33Canada45'))
        db.session.add(person35)
        db.session.commit()
        person36 = User(username = 'Cape-Verde', password = generate_password_hash('33Cape-Verde45'))
        db.session.add(person36)
        db.session.commit()
        person37 = User(username = 'Cayman-Islands', password = generate_password_hash('33Cayman-Islands45'))
        db.session.add(person37)
        db.session.commit()
        person38 = User(username = 'Central-African-Republic', password = generate_password_hash('33Central-African-Republic45'))
        db.session.add(person38)
        db.session.commit()
        person39 = User(username = 'Chad', password = generate_password_hash('33Chad45'))
        db.session.add(person39)
        db.session.commit()
        person40 = User(username = 'Chile', password = generate_password_hash('33Chile45'))
        db.session.add(person40)
        db.session.commit()
        person41 = User(username = 'China', password = generate_password_hash('33China45'))
        db.session.add(person41)
        db.session.commit()
        person42 = User(username = 'Christmas-Island', password = generate_password_hash('33Christmas-Island45'))
        db.session.add(person42)
        db.session.commit()
        person43 = User(username = 'Cocos', password = generate_password_hash('33Cocos45'))
        db.session.add(person43)
        db.session.commit()
        person44 = User(username = 'Colombia', password = generate_password_hash('33Colombia45'))
        db.session.add(person44)
        db.session.commit()
        person45 = User(username = 'Comoros', password = generate_password_hash('33Comoros45'))
        db.session.add(person45)
        db.session.commit()
        person46 = User(username = 'Congo', password = generate_password_hash('33Congo45'))
        db.session.add(person46)
        db.session.commit()
        person47 = User(username = 'Cook-Islands', password = generate_password_hash('33Cook-Islands45'))
        db.session.add(person47)
        db.session.commit()
        person48 = User(username = 'Costa-Rica', password = generate_password_hash('33Costa-Rica45'))
        db.session.add(person48)
        db.session.commit()
        person49 = User(username = 'Ivory-Coast', password = generate_password_hash('33Ivory-Coast45'))
        db.session.add(person49)
        db.session.commit()
        person50 = User(username = 'Croatia', password = generate_password_hash('33Croatia45'))
        db.session.add(person50)
        db.session.commit()
        person51 = User(username = 'Cuba', password = generate_password_hash('33Cuba45'))
        db.session.add(person51)
        db.session.commit()
        person52 = User(username = 'Cyprus', password = generate_password_hash('33Cyprus45'))
        db.session.add(person52)
        db.session.commit()
        person53 = User(username = 'Czech-Republic', password = generate_password_hash('33Czech-Republic45'))
        db.session.add(person53)
        db.session.commit()
        person54 = User(username = 'Denmark', password = generate_password_hash('33Denmark45'))
        db.session.add(person54)
        db.session.commit()
        person55 = User(username = 'Djibouti', password = generate_password_hash('33Djibouti45'))
        db.session.add(person55)
        db.session.commit()
        person56 = User(username = 'Dominica', password = generate_password_hash('33Dominica45'))
        db.session.add(person56)
        db.session.commit()
        person57 = User(username = 'Dominican-Republic', password = generate_password_hash('33Dominican-Republic45'))
        db.session.add(person57)
        db.session.commit()
        person58 = User(username = 'East-Timor', password = generate_password_hash('33East-Timor45'))
        db.session.add(person58)
        db.session.commit()
        person59 = User(username = 'Ecuador', password = generate_password_hash('33Ecuador45'))
        db.session.add(person59)
        db.session.commit()
        person60 = User(username = 'Egypt', password = generate_password_hash('33Egypt45'))
        db.session.add(person60)
        db.session.commit()
        person61 = User(username = 'El-Salvador', password = generate_password_hash('33El-Salvador45'))
        db.session.add(person61)
        db.session.commit()
        person62 = User(username = 'Equatorial-Guinea', password = generate_password_hash('33Equatorial-Guinea45'))
        db.session.add(person62)
        db.session.commit()
        person63 = User(username = 'Eritrea', password = generate_password_hash('33Eritrea45'))
        db.session.add(person63)
        db.session.commit()
        person64 = User(username = 'Estonia', password = generate_password_hash('33Estonia45'))
        db.session.add(person64)
        db.session.commit()
        person65 = User(username = 'Ethiopia', password = generate_password_hash('33Ethiopia45'))
        db.session.add(person65)
        db.session.commit()
        person66 = User(username = 'Falkland-Islands', password = generate_password_hash('33Falkland-Islands45'))
        db.session.add(person66)
        db.session.commit()
        person67 = User(username = 'Faroe-Islands', password = generate_password_hash('33Faroe-Islands45'))
        db.session.add(person67)
        db.session.commit()
        person68 = User(username = 'Fiji', password = generate_password_hash('33Fiji45'))
        db.session.add(person68)
        db.session.commit()
        person69 = User(username = 'Finland', password = generate_password_hash('33Finland45'))
        db.session.add(person69)
        db.session.commit()
        person70 = User(username = 'France', password = generate_password_hash('33France45'))
        db.session.add(person70)
        db.session.commit()
        person71 = User(username = 'Metropolitan', password = generate_password_hash('33Metropolitan45'))
        db.session.add(person71)
        db.session.commit()
        person72 = User(username = 'French-Guiana', password = generate_password_hash('33French-Guiana45'))
        db.session.add(person72)
        db.session.commit()
        person73 = User(username = 'French-Polynesia', password = generate_password_hash('33French-Polynesia45'))
        db.session.add(person73)
        db.session.commit()
        person74 = User(username = 'Gabon', password = generate_password_hash('33Gabon45'))
        db.session.add(person74)
        db.session.commit()
        person75 = User(username = 'Gambia', password = generate_password_hash('33Gambia45'))
        db.session.add(person75)
        db.session.commit()
        person76 = User(username = 'Georgia', password = generate_password_hash('33Georgia45'))
        db.session.add(person76)
        db.session.commit()
        person77 = User(username = 'Germany', password = generate_password_hash('33Germany45'))
        db.session.add(person77)
        db.session.commit()
        person78 = User(username = 'Ghana', password = generate_password_hash('33Ghana45'))
        db.session.add(person78)
        db.session.commit()
        person79 = User(username = 'Gibraltar', password = generate_password_hash('33Gibraltar45'))
        db.session.add(person79)
        db.session.commit()
        person80 = User(username = 'Greece', password = generate_password_hash('33Greece45'))
        db.session.add(person80)
        db.session.commit()
        person81 = User(username = 'Greenland', password = generate_password_hash('33Greenland45'))
        db.session.add(person81)
        db.session.commit()
        person82 = User(username = 'Grenada', password = generate_password_hash('33Grenada45'))
        db.session.add(person82)
        db.session.commit()
        person83 = User(username = 'Guadeloupe', password = generate_password_hash('33Guadeloupe45'))
        db.session.add(person83)
        db.session.commit()
        person84 = User(username = 'Guam', password = generate_password_hash('33Guam45'))
        db.session.add(person84)
        db.session.commit()
        person85 = User(username = 'Guatemala', password = generate_password_hash('33Guatemala45'))
        db.session.add(person85)
        db.session.commit()
        person86 = User(username = 'Guinea', password = generate_password_hash('33Guinea45'))
        db.session.add(person86)
        db.session.commit()
        person87 = User(username = 'Guinea-Bissau', password = generate_password_hash('33Guinea-Bissau45'))
        db.session.add(person87)
        db.session.commit()
        person88 = User(username = 'Guyana', password = generate_password_hash('33Guyana45'))
        db.session.add(person88)
        db.session.commit()
        person89 = User(username = 'Haiti', password = generate_password_hash('33Haiti45'))
        db.session.add(person89)
        db.session.commit()
        person90 = User(username = 'Honduras', password = generate_password_hash('33Honduras45'))
        db.session.add(person90)
        db.session.commit()
        person91 = User(username = 'Hong-Kong', password = generate_password_hash('33Hong-Kong45'))
        db.session.add(person91)
        db.session.commit()
        person92 = User(username = 'Hungary', password = generate_password_hash('33Hungary45'))
        db.session.add(person92)
        db.session.commit()
        person93 = User(username = 'Iceland', password = generate_password_hash('33Iceland45'))
        db.session.add(person93)
        db.session.commit()
        person94 = User(username = 'India', password = generate_password_hash('33India45'))
        db.session.add(person94)
        db.session.commit()
        person95 = User(username = 'Indonesia', password = generate_password_hash('33Indonesia45'))
        db.session.add(person95)
        db.session.commit()
        person96 = User(username = 'Iran', password = generate_password_hash('33Iran45'))
        db.session.add(person96)
        db.session.commit()
        person97 = User(username = 'Iraq', password = generate_password_hash('33Iraq45'))
        db.session.add(person97)
        db.session.commit()
        person98 = User(username = 'Ireland', password = generate_password_hash('33Ireland45'))
        db.session.add(person98)
        db.session.commit()
        person99 = User(username = 'Israel', password = generate_password_hash('33Israel45'))
        db.session.add(person99)
        db.session.commit()
        person100 = User(username = 'Italy', password = generate_password_hash('33Italy45'))
        db.session.add(person100)
        db.session.commit()
        person101 = User(username = 'Jamaica', password = generate_password_hash('33Jamaica45'))
        db.session.add(person101)
        db.session.commit()
        person102 = User(username = 'Japan', password = generate_password_hash('33Japan45'))
        db.session.add(person102)
        db.session.commit()
        person103 = User(username = 'Jordan', password = generate_password_hash('33Jordan45'))
        db.session.add(person103)
        db.session.commit()
        person104 = User(username = 'Kazakhstan', password = generate_password_hash('33Kazakhstan45'))
        db.session.add(person104)
        db.session.commit()
        person105 = User(username = 'Kenya', password = generate_password_hash('33Kenya45'))
        db.session.add(person105)
        db.session.commit()
        person106 = User(username = 'Kiribati', password = generate_password_hash('33Kiribati45'))
        db.session.add(person106)
        db.session.commit()
        person107 = User(username = 'DPRK', password = generate_password_hash('33DPRK45'))
        db.session.add(person107)
        db.session.commit()
        person108 = User(username = 'South-Korea', password = generate_password_hash('33South-Korea45'))
        db.session.add(person108)
        db.session.commit()
        person109 = User(username = 'North-Korea', password = generate_password_hash('33North-Korea45'))
        db.session.add(person109)
        db.session.commit()
        person110 = User(username = 'Kuwait', password = generate_password_hash('33Kuwait45'))
        db.session.add(person110)
        db.session.commit()
        person111 = User(username = 'Kyrgyzstan', password = generate_password_hash('33Kyrgyzstan45'))
        db.session.add(person111)
        db.session.commit()
        person112 = User(username = 'Laos', password = generate_password_hash('33Laos45'))
        db.session.add(person112)
        db.session.commit()
        person113 = User(username = 'Latvia', password = generate_password_hash('33Latvia45'))
        db.session.add(person113)
        db.session.commit()
        person114 = User(username = 'Lebanon', password = generate_password_hash('33Lebanon45'))
        db.session.add(person114)
        db.session.commit()
        person115 = User(username = 'Lesotho', password = generate_password_hash('33Lesotho45'))
        db.session.add(person115)
        db.session.commit()
        person116 = User(username = 'Liberia', password = generate_password_hash('33Liberia45'))
        db.session.add(person116)
        db.session.commit()
        person117 = User(username = 'Libya', password = generate_password_hash('33Libya45'))
        db.session.add(person117)
        db.session.commit()
        person118 = User(username = 'Liechtenstein', password = generate_password_hash('33Liechtenstein45'))
        db.session.add(person118)
        db.session.commit()
        person119 = User(username = 'Lithuania', password = generate_password_hash('33Lithuania45'))
        db.session.add(person119)
        db.session.commit()
        person120 = User(username = 'Luxembourg', password = generate_password_hash('33Luxembourg45'))
        db.session.add(person120)
        db.session.commit()
        person121 = User(username = 'Macau', password = generate_password_hash('33Macau45'))
        db.session.add(person121)
        db.session.commit()
        person122 = User(username = 'Macedonia', password = generate_password_hash('33Macedonia45'))
        db.session.add(person122)
        db.session.commit()
        person123 = User(username = 'Madagascar', password = generate_password_hash('33Madagascar45'))
        db.session.add(person123)
        db.session.commit()
        person124 = User(username = 'Malawi', password = generate_password_hash('33Malawi45'))
        db.session.add(person124)
        db.session.commit()
        person125 = User(username = 'Malaysia', password = generate_password_hash('33Malaysia45'))
        db.session.add(person125)
        db.session.commit()
        person126 = User(username = 'Maldives', password = generate_password_hash('33Maldives45'))
        db.session.add(person126)
        db.session.commit()
        person127 = User(username = 'Mali', password = generate_password_hash('33Mali45'))
        db.session.add(person127)
        db.session.commit()
        person128 = User(username = 'Malta', password = generate_password_hash('33Malta45'))
        db.session.add(person128)
        db.session.commit()
        person129 = User(username = 'Marshall-Islands', password = generate_password_hash('33Marshall-Islands45'))
        db.session.add(person129)
        db.session.commit()
        person130 = User(username = 'Martinique', password = generate_password_hash('33Martinique45'))
        db.session.add(person130)
        db.session.commit()
        person131 = User(username = 'Mauritania', password = generate_password_hash('33Mauritania45'))
        db.session.add(person131)
        db.session.commit()
        person132 = User(username = 'Mauritius', password = generate_password_hash('33Mauritius45'))
        db.session.add(person132)
        db.session.commit()
        person133 = User(username = 'Mayotte', password = generate_password_hash('33Mayotte45'))
        db.session.add(person133)
        db.session.commit()
        person134 = User(username = 'Mexico', password = generate_password_hash('33Mexico45'))
        db.session.add(person134)
        db.session.commit()
        person135 = User(username = 'Micronesia', password = generate_password_hash('33Micronesia45'))
        db.session.add(person135)
        db.session.commit()
        person136 = User(username = 'Moldova', password = generate_password_hash('33Moldova45'))
        db.session.add(person136)
        db.session.commit()
        person137 = User(username = 'Monaco', password = generate_password_hash('33Monaco45'))
        db.session.add(person137)
        db.session.commit()
        person138 = User(username = 'Mongolia', password = generate_password_hash('33Mongolia45'))
        db.session.add(person138)
        db.session.commit()
        person139 = User(username = 'Montserrat', password = generate_password_hash('33Montserrat45'))
        db.session.add(person139)
        db.session.commit()
        person140 = User(username = 'Morocco', password = generate_password_hash('33Morocco45'))
        db.session.add(person140)
        db.session.commit()
        person141 = User(username = 'Mozambique', password = generate_password_hash('33Mozambique45'))
        db.session.add(person141)
        db.session.commit()
        person142 = User(username = 'Myanmar', password = generate_password_hash('33Myanmar45'))
        db.session.add(person142)
        db.session.commit()
        person143 = User(username = 'Namibia', password = generate_password_hash('33Namibia45'))
        db.session.add(person143)
        db.session.commit()
        person144 = User(username = 'Nauru', password = generate_password_hash('33Nauru45'))
        db.session.add(person144)
        db.session.commit()
        person145 = User(username = 'Nepal', password = generate_password_hash('33Nepal45'))
        db.session.add(person145)
        db.session.commit()
        person146 = User(username = 'Netherlands', password = generate_password_hash('33Netherlands45'))
        db.session.add(person146)
        db.session.commit()
        person147 = User(username = 'Netherlands-Antilles', password = generate_password_hash('33Netherlands-Antilles45'))
        db.session.add(person147)
        db.session.commit()
        person148 = User(username = 'New-Caledonia', password = generate_password_hash('33New-Caledonia45'))
        db.session.add(person148)
        db.session.commit()
        person149 = User(username = 'New-Zealand', password = generate_password_hash('33New-Zealand45'))
        db.session.add(person149)
        db.session.commit()
        person150 = User(username = 'Nicaragua', password = generate_password_hash('33Nicaragua45'))
        db.session.add(person150)
        db.session.commit()
        person151 = User(username = 'Niger', password = generate_password_hash('33Niger45'))
        db.session.add(person151)
        db.session.commit()
        person152 = User(username = 'Nigeria', password = generate_password_hash('33Nigeria45'))
        db.session.add(person152)
        db.session.commit()
        person153 = User(username = 'Niue', password = generate_password_hash('33Niue45'))
        db.session.add(person153)
        db.session.commit()
        person154 = User(username = 'Norfolk-Island', password = generate_password_hash('33Norfolk-Island45'))
        db.session.add(person154)
        db.session.commit()
        person155 = User(username = 'Northern-Mariana-Islands', password = generate_password_hash('33Northern-Mariana-Islands45'))
        db.session.add(person155)
        db.session.commit()
        person156 = User(username = 'Norway', password = generate_password_hash('33Norway45'))
        db.session.add(person156)
        db.session.commit()
        person157 = User(username = 'Oman', password = generate_password_hash('33Oman45'))
        db.session.add(person157)
        db.session.commit()
        person158 = User(username = 'Pakistan', password = generate_password_hash('33Pakistan45'))
        db.session.add(person158)
        db.session.commit()
        person159 = User(username = 'Palau', password = generate_password_hash('33Palau45'))
        db.session.add(person159)
        db.session.commit()
        person160 = User(username = 'Panama', password = generate_password_hash('33Panama45'))
        db.session.add(person160)
        db.session.commit()
        person161 = User(username = 'Papua-New-Guinea', password = generate_password_hash('33Papua-New-Guinea45'))
        db.session.add(person161)
        db.session.commit()
        person162 = User(username = 'Paraguay', password = generate_password_hash('33Paraguay45'))
        db.session.add(person162)
        db.session.commit()
        person163 = User(username = 'Peru', password = generate_password_hash('33Peru45'))
        db.session.add(person163)
        db.session.commit()
        person164 = User(username = 'Philippines', password = generate_password_hash('33Philippines45'))
        db.session.add(person164)
        db.session.commit()
        person165 = User(username = 'Pitcairn', password = generate_password_hash('33Pitcairn45'))
        db.session.add(person165)
        db.session.commit()
        person166 = User(username = 'Poland', password = generate_password_hash('33Poland45'))
        db.session.add(person166)
        db.session.commit()
        person167 = User(username = 'Portugal', password = generate_password_hash('33Portugal45'))
        db.session.add(person167)
        db.session.commit()
        person168 = User(username = 'Puerto-Rico', password = generate_password_hash('33Puerto-Rico45'))
        db.session.add(person168)
        db.session.commit()
        person169 = User(username = 'Qatar', password = generate_password_hash('33Qatar45'))
        db.session.add(person169)
        db.session.commit()
        person170 = User(username = 'Reunion', password = generate_password_hash('33Reunion45'))
        db.session.add(person170)
        db.session.commit()
        person171 = User(username = 'Romania', password = generate_password_hash('33Romania45'))
        db.session.add(person171)
        db.session.commit()
        person172 = User(username = 'Russian-Federation', password = generate_password_hash('33Russian-Federation45'))
        db.session.add(person172)
        db.session.commit()
        person173 = User(username = 'Rwanda', password = generate_password_hash('33Rwanda45'))
        db.session.add(person173)
        db.session.commit()
        person174 = User(username = 'Saint-Kitts-and-Nevis', password = generate_password_hash('33Saint-Kitts-and-Nevis45'))
        db.session.add(person174)
        db.session.commit()
        person175 = User(username = 'Saint-Lucia', password = generate_password_hash('33Saint-Lucia45'))
        db.session.add(person175)
        db.session.commit()
        person176 = User(username = 'Saint-Vincent-and-The-Grenadines', password = generate_password_hash('33Saint-Vincent-and-The-Grenadines45'))
        db.session.add(person176)
        db.session.commit()
        person177 = User(username = 'Samoa', password = generate_password_hash('33Samoa45'))
        db.session.add(person177)
        db.session.commit()
        person178 = User(username = 'San-Marino', password = generate_password_hash('33San-Marino45'))
        db.session.add(person178)
        db.session.commit()
        person179 = User(username = 'Sao-Tome-and-Principe', password = generate_password_hash('33Sao-Tome-and-Principe45'))
        db.session.add(person179)
        db.session.commit()
        person180 = User(username = 'Saudi-Arabia', password = generate_password_hash('33Saudi-Arabia45'))
        db.session.add(person180)
        db.session.commit()
        person181 = User(username = 'Senegal', password = generate_password_hash('33Senegal45'))
        db.session.add(person181)
        db.session.commit()
        person182 = User(username = 'Seychelles', password = generate_password_hash('33Seychelles45'))
        db.session.add(person182)
        db.session.commit()
        person183 = User(username = 'Sierra-Leone', password = generate_password_hash('33Sierra-Leone45'))
        db.session.add(person183)
        db.session.commit()
        person184 = User(username = 'Singapore', password = generate_password_hash('33Singapore45'))
        db.session.add(person184)
        db.session.commit()
        person185 = User(username = 'Slovak-Republic', password = generate_password_hash('33Slovak-Republic45'))
        db.session.add(person185)
        db.session.commit()
        person186 = User(username = 'Slovenia', password = generate_password_hash('33Slovenia45'))
        db.session.add(person186)
        db.session.commit()
        person187 = User(username = 'Solomon-Islands', password = generate_password_hash('33Solomon-Islands45'))
        db.session.add(person187)
        db.session.commit()
        person188 = User(username = 'Somalia', password = generate_password_hash('33Somalia45'))
        db.session.add(person188)
        db.session.commit()
        person189 = User(username = 'South-Africa', password = generate_password_hash('33South-Africa45'))
        db.session.add(person189)
        db.session.commit()
        person190 = User(username = 'Spain', password = generate_password_hash('33Spain45'))
        db.session.add(person190)
        db.session.commit()
        person191 = User(username = 'Sri-Lanka', password = generate_password_hash('33Sri-Lanka45'))
        db.session.add(person191)
        db.session.commit()
        person192 = User(username = 'St.Helena', password = generate_password_hash('33St.Helena45'))
        db.session.add(person192)
        db.session.commit()
        person193 = User(username = 'St.Pierre-and-Miquelon', password = generate_password_hash('33St.Pierre-and-Miquelon45'))
        db.session.add(person193)
        db.session.commit()
        person194 = User(username = 'Sudan', password = generate_password_hash('33Sudan45'))
        db.session.add(person194)
        db.session.commit()
        person195 = User(username = 'Suriname', password = generate_password_hash('33Suriname45'))
        db.session.add(person195)
        db.session.commit()
        person196 = User(username = 'Swaziland', password = generate_password_hash('33Swaziland45'))
        db.session.add(person196)
        db.session.commit()
        person197 = User(username = 'Sweden', password = generate_password_hash('33Sweden45'))
        db.session.add(person197)
        db.session.commit()
        person198 = User(username = 'Switzerland', password = generate_password_hash('33Switzerland45'))
        db.session.add(person198)
        db.session.commit()
        person199 = User(username = 'Syria', password = generate_password_hash('33Syria45'))
        db.session.add(person199)
        db.session.commit()
        person200 = User(username = 'Taiwan', password = generate_password_hash('33Taiwan45'))
        db.session.add(person200)
        db.session.commit()
        person201 = User(username = 'Tajikistan', password = generate_password_hash('33Tajikistan45'))
        db.session.add(person201)
        db.session.commit()
        person202 = User(username = 'Tanzania', password = generate_password_hash('33Tanzania45'))
        db.session.add(person202)
        db.session.commit()
        person203 = User(username = 'Thailand', password = generate_password_hash('33Thailand45'))
        db.session.add(person203)
        db.session.commit()
        person204 = User(username = 'Togo', password = generate_password_hash('33Togo45'))
        db.session.add(person204)
        db.session.commit()
        person205 = User(username = 'Tokelau', password = generate_password_hash('33Tokelau45'))
        db.session.add(person205)
        db.session.commit()
        person206 = User(username = 'Tonga', password = generate_password_hash('33Tonga45'))
        db.session.add(person206)
        db.session.commit()
        person207 = User(username = 'Trinidad-and-Tobago', password = generate_password_hash('33Trinidad-and-Tobago45'))
        db.session.add(person207)
        db.session.commit()
        person208 = User(username = 'Tunisia', password = generate_password_hash('33Tunisia45'))
        db.session.add(person208)
        db.session.commit()
        person209 = User(username = 'Turkey', password = generate_password_hash('33Turkey45'))
        db.session.add(person209)
        db.session.commit()
        person210 = User(username = 'Turkmenistan', password = generate_password_hash('33Turkmenistan45'))
        db.session.add(person210)
        db.session.commit()
        person211 = User(username = 'Turks-and-Caicos-Islands', password = generate_password_hash('33Turks-and-Caicos-Islands45'))
        db.session.add(person211)
        db.session.commit()
        person212 = User(username = 'Tuvalu', password = generate_password_hash('33Tuvalu45'))
        db.session.add(person212)
        db.session.commit()
        person213 = User(username = 'Uganda', password = generate_password_hash('33Uganda45'))
        db.session.add(person213)
        db.session.commit()
        person214 = User(username = 'Ukraine', password = generate_password_hash('33Ukraine45'))
        db.session.add(person214)
        db.session.commit()
        person215 = User(username = 'United-Arab-Emirates', password = generate_password_hash('33United-Arab-Emirates45'))
        db.session.add(person215)
        db.session.commit()
        person216 = User(username = 'UAE', password = generate_password_hash('33UAE45'))
        db.session.add(person216)
        db.session.commit()
        person217 = User(username = 'United-Kingdom', password = generate_password_hash('33United-Kingdom45'))
        db.session.add(person217)
        db.session.commit()
        person218 = User(username = 'UK', password = generate_password_hash('33UK45'))
        db.session.add(person218)
        db.session.commit()
        person219 = User(username = 'United-States-of-America', password = generate_password_hash('33United-States-of-America45'))
        db.session.add(person219)
        db.session.commit()
        person220 = User(username = 'United-States', password = generate_password_hash('33United-States45'))
        db.session.add(person220)
        db.session.commit()
        person221 = User(username = 'USA', password = generate_password_hash('33USA45'))
        db.session.add(person221)
        db.session.commit()
        person222 = User(username = 'Uzbekistan', password = generate_password_hash('33Uzbekistan45'))
        db.session.add(person222)
        db.session.commit()
        person223 = User(username = 'Vanuatu', password = generate_password_hash('33Vanuatu45'))
        db.session.add(person223)
        db.session.commit()
        person224 = User(username = 'Vatican-City', password = generate_password_hash('33Vatican-City45'))
        db.session.add(person224)
        db.session.commit()
        person225 = User(username = 'Venezuela', password = generate_password_hash('33Venezuela45'))
        db.session.add(person225)
        db.session.commit()
        person226 = User(username = 'Vietnam', password = generate_password_hash('33Vietnam45'))
        db.session.add(person226)
        db.session.commit()
        person227 = User(username = 'Virgin-Islands', password = generate_password_hash('33Virgin-Islands45'))
        db.session.add(person227)
        db.session.commit()
        person228 = User(username = 'Western-Sahara', password = generate_password_hash('33Western-Sahara45'))
        db.session.add(person228)
        db.session.commit()
        person229 = User(username = 'Yemen', password = generate_password_hash('33Yemen45'))
        db.session.add(person229)
        db.session.commit()
        person230 = User(username = 'Yugoslavia', password = generate_password_hash('33Yugoslavia45'))
        db.session.add(person230)
        db.session.commit()
        person231 = User(username = 'Zaire', password = generate_password_hash('33Zaire45'))
        db.session.add(person231)
        db.session.commit()
        person232 = User(username = 'Zambia', password = generate_password_hash('33Zambia45'))
        db.session.add(person232)
        db.session.commit()
        person233 = User(username = 'Zimbabwe', password = generate_password_hash('33Zimbabwe45'))
        db.session.add(person233)
        db.session.commit()
        person234 = User(username = 'US', password = generate_password_hash('33US45'))
        db.session.add(person234)
        db.session.commit()
        person235 = User(username = 'Chair', password = generate_password_hash('chairMUN6'))
        db.session.add(person235)
        db.session.commit()
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


        # Query database for username
        rows = User.query.filter_by(username=gg).first()

        #print(rows)

        # Ensure username exists and password is correct
        #if len(rows) != 1:
         #   return redirect("/login")

        #if request.form.get("password") != rows[0]["password"]:
        #    return redirect("/login")
        # Ensure username exists and password is correct
        #y = check_password_hash(rows[0]["password"], request.form.get("password"))
        if rows == "shouldnotbethis" or not check_password_hash(rows.password, request.form.get("password")):
            return render_template("login.html")

        #if rows != "shouldnotbethis" or not check_password_hash(rows[0]["password"], request.form.get("password")):
        #    return render_template("login.html")

        #if rows[0]["password"] != request.form.get("password")):
           # return apology("invalid", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")


@app.route("/chair", methods=["GET", "POST"])
def chair():
    if request.method == "POST":
        global counter
        global counter1
        global counter2
        global final_count
        global final_vote
        global agains
        global forr
        global obstain
        global amt
        global countries
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
        return redirect("/")


@app.route("/quickrefresh", methods=["GET", "POST"])
def refresh():
    if request.method == "POST":
        return redirect("/")

@app.route("/raise", methods=["GET", "POST"])
def raise_hand():
    if request.method == "GET":
        return render_template("raise.html")
    elif request.method == "POST":
        global type_hand
        global country_hand
        global number_track
        isit = False
        reason = request.form.get("raise_type")
        before_country_raise = User.query.filter_by(id=session["user_id"]).first()
        country_raise = before_country_raise.username


        for items in country_hand:
            if str(items) == str(country_raise):
                x = country_hand.index(country_raise)
                earlier_raise = type_hand[x]
                type_hand[x] = reason
                isit = True

        if isit == False:
            country_hand.append(country_raise)
            type_hand.append(reason)
        number_track = len(country_hand)
        return redirect("/")

@app.route("/quickraise", methods=["GET", "POST"])
def quick_raise():
    if request.method == "POST":
        global type_hand
        global country_hand
        global number_track
        #sure = False
        before_country_raise = User.query.filter_by(id=session["user_id"]).first()
        current_count = before_country_raise.username

        for items in country_hand:
            if str(items) == str(current_count):
                x = country_hand.index(current_count)
                country_hand.pop(x)
                type_hand.pop(x)
                return redirect("/")


        return render_template("raise.html")

@app.route("/alldown", methods=["GET", "POST"])
def quick_close():
    if request.method == "POST":
        global type_hand
        global country_hand
        global number_track
        number_track = 0
        country_hand = []
        type_hand = []
        return redirect("/")
