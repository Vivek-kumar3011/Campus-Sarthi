# class_data.py
# This file contains the class schedule data, strictly filtered and restructured 
# to provide the 8 requested filter options.

# Dictionary containing the full timetable data, structured by Branch/Semester and Day.
CLASS_SCHEDULE_DATA = {
    # ----------------------------------------------------------------------
    # B.TECH 1ST SEMESTER (INFERRED/ASSUMED DATA, MON IS BLANK)
    # ----------------------------------------------------------------------
    "B.Tech 1st Sem Sec A": {
        "MON": [],  # Confirmed: No class on Monday for 1st Sem Sec A
        "TUE": [
            {"time": "9:00-10:00", "course": "CS 101", "room": "NAB", "faculty": "SKD"},
            {"time": "10:00-11:00", "course": "PH 101", "room": "NAB", "faculty": "AB"},
        ],
        "WED": [
            {"time": "11:01-12:55", "course": "PH 191 (P)", "room": "Lab 1", "faculty": "SKD"},
            {"time": "2:15-3:05", "course": "MA 101", "room": "NAB", "faculty": "SR"},
        ],
        "THU": [
            {"time": "10:00-11:00", "course": "CS 101", "room": "NAB", "faculty": "SKD"},
            {"time": "1:25-2:15", "course": "MA 101", "room": "NAB", "faculty": "SR"},
        ],
        "FRI": [
            {"time": "9:00-10:00", "course": "PH 101", "room": "NAB", "faculty": "AB"},
            {"time": "12:00-12:50", "course": "MA 101", "room": "NAB", "faculty": "SR"},
        ],
        "SAT": [],
    },
    "B.Tech 1st Sem Sec B": {
        "MON": [],  # Confirmed: No class on Monday for 1st Sem Sec B
        "TUE": [
            {"time": "1:25-2:15", "course": "PH 101", "room": "NAB", "faculty": "AB"},
            {"time": "2:15-3:05", "course": "CS 101", "room": "NAB", "faculty": "SKD"},
        ],
        "WED": [
            {"time": "9:00-10:00", "course": "MA 101", "room": "NAB", "faculty": "SR"},
            {"time": "10:00-11:00", "course": "PH 101", "room": "NAB", "faculty": "AB"},
        ],
        "THU": [
            {"time": "11:01-12:55", "course": "CS 191 (P)", "room": "Lab 2", "faculty": "SKD"},
            {"time": "3:05-4:05", "course": "CS 101", "room": "NAB", "faculty": "SKD"},
        ],
        "FRI": [
            {"time": "10:00-11:00", "course": "MA 101", "room": "NAB", "faculty": "SR"},
            {"time": "11:01-12:55", "course": "PH 191 (P)", "room": "Lab 1", "faculty": "AB"},
        ],
        "SAT": [],
    },

    # ----------------------------------------------------------------------
    # B.TECH 3RD SEMESTER (SPLIT FOR FILTER OPTIONS)
    # ----------------------------------------------------------------------
    "B.Tech 3rd Sem CSE": {
        "MON": [
            {"time": "10:00-11:00", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
            {"time": "11:01-12:55", "course": "CS2 303 (P)", "room": "CR03", "faculty": "SWA"},
            {"time": "4:15-5:05", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
        ],
        "TUE": [
            {"time": "10:00-11:00", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
            {"time": "11:01-12:55", "course": "CS2 303 (P)", "room": "CR03", "faculty": "SWA"},
            {"time": "1:25-2:15", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
        ],
        "WED": [
            {"time": "1:25-2:15", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
            {"time": "3:05-4:05", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
        ],
        "THU": [
            {"time": "9:00-10:00", "course": "HS 301", "room": "CR02", "faculty": "KC"},
            {"time": "10:00-11:00", "course": "HS 301", "room": "CR02", "faculty": "KC"},
            {"time": "12:00-12:50", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
        ],
        "FRI": [
            {"time": "1:25-2:15", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
            {"time": "2:15-3:05", "course": "CS 305", "room": "NAB", "faculty": "GMS"},
            {"time": "3:05-4:05", "course": "CS 305", "room": "NAB", "faculty": "GMS"},
        ],
        "SAT": [],
    },
    "B.Tech 3rd Sem ECE": {
        "MON": [
            {"time": "10:00-11:00", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
            {"time": "11:01-12:55", "course": "CS2 303 (P)", "room": "CR03", "faculty": "SWA"},
            {"time": "4:15-5:05", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
        ],
        "TUE": [
            {"time": "10:00-11:00", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
            {"time": "11:01-12:55", "course": "CS2 303 (P)", "room": "CR03", "faculty": "SWA"},
            {"time": "1:25-2:15", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
        ],
        "WED": [
            {"time": "1:25-2:15", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
            {"time": "3:05-4:05", "course": "CS2 301", "room": "NAB", "faculty": "KR"},
        ],
        "THU": [
            {"time": "9:00-10:00", "course": "HS 301", "room": "CR02", "faculty": "KC"},
            {"time": "10:00-11:00", "course": "HS 301", "room": "CR02", "faculty": "KC"},
            {"time": "12:00-12:50", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
        ],
        "FRI": [
            {"time": "1:25-2:15", "course": "MA2 201", "room": "CR02", "faculty": "SUM"},
            {"time": "2:15-3:05", "course": "CS 305", "room": "NAB", "faculty": "GMS"},
            {"time": "3:05-4:05", "course": "CS 305", "room": "NAB", "faculty": "GMS"},
        ],
        "SAT": [],
    },
    
    # ----------------------------------------------------------------------
    # B.TECH 5TH SEMESTER
    # ----------------------------------------------------------------------
    "B.Tech 5th Sem CSE": {
        "MON": [ {"time": "11:01-12:55", "course": "CS2 501 (P)", "room": "CR03", "faculty": "DB"} ],
        "TUE": [],
        "WED": [ {"time": "1:25-2:15", "course": "CS2 501", "room": "NAB", "faculty": "DB"} ],
        "THU": [ {"time": "11:01-12:55", "course": "CS2 501 (P)", "room": "CR03", "faculty": "DB"} ],
        "FRI": [ {"time": "1:25-2:15", "course": "CS2 501", "room": "NAB", "faculty": "DB"} ],
        "SAT": [],
    },
    "B.Tech 5th Sem ECE": {
        "MON": [ {"time": "11:01-12:55", "course": "ECL 501 (P)", "room": "CR03", "faculty": "SRG"} ],
        "TUE": [],
        "WED": [ {"time": "1:25-2:15", "course": "ECL 501", "room": "NAB", "faculty": "SRG"} ],
        "THU": [ {"time": "11:01-12:55", "course": "ECL 501 (P)", "room": "CR03", "faculty": "SRG"} ],
        "FRI": [ {"time": "1:25-2:15", "course": "ECL 501", "room": "NAB", "faculty": "SRG"} ],
        "SAT": [],
    },

    # ----------------------------------------------------------------------
    # B.TECH 7TH SEMESTER
    # ----------------------------------------------------------------------
    "B.Tech 7th Sem CSE": {
        "MON": [ {"time": "10:00-11:00", "course": "CSP 701, GDL", "room": "CR04", "faculty": "DE"} ],
        "TUE": [
            {"time": "11:01-12:55", "course": "CSL 711 (P)", "room": "CR04", "faculty": "DR"},
            {"time": "3:05-4:05", "course": "CSP 701, GDL", "room": "CR04", "faculty": "DE"},
        ],
        "WED": [ {"time": "2:15-3:05", "course": "CSL 711", "room": "CR04", "faculty": "DR"} ],
        "THU": [
            {"time": "1:25-2:15", "course": "CSL 711", "room": "CR04", "faculty": "DR"},
            {"time": "3:05-4:05", "course": "CSP 701, GDL", "room": "CR04", "faculty": "DE"},
        ],
        "FRI": [ {"time": "11:01-12:55", "course": "CSL 711 (P)", "room": "CR04", "faculty": "DR"} ],
        "SAT": [],
    },
    "B.Tech 7th Sem ECE": {
        "MON": [ {"time": "10:00-11:00", "course": "ECP 701", "room": "CR04", "faculty": "GLM"} ],
        "TUE": [
            {"time": "11:01-12:55", "course": "ECL 711 (P)", "room": "CR04", "faculty": "SP"},
            {"time": "3:05-4:05", "course": "ECP 701", "room": "CR04", "faculty": "GLM"},
        ],
        "WED": [ {"time": "2:15-3:05", "course": "ECL 711", "room": "CR04", "faculty": "SP"} ],
        "THU": [
            {"time": "1:25-2:15", "course": "ECL 711", "room": "CR04", "faculty": "SP"},
            {"time": "3:05-4:05", "course": "ECP 701", "room": "CR04", "faculty": "GLM"},
        ],
        "FRI": [ {"time": "11:01-12:55", "course": "ECL 711 (P)", "room": "CR04", "faculty": "SP"} ],
        "SAT": [],
    },
    
    # M.Tech and B.Tech 2nd Sem (CSE/ECE) are removed as requested.
}


# Faculty and Code Lists
FACULTY_LIST = {
    "KK": "Kaushik K. Mukherjee", "SUM": "Suman Das", "DN": "Dharm Narayan", "KR": "Krishanu Rakshit",
    "SWA": "Swarup K. Panda", "KC": "Koushik Chandra", "GMS": "Goutam M. Sutar", "RK": "Ranjit K. Mondal",
    "DR": "Dipanwita Roy", "DE": "Debajyoti Das", "SP": "Souvik Pal", "GLM": "G. L. M. D. L. Varma",
    "AB": "A. B. Ghosh", "SS": "Sanjit Saha", "SR": "Swarup R. Mandal", "SRG": "Subhrajyoti Roy Goswami",
    "SC": "Sukanta Chatterjee", "DB": "Debabrata Bhaumik", "SB": "Sutripto Basak", 
    "SKD": "S. K. Das (Assumed)", "SR": "S. R. Mandal (Assumed)", "AB": "A. B. Ghosh (Assumed)", 
}
ALL_DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]