import logging

import PySimpleGUI as sg

from Business.AccountsBiz import AccountsBiz

from Gui.HomeGUI import HomeGUI

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
                result = AccountsBiz().login(username=username, password=password)
                if result["flag"]:
                    user = {"id_account":result["data"][0],"role":result["data"][3],"status":result["data"][4]}
                    homeGUI = HomeGUI(user=user)
                    homeGUI.run()
                else:
                    sg.popup(result["data"])


        # đóng cửa sổ giao diện khi kết thúc
        self.window.close()

# if __name__ == '__main__':
#     gui = LoginGUI()
#     gui.run()