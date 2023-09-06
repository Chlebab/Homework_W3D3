class Event():
    def __init__(self, date, event_number, guest_number, room_location, description, recurring):
        self.date = date
        self.event_number = event_number
        self.guest_number = guest_number
        self.room_location = room_location
        self.description = description
        self.recurring = recurring