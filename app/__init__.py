from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

from app import views
from app import admin_views


