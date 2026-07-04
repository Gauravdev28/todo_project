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
    print("4. Update Task")
    print("5. Mark Task Completed")
    print("6. Delete Task")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    # Add Task 
    if choice == "1" :
        
        task = input("Enter Your Task :")

        new_task = {
            "task" : task ,
            "status" : "Pending" ,
        }

        todo.append[new_task]
        save_todo() 

        print("Task Added Successfull")


    # View Task
    if choice == "2" :

        if len(todo) == 0 :
            print("No task Found") 

        else :
            print("\n========== TASK LIST ==========")

            for i in 
