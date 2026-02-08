import os
import library
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
    print(f"{library.menu[current]['prompt']}\n")

    # Show options
    for key, (label, target) in library.menu[current]["options"].items():
        print(f"{key}. {label}")

    # Back button
    if current != "0":
        last_num = max(int(k) for k in library.menu[current]["options"].keys())
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
    if choice in library.menu[current]["options"]:
        target = library.menu[current]["options"][choice][1]
        previous_menu = current  # remember where we came from
        if target == "quit":
            clear()
            break
        current = target
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")
