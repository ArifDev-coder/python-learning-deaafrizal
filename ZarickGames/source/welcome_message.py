import socket

pc_name = socket.gethostname()

def welcome_message(name):
    shape = "="
    shape_title = shape * 5
    pc_name_title = f"{shape_title} Hello {name.capitalize()}({pc_name}) Welcome to Zarick Games! {shape_title}"
    long_title = len(pc_name_title)

    print(shape * long_title)
    print(pc_name_title)
    print(shape * long_title)