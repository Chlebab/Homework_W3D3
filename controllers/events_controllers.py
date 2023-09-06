from flask import render_template, Blueprint, request
from models.event_list import events, add_new_event
from models.event import Event


events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='Events list', events=events)

@events_blueprint.route("/events", methods=["POST"])
def add_event():
    print(request.form)
    date = request.form["date"]
    event_number = request.form["event_number"]
    guest_number = request.form["guest_number"]
    room_location = request.form["room_location"]
    description = request.form["description"]

    new_event = Event(date, event_number, guest_number, room_location, description)
    add_new_event(new_event)
    return "Done"
