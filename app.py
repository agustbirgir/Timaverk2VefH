from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    return "Hallo Heimur!"#add comment
=======
    return "Hallo Heimur!"
>>>>>>> origin/New-Features
    
