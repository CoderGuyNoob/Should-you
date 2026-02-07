# -------- MENU DATA --------
menu = {
    "main": {
        "1": ("Go to settings", "settings"),
        "2": ("Open tools menu", "tools"),
        "3": ("Exit program", "quit")
    },
    "settings": {
        "1": ("Audio settings", "audio"),
        "2": ("Video settings", "video"),
        "3": ("Back to main menu", "main")
    },
    "tools": {
        "1": ("Calculator", "calculator"),
        "2": ("Back to main menu", "main")
    },
    "audio": {
        "1": ("Back to settings", "settings")
    },
    "video": {
        "1": ("Back to settings", "settings")
    },
    "calculator": {
        "1": ("Back to tools", "tools")
    }
}

# -------- MENU ENGINE --------
current = "main"

while True:
    

    # Display all options dynamically
    for key, (label, target) in menu[current].items():
        print(f"{key}. {label}")

    # Get user input
    choice = input("Choose: ").strip()

    # Validate input and move to next menu
    if choice in menu[current]:
        current = menu[current][choice][1]  # use the target
        if current == "quit":
            break
    else:
        print("Invalid option. Please try again.")