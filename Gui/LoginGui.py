import logging

import PySimpleGUI as sg
from Business.AccountBiz import AccountBiz
from Entity.AccountEntity import Account


class LoginGUI:
    def __init__(self):
        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layout = [[sg.Text('Đăng nhập', font=('Helvetica', 20), justification='center')],
                  [sg.Text('Tên đăng nhập:'), sg.InputText(key='username')],
                  [sg.Text('Mật khẩu:'), sg.InputText(key='password', password_char='*')],
                  [sg.Button('Đăng nhập', bind_return_key=True), sg.Button('Hủy bỏ')]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Đăng nhập', layout)

    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()
            if event in (sg.WINDOW_CLOSED, 'Hủy bỏ'):
                break
            elif event == 'Đăng nhập':
                # kiểm tra thông tin đăng nhập
                username = values['username']
                password = values['password']
                biz = AccountBiz()
                result = biz.login(username=username, password=password)
                # print(result)
                if result == None:
                    sg.popup('Đăng nhập thất baị')
                    return
                sg.popup('Đăng nhập thành công!', result)

        # đóng cửa sổ giao diện khi kết thúc
        self.window.close()

# if __name__ == '__main__':
#     gui = LoginGUI()
#     gui.run()
