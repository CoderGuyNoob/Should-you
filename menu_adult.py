# menu_adult.py
# Full menu with work, hooking up, and adult scenarios

menu = {
    "0": {
        "prompt": "Do you want help deciding whether to tell your crush you like them?",
        "options": {
            "1": ("Yes, continue", "0-1"),
            "2": ("No, quit", "quit")
        }
    },

    "0-1": {
        "prompt": "Is your crush seeing someone?",
        "options": {
            "1": ("Yes", "0-1-yes"),
            "2": ("No", "0-1-no"),
            "3": ("I don't know", "statement:Find out first")
        }
    },

    # CRUSH NOT SEEING SOMEONE
    "0-1-no": {
        "prompt": "How do you know your crush?",
        "options": {
            "1": ("In person", "0-1-no-inperson"),
            "2": ("Online", "0-1-no-online"),
            "3": ("Through work", "0-1-no-work")
        }
    },

    # IN-PERSON PATH
    "0-1-no-inperson": {
        "prompt": "Where did you meet your crush?",
        "options": {
            "1": ("Through friends", "0-1-no-inperson-friends"),
            "2": ("Through school", "0-1-no-inperson-school"),
            "3": ("Third space (coffee shop, library, etc.)", "statement:Tell them, it's low risk")
        }
    },

    # Friends sub-path
    "0-1-no-inperson-friends": {
        "prompt": "Are you friends with your crush?",
        "options": {
            "1": ("Yes", "0-1-no-inperson-friends-yes"),
            "2": ("No", "0-1-no-inperson-friends-no")
        }
    },

    "0-1-no-inperson-friends-yes": {
        "prompt": "Are you in a friend group with them?",
        "options": {
            "1": ("Yes", "statement:Tread carefully, could be awkward but tell them if you want clarity"),
            "2": ("No", "statement:You should tell them, expect some awkwardness")
        }
    },

    "0-1-no-inperson-friends-no": {
        "prompt": "Do you and your crush have a mutual friend?",
        "options": {
            "1": ("Yes", "0-1-no-inperson-friends-yes"),  # shared menu
            "2": ("No, they are a friend’s sibling", "0-1-no-inperson-friends-sibling")
        }
    },

    "0-1-no-inperson-friends-sibling": {
        "prompt": "Do you like them just because they're your friend's sibling?",
        "options": {
            "1": ("Yes", "statement:Don't tell them, you'll phase out of it"),
            "2": ("No", "statement:Tell them, but be prepared for awkwardness with your friend")
        }
    },

    # School path
    "0-1-no-inperson-school": {
        "prompt": "Do you see your crush often at school?",
        "options": {
            "1": ("Yes", "0-1-no-inperson-school-yes"),
            "2": ("No", "statement:Tell them, nothing to risk")
        }
    },

    "0-1-no-inperson-school-yes": {
        "prompt": "Do you like them because of proximity or genuinely?",
        "options": {
            "1": ("Only because of forced proximity", "statement:Don't tell them"),
            "2": ("Genuine feelings", "statement:Tell them, best case you succeed, worst case awkward")
        }
    },

    # ONLINE PATH
    "0-1-no-online": {
        "prompt": "Is your crush a celebrity?",
        "options": {
            "1": ("Yes", "statement:You can tell them, but they won't notice"),
            "2": ("No", "0-1-no-online-real")
        }
    },

    "0-1-no-online-real": {
        "prompt": "Did you meet them on a dating app?",
        "options": {
            "1": ("Yes", "statement:Tell them, they probably know"),
            "2": ("No", "0-1-no-online-meet")
        }
    },

    "0-1-no-online-meet": {
        "prompt": "Have you met them in real life?",
        "options": {
            "1": ("Yes", "statement:Tell them"),
            "2": ("No", "statement:You can tell them, but be prepared that reality may differ")
        }
    },

    # WORK PATH
    "0-1-no-work": {
        "prompt": "Do you fear being fired if you tell them?",
        "options": {
            "1": ("Yes", "statement:Don't tell them"),
            "2": ("No", "statement:You could tell them, proceed carefully")
        }
    },

    # CRUSH IS SEEING SOMEONE
    "0-1-yes": {
        "prompt": "How is your crush involved with someone?",
        "options": {
            "1": ("Hooking up", "0-1-yes-hookup"),
            "2": ("Casually dating", "0-1-yes-casual"),
            "3": ("In a serious relationship", "statement:Don't tell them, homewrecker")
        }
    },

    # CASUAL dating path
    "0-1-yes-casual": {
        "prompt": "Is it actually casual and with one person?",
        "options": {
            "1": ("Yes", "statement:Proceed with caution, might work"),
            "2": ("No", "statement:Don't tell them, avoid complications")
        }
    },

    # HOOK-UP path
    "0-1-yes-hookup": {
        "prompt": "Are they in a situationship? Who controls it?",
        "options": {
            "1": ("They are being dragged along", "statement:Tell them, but likely won't reciprocate"),
            "2": ("They are dragging the other person", "statement:Don't tell them")
        }
    }
}
