todo_list = []
def add_task(task,status):
  new_task = {"task":task , "status":status}
  todo_list.append(new_task)
  print(f"Task '{task}' added to the to-do list.")

add_task("cut","Pending")

