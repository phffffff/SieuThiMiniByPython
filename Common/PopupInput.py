import PySimpleGUI as sg

# Tạo layout cho popup
def getPopupInput():
    layout = [[sg.Text('Nhập mã xác nhận thành viên:'), sg.Input(key="-COMFIRM-")],
          [sg.Button('OK'), sg.Button('Cancel')]]


    return sg.Window('Xác nhận', layout)
