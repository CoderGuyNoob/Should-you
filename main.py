# main.py

import os

# -------- Helper function to clear the screen --------
def clear():
    """Clear the terminal screen (cross-platform)."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\n" * 50)

# -------- Helper to go back in menu hierarchy --------
def get_back_menu_id(current_id):
    """Return the parent menu ID (strip last dash section)."""
    if '-' in current_id:
        return current_id.rsplit('-', 1)[0]
    return current_id

# -------- Choose version --------
clear()
print("Welcome! Let's figure out your scenario.\n")
print("1. I am in high school")
print("2. I am not in high school\n")

choice = input("Enter your choice: ").strip()

if choice == "1":
    import menu_hs as menu_library
elif choice == "2":
    import menu_adult as menu_library
else:
    print("Invalid choice. Defaulting to high school version.")
    import menu_hs as menu_library
    input("Press Enter to continue...")

# -------- MENU ENGINE --------
current = "0"
previous_menu = None

while True:
    clear()

    # -------- GLOBAL QUIT --------
    if current == "quit":
        print("Thanks for playing!")
        break

    # -------- STATEMENT HANDLER --------
    if current.startswith("statement:"):
        if "|" in current:
            text, fixed_next = current.split("|", 1)
            text = text.replace("statement:", "")
            print(text)
            input("\nPress Enter to continue...")
            current = fixed_next
        else:
            text = current.replace("statement:", "")
            print(text)
            input("\nPress Enter to go back...")
            current = previous_menu
        continue

    # -------- NORMAL MENU --------
    if current not in menu_library.menu:
        print("Error: menu not found:", current)
        break

    menu_data = menu_library.menu[current]
    print(menu_data["prompt"] + "\n")

    # Show options
    for key, (label, target) in menu_data["options"].items():
        print(f"{key}. {label}")

    # Back button
    back_num = None
    if current != "0":
        back_num = str(max(int(k) for k in menu_data["options"].keys()) + 1)
        print(f"{back_num}. Back")

    # Input
    user_choice = input("\nEnter your choice: ").strip()

    # Back handling
    if back_num and user_choice == back_num:
        current = get_back_menu_id(current)
        continue

    # Normal option
    if user_choice in menu_data["options"]:
        target = menu_data["options"][user_choice][1]
        previous_menu = current
        current = target
    else:
        print("Invalid option.")
        input("Press Enter to continue...")
