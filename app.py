from flask import Flask, render_template
from routers.web import web
from routers.api import api_bp

app = Flask(__name__)
app.register_blueprint(web, url_prefix="/admin")
app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)