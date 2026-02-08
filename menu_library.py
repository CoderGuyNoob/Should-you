menu = {
    "0": {
        "prompt": "Welcome to should I tell my crush I like them? What do you want to do?",
        "options": {
            "1": ("Continue", "0-1"),
            "2": ("Quit program", "quit")
        }
    },
    "0-1": {
        "prompt": "Is your crush seeing someone?",
        "options": {
            "1": ("Yes","0-1-1"),  # dynamic
            "2": ("No", "0-1-2"),
            "3": ("Not sure", "statement:Find out.")  # dynamic
        }
    },
    "0-1-2": {
        "prompt": "How do you know your crush?",
        "options": {
            "1": ("In person.", "0-1-2-1"),
            "2": ("Online.", "0-1-2-2")
        }
    }
}