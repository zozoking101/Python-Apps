# To do list app
#Task Class
def print_instructions():
    print("\nEnter + to add tasks, - to remove tasks,")
    print("M to mark a task as completed, N to mark a task as uncompleted")
    print("F to filter tasks according: to All(A) Completed (C), Uncompleted (U), Due Date (D)")
    print("Enter Q to quit\n")
class Task():
    #The properties of the class
    def __init__(self, task_id, title, description, due_date, completed):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed  
    
class ToDoList(Task):
    #Creates instances
    def __init__(self):
        self.tasks = []
       
    def add_task(self):
        task_id = input('Task ID: ') 
        title = input('Title: ')
        description = input('Description: ')
        due_date = input('Due Date (YYMMDD): ')          
        completed = input('Completed (Y/N): ')  
        task = Task(task_id, title, description, due_date, completed)         
        self.tasks.append(task)
        print(f'\n{task.title} added!')
        print_instructions()
        
    def remove_task(self):
        task_id_check = input('Enter task ID to remove: ')
        for task in self.tasks:
            if task.task_id == task_id_check:
                self.tasks.remove(task)
                print(task.title,' removed!\n')
                print_instructions()
                return
        print(task_id_check," not found!")
        print_instructions()
                
    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = 'Y'
                print(task.title, 'completed!')
                print_instructions()
                return
        print('Task not found!')
        print_instructions()
        
    def mark_uncompleted(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = 'N'
                print(task.title, 'uncompleted!')
                print_instructions()
                return
        print('Task not found!')  
        print_instructions()
                 
    def display_all_tasks(self):
        for task in self.tasks:
            print("\nTask ID: ", task.task_id)
            print("Title: ", task.title,"\n")
            print('============================')
            print("Description: ", task.description)
            print("Due Date: ", task.due_date)
            print('============================\n')
            if task.completed == 'Y'or task.completed == 'y':
                print(f"{task.title} Completed: Yes\n")
            else:
                print(f"{task.title} Completed: No\n")
        print_instructions()
    
    def display_completed_tasks(self):
        for task in self.tasks:
            if task.completed == 'Y' or task.completed == 'y':
                print("\nCompleted Tasks: \n")
                print("Task ID: ", task.task_id)
                print("Title: ", task.title)
                print("Description: ", task.description)
                print("Due Date: ", task.due_date)
        print_instructions()
             
    def display_uncompleted_tasks(self):
        for task in self.tasks:
            if task.completed == 'N' or task.completed == 'n':
                print("\nUncompleted Tasks: \n")
                print("Task ID: ", task.task_id)
                print("Title: ", task.title)
                print("Description: ", task.description)
                print("Due Date: ", task.due_date)
        print_instructions()
                  
    def display_due_date(self):
        sorted_tasks = sorted(self.tasks, key = lambda t: t.due_date)
        print("\nTasks by Due Date: \n")
        for task in sorted_tasks:
            print("Task ID: ", task.task_id)
            print("Title: ", task.title)
            print("Description: ", task.description)
            print("Due Date: ", task.due_date)
        print_instructions()
                             
class App():
    def __init__(self):
        self.app_flow = ToDoList()
        self.app_running = True
        
    def app_start(self):
        self.app_flow = ToDoList()
        self.tasks = self.app_flow.tasks
        print("To Do List App\n")
        print("Enter + to add tasks, - to remove tasks,")
        print("M to mark a task as completed, N to mark a task as uncompleted")
        print("F to filter tasks according: to All(A) Completed (C), Uncompleted (U), Due Date (D)")
        print("Enter Q to quit\n")
        self.app_running = True
        
    def main(self):
        while self.app_running:
            self.app_start()
            while self.app_running:
                char = input(': ')
                if char == '+':
                    self.app_flow.add_task()
                elif char == '-':
                    self.app_flow.remove_task()
                elif char == "M" or char == 'm':
                    task_id = input('Enter Task ID to Mark Complete: ')
                    self.app_flow.mark_completed(task_id)
                elif char == "N" or char == 'n':
                    task_id = input('Enter Task ID to Mark Uncomplete: ')
                    self.app_flow.mark_uncompleted(task_id)
                elif char == 'Q' or char == 'q':
                    self.app_running = False
                elif char == 'f' or char == 'F':
                        filter = input('Filter tasks by A (All), C (Completed), U (Uncompleted), D (Due Date) : ')
                        if filter == 'A' or filter == 'a' or filter == '' or filter == ' ':
                            self.app_flow.display_all_tasks()
                        elif filter == 'C' or filter == 'c':
                            self.app_flow.display_completed_tasks()
                        elif filter == 'U' or filter == 'u':
                            self.app_flow.display_uncompleted_tasks()
                        elif filter == 'D' or filter == 'd':
                            self.app_flow.display_due_date()
                        elif filter == 'Q' or filter == 'q':
                            self.app_running = False
                        else:
                            print("Enter valid filter (A, C, U, D, Q): ")  
                            self.app_sart()                     
# Launch the app
if __name__ == '__main__':
    App().main()