from flask import render_template, Blueprint, request, redirect
from models.event_list import events, add_new_event, delete_existing_event
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
    # if request.form.get("recurring") == None:
    #     recurring = "No"
    if "recurring" in request.form:
        recurring = request.form["recurring"]
    else:
        recurring = "No"
    new_event = Event(date, event_number, guest_number, room_location, description, recurring)
    add_new_event(new_event)
    return "Done"

@events_blueprint.route("/events/delete/<index>", methods=["GET", "POST"])
def delete_event(index):
    chosen_order = events[int(index)]
    delete_existing_event(chosen_order)
    return redirect("/events")

