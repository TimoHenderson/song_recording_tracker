from flask import Flask, render_template

# from controllers.songs_controller import songs_blueprint

app = Flask(__name__)

# app.register_blueprint(songs_blueprint)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
