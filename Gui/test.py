import PySimpleGUI as sg

layout = [[sg.Text("Hello, World!")],
[sg.Frame("Options", [[sg.Checkbox("Option 1"),
sg.Checkbox("Option 2")]])],
[sg.Button("OK"), sg.Button("Cancel")]]

window = sg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == "OK":
# do something
     break
    elif event in (sg.WINDOW_CLOSED, "Cancel"):
     break

window.close()