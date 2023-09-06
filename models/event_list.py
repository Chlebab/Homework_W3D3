from models.event import Event
from datetime import date

event1 = Event(date(2023, 5, 11), 1, 30, "FanDuel", "Networking", "Yes")
event2 = Event(date(2023, 12, 31), 2, 45, "Codebase", "Hot Desking", "Yes")
event3 = Event(date(2023, 2, 28), 3, 100, "Stadium", "Football Match", "No")

events = [event1, event2, event3]
event_counter = len(events)

def add_new_event(new_event):
    events.append(new_event)

def delete_existing_event(index):
    events.remove(index)


