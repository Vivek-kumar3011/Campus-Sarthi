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
        "MON": [],
        "TUE": [
            {"time": "11:05-12:50", "course": "CSC 502", "room": "302", "faculty": "OB"},
            {"time": "2:15-4:55", "course": "CSC 511", "room": "(201,202,207)", "faculty": "(NG/SS,SHI)"},
        ],
        "WED": [ 
            {"time": "9:15-11:00", "course": "CSC 501", "room": "302", "faculty": "SHI"},
            {"time": "2:15-4:00", "course": "ECC 502", "room": "G02", "faculty": "DN"}
        ],
        "THU": [ 
            {"time": "10:10-12:50", "course": "CSC 591 (PROJECT-IA)", "room": "", "faculty": ""},
        ],
        "FRI": [ 
            {"time": "9:15-11:55", "course": "ECC 512", "room": "(201,202,207)", "faculty": "(DPC/BS/SHB,RB)"},
            {"time": "12:00-12:50", "course": "ECC 502", "room": "302", "faculty": "DN"},
            {"time": "2:15-4:00", "course": "CSC 502", "room": "302", "faculty": "OB"},
            {"time": "4:05-5:50", "course": "CSC 501", "room": "302", "faculty": "SHI"},
        ],
        "SAT": [
            {"time": "9:15-11:00", "course": "HUC 501", "room": "302", "faculty": "FU"},
            {"time": "11:05-12:50", "course": "ECC 511", "room": "302", "faculty": "DD"},
            {"time": "2:15-3:05", "course": "CSC 501", "room": "302", "faculty": "FU"},
            {"time": "3:10-4:00", "course": "CSC 511", "room": "302", "faculty": "DD"},
        ],
    },
    "B.Tech 5th Sem ECE": {
        "MON": [],
        "TUE": [
            {"time": "11:05-12:50", "course": "CSC 501", "room": "402", "faculty": "PC"},
            {"time": "2:15-4:55", "course": "ECC 511", "room": "G05", "faculty": "(AG/BS,RB)"},
        ],
        "WED": [ 
            {"time": "9:15-11:00", "course": "EEC 501", "room": "305", "faculty": "ARA"},
            {"time": "11:05-12:50", "course": "ECC 502", "room": "305", "faculty": "DN"},
            {"time": "2:15-4:00", "course": "ECC 501", "room": "305", "faculty": "PC"}
        ],
        "THU": [ 
            {"time": "10:10-12:50", "course": "ECC 591 (PROJECT-IA)", "room": "", "faculty": ""},
        ],
        "FRI": [ 
            {"time": "9:15-11:00", "course": "EEC 501", "room": "402", "faculty": "ARA"},
            {"time": "11:05-11:55", "course": "ECC 502", "room": "305", "faculty": "DN"},
            {"time": "2:15-4:55", "course": "ECC 512", "room": "(201,207)", "faculty": "(AG/DPC,DN)"},
        ],
        "SAT": [
            {"time": "9:15-11:00", "course": "HUC 511", "room": "305", "faculty": "DD"},
            {"time": "11:05-12:50", "course": "ECC 501", "room": "305", "faculty": "FU"},
            {"time": "2:15-3:05", "course": "CSC 511", "room": "305", "faculty": "DD"},
            {"time": "3:10-4:00", "course": "CSC 501", "room": "305", "faculty": "FU"},
        ],
    },

    # ----------------------------------------------------------------------
    # B.TECH 7TH SEMESTER
    # ----------------------------------------------------------------------
    "B.Tech 7th Sem CSE": {
        "MON": [ 
            {"time": "10:10-12:50", "course": "CSC 711", "room": "(201,202,207)", "faculty": "(MS/MD,OB)"},
            {"time": "2:15-4:00", "course": "CSE 722", "room": "G01", "faculty": "DB"},
            {"time": "4:05-5:50", "course": "CSE 730", "room": "G01", "faculty": "SP"},
        ],
        "TUE": [
            {"time": "9:15-11:00", "course": "CSE 737/CSE 740", "room": "302/402", "faculty": "SHI/IM"},
            {"time": "11:05-12:50", "course": "CSE 733", "room": "305", "faculty": "SCH"},
            {"time": "2:15-3:05", "course": "CSC 701", "room": "G02", "faculty": "OB"},
            {"time": "3:10-4:00", "course": "CSE 722", "room": "305", "faculty": "DB"},
            {"time": "4:05-5:50", "course": "CSE 736", "room": "302", "faculty": "BB"},
        ],
        "WED": [ 
            {"time": "11:05-12:50", "course": "CSC 701", "room": "302", "faculty": "OB"},
            {"time": "2:15-4:00", "course": "CSC 702", "room": "302", "faculty": "IM"},
            {"time": "4:05-4:55", "course": "CSE 730", "room": "302", "faculty": "SP"},
            {"time": "5:00-5:50", "course": "CSE 733", "room": "302", "faculty": "SCH"},
        ],
        "THU": [
            {"time": "10:10-12:50", "course": "CSC 791(PROJECT-IIA)", "room": "", "faculty": ""},
            {"time": "2:15-4:55", "course": "CSC 791(PROJECT-IIA)", "room": "", "faculty": ""},
        ],
        "FRI": [ 
            {"time": "9:15-10:05", "course": "CSE 736", "room": "302", "faculty": "BB"},
            {"time": "10:10-11:00", "course": "CSE 737", "room": "305", "faculty": "SHI"},
            {"time": "12:00-12:50", "course": "CSE 740", "room": "305", "faculty": "IM"},
            {"time": "4:05-4:55", "course": "CSC 702", "room": "G01", "faculty": "IM"},     
        ],
        "SAT": [],
    },
    "B.Tech 7th Sem ECE": {
        "MON": [ 
            {"time": "9:15-11:00", "course": "ECC 702", "room": "G02", "faculty": "ARA"},
            {"time": "11:05-11:00", "course": "ECC 701", "room": "G02", "faculty": "RS"},
            {"time": "2:15-3:05", "course": "ECE 732", "room": "305", "faculty": "RS"},
            {"time": "3:10-4:55", "course": "ECE 733", "room": "305", "faculty": "SPA"},
        ],
        "TUE": [
            {"time": "10:10-11:00", "course": "ECE 728", "room": "305", "faculty": "RB"},
            {"time": "2:15-3:05", "course": "ECC 701", "room": "305", "faculty": "RS"},
            {"time": "3:10-4:00", "course": "ECE 733", "room": "402", "faculty": "SPA"},
        ],
        "WED": [ 
            {"time": "10:10-12:50", "course": "ECC 791(PROJECT-IIA)", "room": "", "faculty": ""},
            {"time": "2:15-4:55", "course": "ECC 791(PROJECT-IIA)", "room": "", "faculty": ""},
        ],
        "THU": [
            {"time": "9:15-11:00", "course": "ECC 702", "room": "305", "faculty": "ARA"},
            {"time": "11:05-12:50", "course": "ECE 728", "room": "305", "faculty": "RB"},
            {"time": "2:15-4:55", "course": "ECC 711", "room": "202", "faculty": "(XXX,SPA)"},
        ],
        "FRI": [ 
            {"time": "11:05-12:50", "course": "ECE 732", "room": "402", "faculty": "RS"},
            {"time": "2:15-4:55", "course": "ECC 712", "room": "202", "faculty": "(SJP,ARA)"},
        ],
        "SAT": [],
    },
    
}


# Faculty and Code Lists
FACULTY_LIST = {
    "IM": "Dr.Imon Mukherjee", "SHI": "Dr.SK Hafizul Islam", "SP": "Dr.Sanjoy Pratihar", "OB": "Dr.Oishila Bandyopadhya",
    "SCH": "Dr.Sanjay Chatterji", "DB": "Dr.Debasish Bera", "ARA": "Dr.Amit Ranjan Azad", "BK": "Dr.Bapi Kar",
    "UD": "Dr.Uma Das", "DN": "Dr. Dalia Nandi", "AL": "Dr.Anirban Lakshman", "RS": "Dr.Rinky Sha",
    "PC": "Dr.Pratik Chakraborty", "BB": "Dr.Bhaskar Biswas", "SUM": "Dr.Sudeshna Mondal", "SPA": "Dr.Soumen Pandit",
}

GUEST_FACULTY_LIST = {
    "DD": "Dr.Debasish Dutta", "FU": "Dr.Furquan Uddin", "RK": "Dr.Rasheed K", "SAS": "Mr.Sabyasachi Sen",
    "SMA": "Mr.Sukanta Mazumdar", "MD": "Ms.Mukta Debnath", "SB": "Mrs.Shweta Basu", "SRC": "Ms.Sreyoshi Roy Chowdhury",
}

Research_Scholar = {
    "AD": "Arijit Das", "AG": "Abhishek Ghosh", "AP": "Amritesu Pal", "AS": "Atashi Saha",
    "BS": "Bijaylakshmi Singh", "DKN": "Dilkashan Neyaz", "DPC": "Debarpita Paul Choudhury", "DS": "Debmani Saha",
    "JT": "Jaob Tauro", "MD": "Madhuchhanda Dasgupta", "MS": "Mou Sarkar", "ND": "Nikita Dhar",
    "NG": "Nilkantha Garain", "PB": "Pritam Biswas", "SHB": "Shikha Biswas", "SJM": "Suvojit Mukhopadhyay",
    "SJP": "Subhajit Paul", "SPK": "Saptaparna Kundu", "SR": "Sabnur Rahaman", "SS": "Suman Som",
}

ALL_DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]