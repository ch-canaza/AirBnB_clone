#!/usr/bin/python3
"""
class that inherits from BaseModel
"""


class Place(BaseModel):
    """ class containing places
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = ""
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
