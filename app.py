from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) 

    db.init_app(app) 

    @app.route("/")
    def home():
        return "Hola Flask! 🚀"

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


