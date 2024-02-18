def show_menu():
    print("\nGetting Started")
    know_how = {
        1: "\tSkip and start Program",
        2: "\tHow to run program⚙️",
        3: "\tFrequently asked questions📢",
        4: "\tLinks🔗",
        5: "\tModule Installation."
    }
    
    while True:
        for key, value in know_how.items():
            print(f"{key}: {value}")

        user_sel = input("Enter (1/2/3/4) for selection, or 'q' to quit: ")       
        try:
            if user_sel == 'q':
                break

            user_sel = int(user_sel)
            if user_sel == 1:
                break
            elif user_sel == 2:
                run()
            elif user_sel == 3:
                faq()
            elif user_sel == 4:
                links()
            elif user_sel == 5:
                module()
            else:
                print("Enter a valid option (1/2/3/4).")
        except ValueError:
            print("Invalid input. Please enter a number (1/2/3/4) or 'q' to quit.")

def run():
    run_path = "run.txt"
    try:
        with open(run_path, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"The file '{run_path}' was not found.")
    except IOError:
        print(f"An error occurred while reading the file '{run_path}'.")

def faq():
    faqs_path = "faqs.txt"
    try:
        with open(faqs_path, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"The file '{faqs_path}' was not found.")
    except IOError:
        print(f"An error occurred while reading the file '{faqs_path}'.")

def links():
    links_path = "links.txt"
    try:
        with open(links_path, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"The file '{links_path}' was not found.")
    except IOError:
        print(f"An error occurred while reading the file '{links_path}'.")

def module():
    module_path = "module.txt"
    try:
        with open(module_path, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"The file '{module_path}' was not found.")
    except IOError:
        print(f"An error occurred while reading the file '{module_path}'.")
