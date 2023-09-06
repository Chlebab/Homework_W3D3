from models.event import Event

event1 = Event("01/02/2023", 1, 30, "FanDuel", "Networking")
event2 = Event("15/06/2023", 2, 45, "Codebase", "Hot Desking")
event3 = Event("31/11/2023", 3, 100, "Stadium", "Football Match")

events = [event1, event2, event3]

def add_new_event(new_event):
    events.append(new_event)