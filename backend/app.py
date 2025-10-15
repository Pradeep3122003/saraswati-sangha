import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from extension import db, jwt

load_dotenv()
def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=["http://127.0.0.1:5000"])
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    from routes.auth_manage import auth_bp
    from routes.org import org_bp
    from routes.profile import profile_bp
    from routes.loan import loan_bp
    from routes.transaction import tra_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(org_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(loan_bp)
    app.register_blueprint(tra_bp)
    return app

if __name__=="__main__":
   host=os.getenv("HOST")
   port=os.getenv("PORT")
   debug=True if os.getenv("DEBUG")=="1" else False
   app = create_app()
   app.run(debug=debug, host=host, port=port)
