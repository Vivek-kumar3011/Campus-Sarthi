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
            {"time": "10:10-12:50", "course": "ECC 111", "room": "(203, 206)", "faculty": "SAS"},
            {"time": "2:15-4:00", "course": "MAC 101", "room": "302", "faculty": "AL"},
        ],
        "WED": [
            {"time": "9:15-10:05", "course": "ECC 101", "room": "G01", "faculty": "SAS"},
            {"time": "10:10-12:50", "course": "CSC 111", "room": "(201,202,207)", "faculty": "SP"},
            {"time": "3:10-4:00", "course": "CSC 101", "room": "G01", "faculty": "SP"},
        ],
        "THU": [
            {"time": "9:15-11:00", "course": "ECC 101", "room": "G01", "faculty": "SAS"},
            {"time": "11:05-12:50", "course": "MAC 101", "room": "G01", "faculty": "(PB,AL)"},
            {"time": "2:15-4:00", "course": "PHC 101", "room": "G01", "faculty": "UD"},
        ],
        "FRI": [
            {"time": "9:15-11:00", "course": "CSC 101", "room": "G01", "faculty": "SP"},
            {"time": "11:05-12:50", "course": "PHC 101", "room": "G01", "faculty": "UD"},
        ],
        "SAT": [
            {"time": "9:15-11:00", "course": "HUC 101", "room": "G01", "faculty": "SB"},
            {"time": "11:05-12:50", "course": "HUC 102", "room": "G01", "faculty": "RK"},
            {"time": "2:15-3:05", "course": "HUC 101", "room": "G01", "faculty": "SB"},
            {"time": "3:10-4:00", "course": "HUC 102", "room": "G01", "faculty": "RK"},
        ],
    },
    "B.Tech 1st Sem Sec B": {
        "MON": [],  # Confirmed: No class on Monday for 1st Sem Sec B
        "TUE": [
            {"time": "10:10-12:50", "course": "CSC 111", "room": "(201,202,207)", "faculty": "BB"},
            {"time": "2:15-4:55", "course": "ECC 111", "room": "(203,206)", "faculty": "SAS"},
        ],
        "WED": [
            {"time": "10:10-11:00", "course": "ECC 101", "room": "G02", "faculty": "SAS"},
            {"time": "11:05-12:50", "course": "PHC 101", "room": "G02", "faculty": "UD"},
            {"time": "2:15-3:05", "course": "CSC 101", "room": "G01", "faculty": "BB"},
        ],
        "THU": [
            {"time": "9:15-11:00", "course": "CSC 101", "room": "G02", "faculty": "BB"},
            {"time": "11:05-12:50", "course": "ECC 101", "room": "G02", "faculty": "SAS"},
            {"time": "3:10-4:55", "course": "MAC 101", "room": "G02", "faculty": "(PB,AL)"},
        ],
        "FRI": [
            {"time": "9:15-11:00", "course": "PHC 101", "room": "G02", "faculty": "UD"},
            {"time": "11:05-12:50", "course": "MAC 101", "room": "G02", "faculty": "AL"},
        ],
        "SAT": [
            {"time": "9:15-11:00", "course": "HUC 102", "room": "G02", "faculty": "RK"},
            {"time": "11:05-12:50", "course": "HUC 101", "room": "G02", "faculty": "SB"},
            {"time": "2:15-3:05", "course": "HUC 102", "room": "G02", "faculty": "RK"},
            {"time": "3:10-4:00", "course": "HUC 101", "room": "G02", "faculty": "SB"},
        ],
    },

    # ----------------------------------------------------------------------
    # B.TECH 3RD SEMESTER (SPLIT FOR FILTER OPTIONS)
    # ----------------------------------------------------------------------
    "B.Tech 3rd Sem CSE": {
        "MON": [
            {"time": "11:05-12:50", "course": "CSC 303", "room": "302", "faculty": "SCH"},
            {"time": "2:15-3:05", "course": "CSC 313", "room": "(201,202,207)", "faculty": "(MS/MD,IM)"},
        ],
        "TUE": [
            {"time": "9:15-11:00", "course": "CSC 301", "room": "G01", "faculty": "SMA"},
            {"time": "11:05-12:50", "course": "HUC 301", "room": "G01", "faculty": "SRC"},
            {"time": "2:15-3:05", "course": "HUC 301", "room": "G01", "faculty": "SRC"},
            {"time": "3:10-4:55", "course": "MAC 301", "room": "G01", "faculty": "(ND,SUM)"},
        ],
        "WED": [
            {"time": "10:10-11:00", "course": "CSC 302", "room": "G01", "faculty": "DB"},
            {"time": "11:05-4:05", "course": "MAC 301", "room": "G01", "faculty": "SUM"},
            {"time": "2:15-4:55", "course": "CSC 312", "room": "(201,202,207)", "faculty": "(SPK/NG,DB)"},
        ],
        "THU": [
            {"time": "10:10-12:50", "course": "CSC 311", "room": "(201,202,207)", "faculty": "(AD/DKN,MD)"},
            {"time": "2:15-4:00", "course": "CSC 302", "room": "302", "faculty": "DB"},
            {"time": "4:05-5:50", "course": "CSC 303", "room": "302", "faculty": "SCH"},
        ],
        "FRI": [
            {"time": "2:15-3:05", "course": "CSC 302", "room": "G02", "faculty": "DB"},
            {"time": "3:10-4:00", "course": "CSC 301", "room": "G02", "faculty": "SMA"},
        ],
        "SAT": [],
    },
    "B.Tech 3rd Sem ECE": {
        "MON": [
            {"time": "9:15-11:00", "course": "MAC 301", "room": "G01", "faculty": "(ND,SUM)"},
            {"time": "11:05-12:50", "course": "ECC 301", "room": "305", "faculty": "PC"},
        ],
        "TUE": [
            {"time": "10:10-11:00", "course": "HUC 301", "room": "G02", "faculty": "SRC"},
            {"time": "11:05-12:50", "course": "CSC 301", "room": "GO2", "faculty": "SMA"},
            {"time": "3:10-4:55", "course": "HUC 301", "room": "G02", "faculty": "SRC"},
        ],
        "WED": [
            {"time": "10:10-12:50", "course": "ECC 312", "room": "(203,G05)", "faculty": "RS"},
            {"time": "2:15-4:00", "course": "ECC 302", "room": "402", "faculty": "SPA"},
        ],
        "THU": [
            {"time": "11:05-12:50", "course": "ECC 301", "room": "302", "faculty": "PC"},
            {"time": "2:15-4:55", "course": "CSC 311", "room": "(201,207)", "faculty": "(AD/DKN,MD)"},
        ],
        "FRI": [
            {"time": "10:10-11:55", "course": "MAC 301", "room": "302", "faculty": "SUM"},
            {"time": "2:15-4:00", "course": "ECC 302", "room": "305", "faculty": "SPA"},
            {"time": "4:05-4:55", "course": "CSC 301", "room": "G02", "faculty": "SMA"},
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