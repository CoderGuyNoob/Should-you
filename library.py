menu = {
    "0": {
        "prompt": "Welcome to should I tell my crush I like them? What do you want to do?",
        "options": {
            "1": ("Continue", "0-1"),
            "2": ("Quit program", "quit")
        }
    },
    "0-1": {
        "prompt": "Is your crush dating someone?",
        "options": {
            "1": ("Yes", "statement:Oh no! Maybe wait a bit."),  # dynamic
            "2": ("No", "0-1-1")
        }
    },
    "0-1-1": {
        "prompt": "Do you want to tell them you like them?",
        "options": {
            "1": ("Yes", "statement:Good luck! Be confident.|0"),  # fixed next menu = main menu
            "2": ("No", "statement:Maybe wait until you’re sure.")   # dynamic
        }
    }
}