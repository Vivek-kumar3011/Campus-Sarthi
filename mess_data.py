"""
Data file containing the weekly mess menu, time slots, and general notes,
based on the provided mess menu image.
"""

# Time slots for each meal
TIME_SLOTS = {
    "Breakfast": "(8:00 to 9:00)",
    "Lunch": "(1:00 to 2:00)",
    "Snacks": "(5:20 to 6:00)",
    "Dinner": "(8:00 to 9:00)"
}

# Weekly mess menu data
MESS_MENU = {
    "Monday": {
        "Breakfast": "Poha / Idli Sambhar (4pc) + Chutney",
        "Lunch": "Veg Sabji + Rice + Roti + Papad",
        "Snacks": "Manchurian (4pc)",
        "Dinner": "Egg/Paneer do piaza (4pc) + Rice + Roti + Dal + Rasgulla"
    },
    "Tuesday": {
        "Breakfast": "Corn Flakes + Milk",
        "Lunch": "Aloo Bhujia + Dal + Rice + Roti + Curd",
        "Snacks": "Maggi (original)",
        "Dinner": "Sattu Paratha + Aloo Dum + Jeera Rice + Sewai"
    },
    "Wednesday": {
        "Breakfast": "Chowmien + Ketchup",
        "Lunch": "Lawki Chana / Fried Aloo Soya + Dal + Rice + Curd",
        "Snacks": "Samosa (2pc) + Ghogni + Onion + Chutney",
        "Dinner": "Chicken (3pc) / Paneer Bhurji + Dal Makhani + Rice + Roti + Rasgulla"
    },
    "Thursday": {
        "Breakfast": "Sprouts + Suji Halwa",
        "Lunch": "Veg Sabji + Rice + Dal + Papad/Chips",
        "Snacks": "Aloo/Onion Pakora",
        "Dinner": "Jeera Rice + Dal Fry + Baigan/Aloo Bhaji + Roti + Chum Chum"
    },
    "Friday": {
        "Breakfast": "Puri (4pc) + Ghugni",
        "Lunch": "Aloo Bhujia + Dal + Rice + Roti + Curd",
        "Snacks": "Sprouts + Banana (1pcs)",
        "Dinner": "Omelette (1pc) / Kadai Paneer (4pcs) + Dal + Roti + Rice + Halwa"
    },
    "Saturday": {
        "Breakfast": "Pav Bhaji + Onion & Lemon",
        "Lunch": "Kala chana + Masala Rice + Roti + Curd + Dal",
        "Snacks": "Aloo Tikki Burger",
        "Dinner": "Plane Paratha + Jeera Aloo + Kheer"
    },
    "Sunday": {
        "Breakfast": "Aloo Paratha (2pc)+Pickle/Onion Paratha (2pc) + Pickle/Curd",
        "Lunch": "Chicken (3pc) / Paneer Bhurji + Fried Rice + Dal + Roti + Curd",
        "Snacks": "Pani Puri (Fuchka, 7pc) / Macaroni",
        "Dinner": "Khichdi + Aloo dum  Veg Biriyani / Pulao + Suji Halwa"
    }
}

# General mess notes
MESS_NOTES = (
    "NOTE:\n"
    "Tea, Biscuit and Banana will be served on each day (Breakfast).\n"
    "Tea will be served on every day at Snacks (except Sunday)."
)