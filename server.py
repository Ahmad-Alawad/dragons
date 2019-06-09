from flask import Flask, render_template, request, flash, redirect, session
from model import Dragon, Place, db

app = Flask(__name__)


app.secret_key = "ABC"


@app.route("/dashboard")
def dashboard():
    all_dragons = Dragon.query.all()
    all_places = Place.query.all()
    return render_template("dashboard.html", all_dragons=all_dragons, all_places=all_places)


@app.route("/change_place", methods=['POST'])
def change_place():
    """ This will be used to change the place of the dragon """
    dragon_id = request.form["dragon_id"]
    selected_place = request.form["selected_place"]
    print "\n\n\n\n After processing POST"
    # Some other stuff need to be done here
    # It also gives 400 for now
    return redirect("/dashboard")



if __name__ == "__main__":
	from model import connect_to_db
	connect_to_db(app)

	app.run(port=5003, host='0.0.0.0')