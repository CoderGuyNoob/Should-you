import os

# -------- Helper function to clear the screen --------
def clear():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\n" * 50)

# -------- Helper to go back in menu hierarchy --------
def get_back_menu_id(current_id):
    if '-' in current_id:
        return '-'.join(current_id.split('-')[:-1])
    else:
        return current_id

# -------- MENU DATA --------
# We can mark statements as:
# "statement:<text>" -> dynamic (goes back to previous menu)
# "statement:<text>|<fixed_next_id>" -> fixed (goes to fixed menu)
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

# -------- MENU ENGINE --------
current = "0"
previous_menu = None  # track menu we came from

while True:
    clear()

    # Handle statements
    if current.startswith("statement:"):
        # Check if there is a fixed next menu
        if "|" in current:
            text, fixed_next = current.split("|")
            text = text.replace("statement:", "")
            print(text)
            input("\nPress Enter to continue...")
            current = fixed_next  # go to fixed menu
        else:
            # dynamic statement
            text = current.replace("statement:", "")
            print(text)
            input("\nPress Enter to go back...")
            current = previous_menu
        continue

    # Normal menu
    print(f"{menu[current]['prompt']}\n")

    # Show options
    for key, (label, target) in menu[current]["options"].items():
        print(f"{key}. {label}")

    # Back button
    if current != "0":
        last_num = max(int(k) for k in menu[current]["options"].keys())
        back_num = str(last_num + 1)
        back_id = get_back_menu_id(current)
        print(f"{back_num}. Back")

    # Get user input
    choice = input("\nEnter your choice: ").strip()

    # Back button handling
    if current != "0" and choice == back_num:
        current = back_id
        continue

    # Normal option handling
    if choice in menu[current]["options"]:
        target = menu[current]["options"][choice][1]
        previous_menu = current  # remember where we came from
        if target == "quit":
            clear()
            break
        current = target
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")
