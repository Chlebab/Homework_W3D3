from flask import Flask
from controllers.events_controllers import events_blueprint

app = Flask(__name__)
app.register_blueprint(events_blueprint)