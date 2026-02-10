def show_help():
    print("\n" + "="*70)
    print("Here's how this CLI works")
    print("\nOn each page, it tells you things you can do")
    print("For example:")
    print('\n"Enter 1 to rename task')
    print(' Enter 2 to change task priority"')
    print("\nYou will then enter the number corresponding to the thing you want to do.")
    print("\nLISTS")
    print("Lists are both numbered and named. You can access any of the lists either way.")
    print("Lists can be renamed once you enter the list")
    print("\nTASKS")
    print("Tasks are named, numbered, and prioritized. Once a list is selected, a specific")
    print("task can be selected and the previous signifiers can be edited.")
    print("\nFurther questions?")
    print("Email me at taskmanagercreator@gmail.com")
    print("="*70)


def view_list(list_data):
    while True:
        print(f"\n--- {list_data['name']} ---")
        
        if list_data['items']:
            for i, task in enumerate(list_data['items'], 1):
                priority = task.get('priority', 'medium')
                print(f"  {i}. [{priority.upper()}] {task['name']}")
        else:
            print("  (No tasks yet)")
        
        print("\nOptions:")
        print("1. Add new task")
        print("2. Edit task")
        print("3. Delete task")
        print("4. Rename list")
        print("5. Back to main menu")
        
        choice = input("\nWhat would you like to do: ").strip()
        
        if choice == "1":
            add_task(list_data)
        elif choice == "2":
            edit_task(list_data)
        elif choice == "3":
            delete_task(list_data)
        elif choice == "4":
            rename_list(list_data)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")


def add_task(list_data):
    task_name = input("\nEnter task name: ").strip()
    
    if not task_name:
        print("Task name cannot be empty.")
        return
    
    print("\nSelect priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    
    priority_choice = input("Enter priority (1-3): ").strip()
    
    priority_map = {"1": "low", "2": "medium", "3": "high"}
    priority = priority_map.get(priority_choice, "medium")
    
    list_data['items'].append({"name": task_name, "priority": priority})
    print(f"\nTask '{task_name}' added with {priority} priority!")


def edit_task(list_data):
    if not list_data['items']:
        print("\nNo tasks to edit.")
        return
    
    task_num = input("\nEnter task number to edit: ").strip()
    
    if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(list_data['items']):
        print("Invalid task number.")
        return
    
    task_index = int(task_num) - 1
    task = list_data['items'][task_index]
    
    print(f"\nEditing: {task['name']} [Priority: {task.get('priority', 'medium')}]")
    print("\n1. Rename task")
    print("2. Change priority")
    
    choice = input("What would you like to do: ").strip()
    
    if choice == "1":
        new_name = input("Enter new task name: ").strip()
        if new_name:
            task['name'] = new_name
            print("Task renamed!")
    elif choice == "2":
        print("\nSelect new priority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        
        priority_choice = input("Enter priority (1-3): ").strip()
        priority_map = {"1": "low", "2": "medium", "3": "high"}
        task['priority'] = priority_map.get(priority_choice, "medium")
        print(f"Priority updated to {task['priority']}!")


def delete_task(list_data):
    if not list_data['items']:
        print("\nNo tasks to delete.")
        return
    
    task_num = input("\nEnter task number to delete: ").strip()
    
    if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(list_data['items']):
        print("Invalid task number.")
        return
    
    task_index = int(task_num) - 1
    task_name = list_data['items'][task_index]['name']
    
    confirm = input(f"\nAre you sure you want to delete '{task_name}'? (yes/no): ").strip().lower()
    
    if confirm in ["yes", "y"]:
        removed_task = list_data['items'].pop(task_index)
        print(f"\nTask '{removed_task['name']}' deleted!")
    else:
        print("\nDeletion cancelled.")


def rename_list(list_data):
    new_name = input("\nEnter new list name: ").strip()
    if new_name:
        list_data['name'] = new_name
        print("List renamed!")


def create_new_list(lists):
    list_name = input("\nEnter new list name: ").strip()
    
    if not list_name:
        print("List name cannot be empty.")
        return
    
    next_num = max(lists.keys()) + 1 if lists else 1
    
    lists[next_num] = {
        "name": list_name,
        "items": []
    }
    
    print(f"\nList '{list_name}' created!")


def delete_list(lists):
    if not lists:
        print("\nNo lists to delete.")
        return
    
    list_num = input("\nEnter list number to delete: ").strip()
    
    if not list_num.isdigit() or int(list_num) not in lists:
        print("Invalid list number.")
        return
    
    list_num = int(list_num)
    list_name = lists[list_num]['name']
    task_count = len(lists[list_num]['items'])
    
    print(f"\n⚠️  WARNING: You are about to delete '{list_name}'")
    if task_count > 0:
        print(f"This list contains {task_count} task(s) that will be permanently lost.")
    print("This action cannot be undone.")
    
    confirm = input("\nAre you sure you want to delete this list? (yes/no): ").strip().lower()
    
    if confirm in ["yes", "y"]:
        removed_list = lists.pop(list_num)
        print(f"\nList '{removed_list['name']}' deleted!")
    else:
        print("\nDeletion cancelled.")


def main():
    lists = {
        1: {
            "name": "Grocery List", 
            "items": [
                {"name": "Milk", "priority": "high"},
                {"name": "Bread", "priority": "medium"},
                {"name": "Eggs", "priority": "high"},
                {"name": "Cheese", "priority": "low"}
            ]
        },
        2: {
            "name": "Biology test prep", 
            "items": [
                {"name": "Review chapters 5-7", "priority": "high"},
                {"name": "Practice questions", "priority": "medium"},
                {"name": "Study cell division", "priority": "high"}
            ]
        },
        3: {
            "name": "Internship Applications", 
            "items": [
                {"name": "Update resume", "priority": "high"},
                {"name": "Write cover letter", "priority": "medium"},
                {"name": "Research companies", "priority": "low"}
            ]
        }
    }
    
    while True:
        print("\n" + "="*40)
        print("YOUR LISTS:")
        for num, list_data in lists.items():
            print(f"{num}. {list_data['name']}")
        
        print("\nEnter the number of the list you want to access")
        print('Type "new" to create a new list')
        print('Type "delete" to delete a list')
        print('Type "help" to open a help menu')
        print('Type "quit" or "exit" to leave')
        
        choice = input("\nWhat do you want to access: ").strip().lower()
        
        if choice == "help":
            show_help()
        
        elif choice == "new":
            create_new_list(lists)
        
        elif choice == "delete":
            delete_list(lists)
            
        elif choice in ["quit", "exit"]:
            print("Goodbye!")
            break
            
        elif choice.isdigit() and int(choice) in lists:
            num = int(choice)
            view_list(lists[num])
                
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()