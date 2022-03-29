from flask import Flask, render_template
import random

app = Flask(__name__)

# Add your name in this list!
trainees = [
    "Harry",
    "Bestami",
    "Yusuf",
    "Rhys",
]
# Add a food you like (or don't!) in this list!
foods = [
    "pizza",
    "lasagne",
    "lahmacun",
    "Ramen",
]

@app.route('/')
def home():
    trainee = random.choice(trainees)
    food = random.choice(foods)
    return render_template("index.html", trainee=trainee, food=food)

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)
