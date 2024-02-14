from plyer import notification

def displayNotif(data):
    notification.notify(
        title = "Task Reminder Application",
        message = data,
        app_icon = r"C:\Users\aryan\OneDrive\Desktop\Software Development\Reminder-Application\checklist.ico",
        timeout = 10
    )

if __name__ == '__main__':
    displayNotif("Hello World")