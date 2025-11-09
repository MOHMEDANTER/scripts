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
def modify(modify_num):
  pen = "Done"
  try:
    modified = int(modify_num) - 1
    if 0 <= modified < len(todo_list):
      if todo_list[modified]['status'] == "Pending":
        todo_list[modified]['status'] = pen
        print("the task modified")
      else:
        print(f"Task {modified + 1} is not pending.")
    else:
      print("Invalid task number")
  except ValueError:
    print("Invalid input. Please enter a valid number.")

def delet(delet_num):
  deleted = int(delet_num) - 1
  if 0<=deleted<len(todo_list):
    deleted_task = todo_list.pop(deleted)
    print(f"The metion ( {delet_num} ) is ( {deleted_task['task']} ) and the status was ( {deleted_task["status"]} ) already deleted .")
  else:
      print("Invalid task number")
