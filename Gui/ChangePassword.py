import PySimpleGUI as sg
from Business.AccountsBiz import AccountsBiz
from Common.PopupComfirm import getPopupComfirm

class ChangePasswordGui:
    def __init__(self, id):

        self.id= id

        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layout1=  [[sg.Text('Change Password',font="blod",size=50,justification="center")],
                      [sg.Text('Old Password:',size=15), sg.Input(key='old_pass')],
                      [sg.Text('New Password:', size=15), sg.Input(key='new_pass')],
                      [sg.Text('Re-Password:',size=15), sg.Input(key='re_pass')],

                      [sg.Button('Update',size=62)]]



        # tạo cửa sổ giao diện
        self.window = sg.Window('Change Password', layout1)

    def empty(self):
        self.window['old_pass'].update('')
        self.window['new_pass'].update('')
        self.window['re_pass'].update('')

    def run(self):
            # xử lý sự kiện cho cửa sổ giao diện
            while True:
                event, values = self.window.read()

                if event == "Exit" or event == sg.WINDOW_CLOSED:
                    break
                elif event == 'Update':
                    old_pass = values['old_pass']
                    new_pass = values['new_pass']
                    re_pass = values['re_pass']

                    rs = AccountsBiz().find_accounts_with_cond(key="id",value=self.id)
                    if rs:
                        if rs[2] == old_pass and new_pass == re_pass:
                            update = {'password':new_pass}
                            upt = AccountsBiz().update_accounts(accounts=update,cond={"id":self.id})
                            if upt != -1:
                                sg.popup("Change Success!")
                            else:
                                sg.popup("Something err with server!")
                        else:
                            sg.popup("Input Invalid!")
                    else:
                        sg.popup("Err with account!")