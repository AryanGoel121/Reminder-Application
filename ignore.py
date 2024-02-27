# -----------------------Previous code to read from a file--------------------
# import csv
# from datetime import datetime
# import notificationLogic as printNotif
# import time

# # Current Time & Date in a Specific Format
# def current_time():
#     return datetime.now().strftime(r"%H:%M")
# def current_date():
#     return datetime.now().strftime(r"%d-%m-%Y")
    
# # Accessing Data from the Tasks File
# myTasksFile = r'C:\Users\aryan\OneDrive\Desktop\Software Development\Reminder-Application\Tasks.csv'
# with open(myTasksFile, 'r') as file:
#     read_file = csv.DictReader(file)
#     myData = list(read_file)

# # Notify User about the task they have scheduled
# while True:
#     for task in myData:
#         if(task['Time'] == current_time() and task['Date'] == current_date()):
#             printNotif.displayNotif(task['Task To Do'])

#     time.sleep(60)