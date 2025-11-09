todo_list = []
def add_task(task,status):
  new_task = {"task":task , "status":status}
  todo_list.append(new_task)
  print(f"Task '{task}' added to the to-do list.")

add_task("cut","Pending")

def view():
  try:
    if todo_list:
      for idx,item in enumerate(todo_list,1):
        task = item['task']
        status = item['status']
      # for i,ii in enumerate(todo_list,1):
        print(idx,item)
    else:
      print("No tasks in the to-do list.")

  except:
    print("Invalid input. Please enter a valid number.")


  print(f"( {idx} )::::( {task} )::::( {status} )")

  print("---------------------------------------\n")

