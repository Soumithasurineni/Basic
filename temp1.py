from flask import Flask, render_template

app = Flask(__name__)
print("Hello")

@app.route("/Users/DELL/OneDrive/Desktop/flask jpmc/<user>")
def index(user):
    return render_template('index.html', name=user)


if __name__ == "__main__":
    app.run(debug=True)