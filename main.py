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
        return '-'.join(current_id.split('-')[:-1])
    else:
        return current_id

# -------- Ask user if in high school --------
clear()
print("Welcome! Let's figure out your scenario.\n")
print("1. I am in high school")
print("2. I am not in high school\n")

choice = input("Enter your choice: ").strip()

if choice == "1":
    import menu_hs as menu_library  # high school menu
elif choice == "2":
    import menu_adult as menu_library  # adult menu (full version)
else:
    print("Invalid choice. Defaulting to high school version.")
    import menu_hs as menu_library

# -------- MENU ENGINE --------
current = "0"
previous_menu = None  # track menu we came from

while True:
    clear()

    # Handle statements
    if current.startswith("statement:"):
        # Check if statement has a fixed next menu (format: statement:TEXT|ID)
        if "|" in current:
            text, fixed_next = current.split("|", 1)
            text = text.replace("statement:", "")
            print(text)
            input("\nPress Enter to continue...")
            current = fixed_next
        else:
            # Dynamic statement: return to previous menu
            text = current.replace("statement:", "")
            print(text)
            input("\nPress Enter to go back...")
            current = previous_menu
        continue

    # Normal menu
    menu_data = menu_library.menu[current]
    print(f"{menu_data['prompt']}\n")

    # Display options
    for key, (label, target) in menu_data["options"].items():
        print(f"{key}. {label}")

    # Back button
    if current != "0":
        # last option + 1
        last_num = max(int(k) for k in menu_data["options"].keys())
        back_num = str(last_num + 1)
        back_id = get_back_menu_id(current)
        print(f"{back_num}. Back")

    # Get user input
    user_choice = input("\nEnter your choice: ").strip()

    # Handle back button
    if current != "0" and user_choice == back_num:
        current = back_id
        continue

    # Handle normal option
    if user_choice in menu_data["options"]:
        target = menu_data["options"][user_choice][1]
        previous_menu = current
        if target == "quit":
            clear()
            break
        current = target
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")
