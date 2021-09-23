from flask import Flask, render_template, jsonify

# Write the first 10 letters next to each other
# Clicking on letters load shows starting with that letter that has more than 20 episodes
# title, year, episode count, actor count
# Page mustn’t reload (so you have to do it with fetch)
import data_manager

app = Flask(__name__)


@app.route("/")
def main_page():
    list_of_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    return render_template("index.html", list_of_letters=list_of_letters)


@app.route("/api/shows/<string:letter>")
def get_shows(letter):
    data = data_manager.get_shows_by_letter(letter)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
