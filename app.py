from flask import Flask, render_template
from routers.web import web
from routers.api import api_bp
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.register_blueprint(web, url_prefix="/admin")
app.register_blueprint(api_bp, url_prefix="/api")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/mps_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)