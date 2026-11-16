from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__) 


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    
    
@app.route('/')
def home():
    return render_template('home.html')    

@app.route('/about')
def about():
    return render_template('about.html')    




if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Database created succesfully!")
        except Exception as e:
            print(f"An error occured: {e}")
            
        app.run(debug=True)
            