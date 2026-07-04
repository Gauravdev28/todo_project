import json

try :
    with open("todo.json" , "r") as file :
        todo = json.load(file)
except (FileNotFoundError , json.JSONDecodeError) :
    todo = []

def save_todo() :
    with open("todo.json" , "w") as file :
        json.dump(todo , file , indent=4)

# Printing Menu 
while True :

    print("\n========== TO DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Mark Task Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    # Add Task 
    if choice == "1" :
        
        task = input("Enter Your Task :")

        new_task = {
            "task" : task ,
            "status" : "Pending" ,
        }

        todo.append(new_task)
        save_todo() 

        print("Task Added Successfull")


    # View Task
    if choice == "2" :

        if len(todo) == 0 :
            print("No task Found") 

        else :
            print("\n========== TASK LIST ==========")

            for i , task in enumerate(todo , start=1) :

                print(f"{i}. {task['task']}")
                print(f"Status : {task['status']}")
                print("-"*40)

    
    # Search Task
    if choice == "3" :

        search = input("Enter Task Name :")
        found = False

        for task in todo :

            if task["task"].lower() == search.lower() :

                print("Task Found")
                print(f"Task :{task['task']}")
                print(f"Status : {task['status']}")


            found = True 
            break

        if not found :
            print("No Task Found with this name ")


    # Mark Task 
    if choice == "4" :

        complete = input("Enter Task Name :") 
        found = False 

        for task in todo :
            
            if task["task"].lower() == complete.lower() :
                task["status"] = "Complete"

                save_todo()
                print("✅ Task Marked as Completed!")

                found = True
                break

        if not found:
            print("❌ Task Not Found.")


    # Delete Task 
    if choice == "5" :

        delete = input("Enter Task Name :") 
        found = False

        for task in todo :
            
            if task["task"].lower() == delete.lower():
                todo.remove()

                save_todo()

                print("Task Deleted")

                found = True
                break

        if not found:
            print("Task Not Found")

    
    # Exit Program 
    if choice == "6" :
        print("Exiting Program")
        break

else:
    print("❌ Invalid Choice! Please Enter a Number Between 1 and 6.")



    