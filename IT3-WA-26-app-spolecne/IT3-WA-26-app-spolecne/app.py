from flask import Flask, render_template
from auth import auth_bp
app = Flask(__name__)

#Registrace Blue Prints
app.register_blueprint(auth_bp)

app.secret_key = "pokemon-tajny-klic-2026"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)