import os

# -------- Helper function to clear the screen --------
def clear():
    """Clear the terminal screen (cross-platform)."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\n" * 50)  # fallback

# -------- MENU DATA --------
# Each menu now has:
#   "prompt" -> the question to ask
#   "options" -> a dictionary of options (label, target)
menu = {
    "0": {
        "prompt": "Welcome! Where do you want to go?",
        "options": {
            "1": ("Go to settings", "settings"),
            "2": ("Quit program", "quit")
        }
    },
    "settings": {
        "prompt": "You are in settings. Where do you want to go next?",
        "options": {
            "1": ("Back to main menu", "0"),
            "2": ("Quit program", "quit")
        }
    }
}

# -------- MENU ENGINE --------
current = "0"

while True:
    clear()

    # Print the menu prompt
    print(f"{menu[current]['prompt']}\n")

    # Display the options
    for key, (label, target) in menu[current]["options"].items():
        print(f"{key}. {label}")

    # Get user input
    choice = input("\nEnter your choice: ").strip()

    # Validate input and move to next menu
    if choice in menu[current]["options"]:
        current = menu[current]["options"][choice][1]  # move to target
        if current == "quit":
            clear()
            break
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")