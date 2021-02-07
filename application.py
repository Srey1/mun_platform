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
# <meta http-equiv="refresh" content="5" >

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
        return render_template("login.html")


    # User reached route via POST (as by submitting a form via POST)
    else:
        person0 = User('Afghanistan', generate_password_hash('33Afghanistan45')
        db.seesion.add(person0)
        db.session.commit()
        person1 = User('Albania', generate_password_hash('33Albania45')
        db.seesion.add(person1)
        db.session.commit()
        person2 = User('Algeria', generate_password_hash('33Algeria45')
        db.seesion.add(person2)
        db.session.commit()
        person3 = User('American-Samoa', generate_password_hash('33American-Samoa45')
        db.seesion.add(person3)
        db.session.commit()
        person4 = User('Andorra', generate_password_hash('33Andorra45')
        db.seesion.add(person4)
        db.session.commit()
        person5 = User('Angola', generate_password_hash('33Angola45')
        db.seesion.add(person5)
        db.session.commit()
        person6 = User('Anguilla', generate_password_hash('33Anguilla45')
        db.seesion.add(person6)
        db.session.commit()
        person7 = User('Antarctica', generate_password_hash('33Antarctica45')
        db.seesion.add(person7)
        db.session.commit()
        person8 = User('Antigua-and-Barbuda', generate_password_hash('33Antigua-and-Barbuda45')
        db.seesion.add(person8)
        db.session.commit()
        person9 = User('Argentina', generate_password_hash('33Argentina45')
        db.seesion.add(person9)
        db.session.commit()
        person10 = User('Armenia', generate_password_hash('33Armenia45')
        db.seesion.add(person10)
        db.session.commit()
        person11 = User('Aruba', generate_password_hash('33Aruba45')
        db.seesion.add(person11)
        db.session.commit()
        person12 = User('Australia', generate_password_hash('33Australia45')
        db.seesion.add(person12)
        db.session.commit()
        person13 = User('Austria', generate_password_hash('33Austria45')
        db.seesion.add(person13)
        db.session.commit()
        person14 = User('Azerbaijan', generate_password_hash('33Azerbaijan45')
        db.seesion.add(person14)
        db.session.commit()
        person15 = User('Bahamas', generate_password_hash('33Bahamas45')
        db.seesion.add(person15)
        db.session.commit()
        person16 = User('Bahrain', generate_password_hash('33Bahrain45')
        db.seesion.add(person16)
        db.session.commit()
        person17 = User('Bangladesh', generate_password_hash('33Bangladesh45')
        db.seesion.add(person17)
        db.session.commit()
        person18 = User('Barbados', generate_password_hash('33Barbados45')
        db.seesion.add(person18)
        db.session.commit()
        person19 = User('Belarus', generate_password_hash('33Belarus45')
        db.seesion.add(person19)
        db.session.commit()
        person20 = User('Belgium', generate_password_hash('33Belgium45')
        db.seesion.add(person20)
        db.session.commit()
        person21 = User('Belize', generate_password_hash('33Belize45')
        db.seesion.add(person21)
        db.session.commit()
        person22 = User('Benin', generate_password_hash('33Benin45')
        db.seesion.add(person22)
        db.session.commit()
        person23 = User('Bermuda', generate_password_hash('33Bermuda45')
        db.seesion.add(person23)
        db.session.commit()
        person24 = User('Bhutan', generate_password_hash('33Bhutan45')
        db.seesion.add(person24)
        db.session.commit()
        person25 = User('Bolivia', generate_password_hash('33Bolivia45')
        db.seesion.add(person25)
        db.session.commit()
        person26 = User('Bosnia-and-Herzegovina', generate_password_hash('33Bosnia-and-Herzegovina45')
        db.seesion.add(person26)
        db.session.commit()
        person27 = User('Botswana', generate_password_hash('33Botswana45')
        db.seesion.add(person27)
        db.session.commit()
        person28 = User('Bouvet-Island', generate_password_hash('33Bouvet-Island45')
        db.seesion.add(person28)
        db.session.commit()
        person29 = User('Brazil', generate_password_hash('33Brazil45')
        db.seesion.add(person29)
        db.session.commit()
        person30 = User('Bulgaria', generate_password_hash('33Bulgaria45')
        db.seesion.add(person30)
        db.session.commit()
        person31 = User('Burkina-Faso', generate_password_hash('33Burkina-Faso45')
        db.seesion.add(person31)
        db.session.commit()
        person32 = User('Burundi', generate_password_hash('33Burundi45')
        db.seesion.add(person32)
        db.session.commit()
        person33 = User('Cambodia', generate_password_hash('33Cambodia45')
        db.seesion.add(person33)
        db.session.commit()
        person34 = User('Cameroon', generate_password_hash('33Cameroon45')
        db.seesion.add(person34)
        db.session.commit()
        person35 = User('Canada', generate_password_hash('33Canada45')
        db.seesion.add(person35)
        db.session.commit()
        person36 = User('Cape-Verde', generate_password_hash('33Cape-Verde45')
        db.seesion.add(person36)
        db.session.commit()
        person37 = User('Cayman-Islands', generate_password_hash('33Cayman-Islands45')
        db.seesion.add(person37)
        db.session.commit()
        person38 = User('Central-African-Republic', generate_password_hash('33Central-African-Republic45')
        db.seesion.add(person38)
        db.session.commit()
        person39 = User('Chad', generate_password_hash('33Chad45')
        db.seesion.add(person39)
        db.session.commit()
        person40 = User('Chile', generate_password_hash('33Chile45')
        db.seesion.add(person40)
        db.session.commit()
        person41 = User('China', generate_password_hash('33China45')
        db.seesion.add(person41)
        db.session.commit()
        person42 = User('Christmas-Island', generate_password_hash('33Christmas-Island45')
        db.seesion.add(person42)
        db.session.commit()
        person43 = User('Cocos', generate_password_hash('33Cocos45')
        db.seesion.add(person43)
        db.session.commit()
        person44 = User('Colombia', generate_password_hash('33Colombia45')
        db.seesion.add(person44)
        db.session.commit()
        person45 = User('Comoros', generate_password_hash('33Comoros45')
        db.seesion.add(person45)
        db.session.commit()
        person46 = User('Congo', generate_password_hash('33Congo45')
        db.seesion.add(person46)
        db.session.commit()
        person47 = User('Cook-Islands', generate_password_hash('33Cook-Islands45')
        db.seesion.add(person47)
        db.session.commit()
        person48 = User('Costa-Rica', generate_password_hash('33Costa-Rica45')
        db.seesion.add(person48)
        db.session.commit()
        person49 = User('Ivory-Coast', generate_password_hash('33Ivory-Coast45')
        db.seesion.add(person49)
        db.session.commit()
        person50 = User('Croatia', generate_password_hash('33Croatia45')
        db.seesion.add(person50)
        db.session.commit()
        person51 = User('Cuba', generate_password_hash('33Cuba45')
        db.seesion.add(person51)
        db.session.commit()
        person52 = User('Cyprus', generate_password_hash('33Cyprus45')
        db.seesion.add(person52)
        db.session.commit()
        person53 = User('Czech-Republic', generate_password_hash('33Czech-Republic45')
        db.seesion.add(person53)
        db.session.commit()
        person54 = User('Denmark', generate_password_hash('33Denmark45')
        db.seesion.add(person54)
        db.session.commit()
        person55 = User('Djibouti', generate_password_hash('33Djibouti45')
        db.seesion.add(person55)
        db.session.commit()
        person56 = User('Dominica', generate_password_hash('33Dominica45')
        db.seesion.add(person56)
        db.session.commit()
        person57 = User('Dominican-Republic', generate_password_hash('33Dominican-Republic45')
        db.seesion.add(person57)
        db.session.commit()
        person58 = User('East-Timor', generate_password_hash('33East-Timor45')
        db.seesion.add(person58)
        db.session.commit()
        person59 = User('Ecuador', generate_password_hash('33Ecuador45')
        db.seesion.add(person59)
        db.session.commit()
        person60 = User('Egypt', generate_password_hash('33Egypt45')
        db.seesion.add(person60)
        db.session.commit()
        person61 = User('El-Salvador', generate_password_hash('33El-Salvador45')
        db.seesion.add(person61)
        db.session.commit()
        person62 = User('Equatorial-Guinea', generate_password_hash('33Equatorial-Guinea45')
        db.seesion.add(person62)
        db.session.commit()
        person63 = User('Eritrea', generate_password_hash('33Eritrea45')
        db.seesion.add(person63)
        db.session.commit()
        person64 = User('Estonia', generate_password_hash('33Estonia45')
        db.seesion.add(person64)
        db.session.commit()
        person65 = User('Ethiopia', generate_password_hash('33Ethiopia45')
        db.seesion.add(person65)
        db.session.commit()
        person66 = User('Falkland-Islands', generate_password_hash('33Falkland-Islands45')
        db.seesion.add(person66)
        db.session.commit()
        person67 = User('Faroe-Islands', generate_password_hash('33Faroe-Islands45')
        db.seesion.add(person67)
        db.session.commit()
        person68 = User('Fiji', generate_password_hash('33Fiji45')
        db.seesion.add(person68)
        db.session.commit()
        person69 = User('Finland', generate_password_hash('33Finland45')
        db.seesion.add(person69)
        db.session.commit()
        person70 = User('France', generate_password_hash('33France45')
        db.seesion.add(person70)
        db.session.commit()
        person71 = User('Metropolitan', generate_password_hash('33Metropolitan45')
        db.seesion.add(person71)
        db.session.commit()
        person72 = User('French-Guiana', generate_password_hash('33French-Guiana45')
        db.seesion.add(person72)
        db.session.commit()
        person73 = User('French-Polynesia', generate_password_hash('33French-Polynesia45')
        db.seesion.add(person73)
        db.session.commit()
        person74 = User('Gabon', generate_password_hash('33Gabon45')
        db.seesion.add(person74)
        db.session.commit()
        person75 = User('Gambia', generate_password_hash('33Gambia45')
        db.seesion.add(person75)
        db.session.commit()
        person76 = User('Georgia', generate_password_hash('33Georgia45')
        db.seesion.add(person76)
        db.session.commit()
        person77 = User('Germany', generate_password_hash('33Germany45')
        db.seesion.add(person77)
        db.session.commit()
        person78 = User('Ghana', generate_password_hash('33Ghana45')
        db.seesion.add(person78)
        db.session.commit()
        person79 = User('Gibraltar', generate_password_hash('33Gibraltar45')
        db.seesion.add(person79)
        db.session.commit()
        person80 = User('Greece', generate_password_hash('33Greece45')
        db.seesion.add(person80)
        db.session.commit()
        person81 = User('Greenland', generate_password_hash('33Greenland45')
        db.seesion.add(person81)
        db.session.commit()
        person82 = User('Grenada', generate_password_hash('33Grenada45')
        db.seesion.add(person82)
        db.session.commit()
        person83 = User('Guadeloupe', generate_password_hash('33Guadeloupe45')
        db.seesion.add(person83)
        db.session.commit()
        person84 = User('Guam', generate_password_hash('33Guam45')
        db.seesion.add(person84)
        db.session.commit()
        person85 = User('Guatemala', generate_password_hash('33Guatemala45')
        db.seesion.add(person85)
        db.session.commit()
        person86 = User('Guinea', generate_password_hash('33Guinea45')
        db.seesion.add(person86)
        db.session.commit()
        person87 = User('Guinea-Bissau', generate_password_hash('33Guinea-Bissau45')
        db.seesion.add(person87)
        db.session.commit()
        person88 = User('Guyana', generate_password_hash('33Guyana45')
        db.seesion.add(person88)
        db.session.commit()
        person89 = User('Haiti', generate_password_hash('33Haiti45')
        db.seesion.add(person89)
        db.session.commit()
        person90 = User('Honduras', generate_password_hash('33Honduras45')
        db.seesion.add(person90)
        db.session.commit()
        person91 = User('Hong-Kong', generate_password_hash('33Hong-Kong45')
        db.seesion.add(person91)
        db.session.commit()
        person92 = User('Hungary', generate_password_hash('33Hungary45')
        db.seesion.add(person92)
        db.session.commit()
        person93 = User('Iceland', generate_password_hash('33Iceland45')
        db.seesion.add(person93)
        db.session.commit()
        person94 = User('India', generate_password_hash('33India45')
        db.seesion.add(person94)
        db.session.commit()
        person95 = User('Indonesia', generate_password_hash('33Indonesia45')
        db.seesion.add(person95)
        db.session.commit()
        person96 = User('Iran', generate_password_hash('33Iran45')
        db.seesion.add(person96)
        db.session.commit()
        person97 = User('Iraq', generate_password_hash('33Iraq45')
        db.seesion.add(person97)
        db.session.commit()
        person98 = User('Ireland', generate_password_hash('33Ireland45')
        db.seesion.add(person98)
        db.session.commit()
        person99 = User('Israel', generate_password_hash('33Israel45')
        db.seesion.add(person99)
        db.session.commit()
        person100 = User('Italy', generate_password_hash('33Italy45')
        db.seesion.add(person100)
        db.session.commit()
        person101 = User('Jamaica', generate_password_hash('33Jamaica45')
        db.seesion.add(person101)
        db.session.commit()
        person102 = User('Japan', generate_password_hash('33Japan45')
        db.seesion.add(person102)
        db.session.commit()
        person103 = User('Jordan', generate_password_hash('33Jordan45')
        db.seesion.add(person103)
        db.session.commit()
        person104 = User('Kazakhstan', generate_password_hash('33Kazakhstan45')
        db.seesion.add(person104)
        db.session.commit()
        person105 = User('Kenya', generate_password_hash('33Kenya45')
        db.seesion.add(person105)
        db.session.commit()
        person106 = User('Kiribati', generate_password_hash('33Kiribati45')
        db.seesion.add(person106)
        db.session.commit()
        person107 = User('DPRK', generate_password_hash('33DPRK45')
        db.seesion.add(person107)
        db.session.commit()
        person108 = User('South-Korea', generate_password_hash('33South-Korea45')
        db.seesion.add(person108)
        db.session.commit()
        person109 = User('North-Korea', generate_password_hash('33North-Korea45')
        db.seesion.add(person109)
        db.session.commit()
        person110 = User('Kuwait', generate_password_hash('33Kuwait45')
        db.seesion.add(person110)
        db.session.commit()
        person111 = User('Kyrgyzstan', generate_password_hash('33Kyrgyzstan45')
        db.seesion.add(person111)
        db.session.commit()
        person112 = User('Laos', generate_password_hash('33Laos45')
        db.seesion.add(person112)
        db.session.commit()
        person113 = User('Latvia', generate_password_hash('33Latvia45')
        db.seesion.add(person113)
        db.session.commit()
        person114 = User('Lebanon', generate_password_hash('33Lebanon45')
        db.seesion.add(person114)
        db.session.commit()
        person115 = User('Lesotho', generate_password_hash('33Lesotho45')
        db.seesion.add(person115)
        db.session.commit()
        person116 = User('Liberia', generate_password_hash('33Liberia45')
        db.seesion.add(person116)
        db.session.commit()
        person117 = User('Libya', generate_password_hash('33Libya45')
        db.seesion.add(person117)
        db.session.commit()
        person118 = User('Liechtenstein', generate_password_hash('33Liechtenstein45')
        db.seesion.add(person118)
        db.session.commit()
        person119 = User('Lithuania', generate_password_hash('33Lithuania45')
        db.seesion.add(person119)
        db.session.commit()
        person120 = User('Luxembourg', generate_password_hash('33Luxembourg45')
        db.seesion.add(person120)
        db.session.commit()
        person121 = User('Macau', generate_password_hash('33Macau45')
        db.seesion.add(person121)
        db.session.commit()
        person122 = User('Macedonia', generate_password_hash('33Macedonia45')
        db.seesion.add(person122)
        db.session.commit()
        person123 = User('Madagascar', generate_password_hash('33Madagascar45')
        db.seesion.add(person123)
        db.session.commit()
        person124 = User('Malawi', generate_password_hash('33Malawi45')
        db.seesion.add(person124)
        db.session.commit()
        person125 = User('Malaysia', generate_password_hash('33Malaysia45')
        db.seesion.add(person125)
        db.session.commit()
        person126 = User('Maldives', generate_password_hash('33Maldives45')
        db.seesion.add(person126)
        db.session.commit()
        person127 = User('Mali', generate_password_hash('33Mali45')
        db.seesion.add(person127)
        db.session.commit()
        person128 = User('Malta', generate_password_hash('33Malta45')
        db.seesion.add(person128)
        db.session.commit()
        person129 = User('Marshall-Islands', generate_password_hash('33Marshall-Islands45')
        db.seesion.add(person129)
        db.session.commit()
        person130 = User('Martinique', generate_password_hash('33Martinique45')
        db.seesion.add(person130)
        db.session.commit()
        person131 = User('Mauritania', generate_password_hash('33Mauritania45')
        db.seesion.add(person131)
        db.session.commit()
        person132 = User('Mauritius', generate_password_hash('33Mauritius45')
        db.seesion.add(person132)
        db.session.commit()
        person133 = User('Mayotte', generate_password_hash('33Mayotte45')
        db.seesion.add(person133)
        db.session.commit()
        person134 = User('Mexico', generate_password_hash('33Mexico45')
        db.seesion.add(person134)
        db.session.commit()
        person135 = User('Micronesia', generate_password_hash('33Micronesia45')
        db.seesion.add(person135)
        db.session.commit()
        person136 = User('Moldova', generate_password_hash('33Moldova45')
        db.seesion.add(person136)
        db.session.commit()
        person137 = User('Monaco', generate_password_hash('33Monaco45')
        db.seesion.add(person137)
        db.session.commit()
        person138 = User('Mongolia', generate_password_hash('33Mongolia45')
        db.seesion.add(person138)
        db.session.commit()
        person139 = User('Montserrat', generate_password_hash('33Montserrat45')
        db.seesion.add(person139)
        db.session.commit()
        person140 = User('Morocco', generate_password_hash('33Morocco45')
        db.seesion.add(person140)
        db.session.commit()
        person141 = User('Mozambique', generate_password_hash('33Mozambique45')
        db.seesion.add(person141)
        db.session.commit()
        person142 = User('Myanmar', generate_password_hash('33Myanmar45')
        db.seesion.add(person142)
        db.session.commit()
        person143 = User('Namibia', generate_password_hash('33Namibia45')
        db.seesion.add(person143)
        db.session.commit()
        person144 = User('Nauru', generate_password_hash('33Nauru45')
        db.seesion.add(person144)
        db.session.commit()
        person145 = User('Nepal', generate_password_hash('33Nepal45')
        db.seesion.add(person145)
        db.session.commit()
        person146 = User('Netherlands', generate_password_hash('33Netherlands45')
        db.seesion.add(person146)
        db.session.commit()
        person147 = User('Netherlands-Antilles', generate_password_hash('33Netherlands-Antilles45')
        db.seesion.add(person147)
        db.session.commit()
        person148 = User('New-Caledonia', generate_password_hash('33New-Caledonia45')
        db.seesion.add(person148)
        db.session.commit()
        person149 = User('New-Zealand', generate_password_hash('33New-Zealand45')
        db.seesion.add(person149)
        db.session.commit()
        person150 = User('Nicaragua', generate_password_hash('33Nicaragua45')
        db.seesion.add(person150)
        db.session.commit()
        person151 = User('Niger', generate_password_hash('33Niger45')
        db.seesion.add(person151)
        db.session.commit()
        person152 = User('Nigeria', generate_password_hash('33Nigeria45')
        db.seesion.add(person152)
        db.session.commit()
        person153 = User('Niue', generate_password_hash('33Niue45')
        db.seesion.add(person153)
        db.session.commit()
        person154 = User('Norfolk-Island', generate_password_hash('33Norfolk-Island45')
        db.seesion.add(person154)
        db.session.commit()
        person155 = User('Northern-Mariana-Islands', generate_password_hash('33Northern-Mariana-Islands45')
        db.seesion.add(person155)
        db.session.commit()
        person156 = User('Norway', generate_password_hash('33Norway45')
        db.seesion.add(person156)
        db.session.commit()
        person157 = User('Oman', generate_password_hash('33Oman45')
        db.seesion.add(person157)
        db.session.commit()
        person158 = User('Pakistan', generate_password_hash('33Pakistan45')
        db.seesion.add(person158)
        db.session.commit()
        person159 = User('Palau', generate_password_hash('33Palau45')
        db.seesion.add(person159)
        db.session.commit()
        person160 = User('Panama', generate_password_hash('33Panama45')
        db.seesion.add(person160)
        db.session.commit()
        person161 = User('Papua-New-Guinea', generate_password_hash('33Papua-New-Guinea45')
        db.seesion.add(person161)
        db.session.commit()
        person162 = User('Paraguay', generate_password_hash('33Paraguay45')
        db.seesion.add(person162)
        db.session.commit()
        person163 = User('Peru', generate_password_hash('33Peru45')
        db.seesion.add(person163)
        db.session.commit()
        person164 = User('Philippines', generate_password_hash('33Philippines45')
        db.seesion.add(person164)
        db.session.commit()
        person165 = User('Pitcairn', generate_password_hash('33Pitcairn45')
        db.seesion.add(person165)
        db.session.commit()
        person166 = User('Poland', generate_password_hash('33Poland45')
        db.seesion.add(person166)
        db.session.commit()
        person167 = User('Portugal', generate_password_hash('33Portugal45')
        db.seesion.add(person167)
        db.session.commit()
        person168 = User('Puerto-Rico', generate_password_hash('33Puerto-Rico45')
        db.seesion.add(person168)
        db.session.commit()
        person169 = User('Qatar', generate_password_hash('33Qatar45')
        db.seesion.add(person169)
        db.session.commit()
        person170 = User('Reunion', generate_password_hash('33Reunion45')
        db.seesion.add(person170)
        db.session.commit()
        person171 = User('Romania', generate_password_hash('33Romania45')
        db.seesion.add(person171)
        db.session.commit()
        person172 = User('Russian-Federation', generate_password_hash('33Russian-Federation45')
        db.seesion.add(person172)
        db.session.commit()
        person173 = User('Rwanda', generate_password_hash('33Rwanda45')
        db.seesion.add(person173)
        db.session.commit()
        person174 = User('Saint-Kitts-and-Nevis', generate_password_hash('33Saint-Kitts-and-Nevis45')
        db.seesion.add(person174)
        db.session.commit()
        person175 = User('Saint-Lucia', generate_password_hash('33Saint-Lucia45')
        db.seesion.add(person175)
        db.session.commit()
        person176 = User('Saint-Vincent-and-The-Grenadines', generate_password_hash('33Saint-Vincent-and-The-Grenadines45')
        db.seesion.add(person176)
        db.session.commit()
        person177 = User('Samoa', generate_password_hash('33Samoa45')
        db.seesion.add(person177)
        db.session.commit()
        person178 = User('San-Marino', generate_password_hash('33San-Marino45')
        db.seesion.add(person178)
        db.session.commit()
        person179 = User('Sao-Tome-and-Principe', generate_password_hash('33Sao-Tome-and-Principe45')
        db.seesion.add(person179)
        db.session.commit()
        person180 = User('Saudi-Arabia', generate_password_hash('33Saudi-Arabia45')
        db.seesion.add(person180)
        db.session.commit()
        person181 = User('Senegal', generate_password_hash('33Senegal45')
        db.seesion.add(person181)
        db.session.commit()
        person182 = User('Seychelles', generate_password_hash('33Seychelles45')
        db.seesion.add(person182)
        db.session.commit()
        person183 = User('Sierra-Leone', generate_password_hash('33Sierra-Leone45')
        db.seesion.add(person183)
        db.session.commit()
        person184 = User('Singapore', generate_password_hash('33Singapore45')
        db.seesion.add(person184)
        db.session.commit()
        person185 = User('Slovak-Republic', generate_password_hash('33Slovak-Republic45')
        db.seesion.add(person185)
        db.session.commit()
        person186 = User('Slovenia', generate_password_hash('33Slovenia45')
        db.seesion.add(person186)
        db.session.commit()
        person187 = User('Solomon-Islands', generate_password_hash('33Solomon-Islands45')
        db.seesion.add(person187)
        db.session.commit()
        person188 = User('Somalia', generate_password_hash('33Somalia45')
        db.seesion.add(person188)
        db.session.commit()
        person189 = User('South-Africa', generate_password_hash('33South-Africa45')
        db.seesion.add(person189)
        db.session.commit()
        person190 = User('Spain', generate_password_hash('33Spain45')
        db.seesion.add(person190)
        db.session.commit()
        person191 = User('Sri-Lanka', generate_password_hash('33Sri-Lanka45')
        db.seesion.add(person191)
        db.session.commit()
        person192 = User('St.Helena', generate_password_hash('33St.Helena45')
        db.seesion.add(person192)
        db.session.commit()
        person193 = User('St.Pierre-and-Miquelon', generate_password_hash('33St.Pierre-and-Miquelon45')
        db.seesion.add(person193)
        db.session.commit()
        person194 = User('Sudan', generate_password_hash('33Sudan45')
        db.seesion.add(person194)
        db.session.commit()
        person195 = User('Suriname', generate_password_hash('33Suriname45')
        db.seesion.add(person195)
        db.session.commit()
        person196 = User('Swaziland', generate_password_hash('33Swaziland45')
        db.seesion.add(person196)
        db.session.commit()
        person197 = User('Sweden', generate_password_hash('33Sweden45')
        db.seesion.add(person197)
        db.session.commit()
        person198 = User('Switzerland', generate_password_hash('33Switzerland45')
        db.seesion.add(person198)
        db.session.commit()
        person199 = User('Syria', generate_password_hash('33Syria45')
        db.seesion.add(person199)
        db.session.commit()
        person200 = User('Taiwan', generate_password_hash('33Taiwan45')
        db.seesion.add(person200)
        db.session.commit()
        person201 = User('Tajikistan', generate_password_hash('33Tajikistan45')
        db.seesion.add(person201)
        db.session.commit()
        person202 = User('Tanzania', generate_password_hash('33Tanzania45')
        db.seesion.add(person202)
        db.session.commit()
        person203 = User('Thailand', generate_password_hash('33Thailand45')
        db.seesion.add(person203)
        db.session.commit()
        person204 = User('Togo', generate_password_hash('33Togo45')
        db.seesion.add(person204)
        db.session.commit()
        person205 = User('Tokelau', generate_password_hash('33Tokelau45')
        db.seesion.add(person205)
        db.session.commit()
        person206 = User('Tonga', generate_password_hash('33Tonga45')
        db.seesion.add(person206)
        db.session.commit()
        person207 = User('Trinidad-and-Tobago', generate_password_hash('33Trinidad-and-Tobago45')
        db.seesion.add(person207)
        db.session.commit()
        person208 = User('Tunisia', generate_password_hash('33Tunisia45')
        db.seesion.add(person208)
        db.session.commit()
        person209 = User('Turkey', generate_password_hash('33Turkey45')
        db.seesion.add(person209)
        db.session.commit()
        person210 = User('Turkmenistan', generate_password_hash('33Turkmenistan45')
        db.seesion.add(person210)
        db.session.commit()
        person211 = User('Turks-and-Caicos-Islands', generate_password_hash('33Turks-and-Caicos-Islands45')
        db.seesion.add(person211)
        db.session.commit()
        person212 = User('Tuvalu', generate_password_hash('33Tuvalu45')
        db.seesion.add(person212)
        db.session.commit()
        person213 = User('Uganda', generate_password_hash('33Uganda45')
        db.seesion.add(person213)
        db.session.commit()
        person214 = User('Ukraine', generate_password_hash('33Ukraine45')
        db.seesion.add(person214)
        db.session.commit()
        person215 = User('United-Arab-Emirates', generate_password_hash('33United-Arab-Emirates45')
        db.seesion.add(person215)
        db.session.commit()
        person216 = User('UAE', generate_password_hash('33UAE45')
        db.seesion.add(person216)
        db.session.commit()
        person217 = User('United-Kingdom', generate_password_hash('33United-Kingdom45')
        db.seesion.add(person217)
        db.session.commit()
        person218 = User('UK', generate_password_hash('33UK45')
        db.seesion.add(person218)
        db.session.commit()
        person219 = User('United-States-of-America', generate_password_hash('33United-States-of-America45')
        db.seesion.add(person219)
        db.session.commit()
        person220 = User('United-States', generate_password_hash('33United-States45')
        db.seesion.add(person220)
        db.session.commit()
        person221 = User('USA', generate_password_hash('33USA45')
        db.seesion.add(person221)
        db.session.commit()
        person222 = User('Uzbekistan', generate_password_hash('33Uzbekistan45')
        db.seesion.add(person222)
        db.session.commit()
        person223 = User('Vanuatu', generate_password_hash('33Vanuatu45')
        db.seesion.add(person223)
        db.session.commit()
        person224 = User('Vatican-City', generate_password_hash('33Vatican-City45')
        db.seesion.add(person224)
        db.session.commit()
        person225 = User('Venezuela', generate_password_hash('33Venezuela45')
        db.seesion.add(person225)
        db.session.commit()
        person226 = User('Vietnam', generate_password_hash('33Vietnam45')
        db.seesion.add(person226)
        db.session.commit()
        person227 = User('Virgin-Islands', generate_password_hash('33Virgin-Islands45')
        db.seesion.add(person227)
        db.session.commit()
        person228 = User('Western-Sahara', generate_password_hash('33Western-Sahara45')
        db.seesion.add(person228)
        db.session.commit()
        person229 = User('Yemen', generate_password_hash('33Yemen45')
        db.seesion.add(person229)
        db.session.commit()
        person230 = User('Yugoslavia', generate_password_hash('33Yugoslavia45')
        db.seesion.add(person230)
        db.session.commit()
        person231 = User('Zaire', generate_password_hash('33Zaire45')
        db.seesion.add(person231)
        db.session.commit()
        person232 = User('Zambia', generate_password_hash('33Zambia45')
        db.seesion.add(person232)
        db.session.commit()
        person233 = User('Zimbabwe', generate_password_hash('33Zimbabwe45')
        db.seesion.add(person233)
        db.session.commit()
        person234 = User('US', generate_password_hash('33US45')
        db.seesion.add(person234)
        db.session.commit()
        person235 = User('Chair', generate_password_hash('33Chair45')
        db.seesion.add(person235)
        db.session.commit()

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
        counter = []
        counter1 = []
        counter2 = []
        final_count = []
        final_vote = []
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
