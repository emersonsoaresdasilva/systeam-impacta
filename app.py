from flask import Flask, render_template
from website.controllers import website_bp
from admin.controllers import admin_bp


app = Flask(__name__)
app.secret_key = 'Aiyd876da0d00s'
app.register_blueprint(website_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")


if __name__ == "__main__":
    app.run(debug=True)
