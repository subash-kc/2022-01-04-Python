# a dictionary that is linking a room to other rooms
rooms = {
    "Office Room": {
        "left": "Weapons Room",
        "right": {"Kid's Bedroom", "Stairs"},
        "straight": "Bedroom",
        "items": ["Wallet"]
    },
    "Weapons Room": {
        "right": {"Office Room", "Stairs"},
        "left": "Bedroom",
        "items": ["Weapon"]
    },

    "Bedroom": {
        "straight": {"Office Room", "Kid's Bedroom"},
        "left": "Stairs",
        "right": "Weapons Room",
        "items": ["Spouse"]
    },

    "Kid's Bedroom": {
        "left": {"Office Room", "Weapons Room"},
        "right": "Stairs",
        "straight": "Bedroom",
        "items": ["Kids"]
    },

    "Stairs": {
        "right": {"Office Room", "Kid's Bedroom", "Weapons Room"},
        "left": "Bedroom",
        "down": "Kitchen",
    },

    "Kitchen": {
        "down": "Garage",
        "up": "All Rooms",
        "items": ["Foods"]
    },

    "Garage": {
        "up": "Kitchen",
        "straight": "Outside",
        "items": ["Key", "Car"]
    },

    "Outside": {}

}