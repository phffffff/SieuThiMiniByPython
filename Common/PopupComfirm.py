import PySimpleGUI as sg

def getPopupComfirm():
    layout = [[sg.Text('Bạn có muốn tiếp tục không?')],
            [sg.OK(), sg.Cancel()]]

    return sg.Window('Xác nhận', layout)