

import PySimpleGUI as sg
from Business.AccountsBiz import AccountsBiz
from DataAccess.AccountsDal import AccountsDal
from Common.PopupComfirm import getPopupComfirm
from Entity.AccountsEntity import Accounts


class AccountsGui:


    def __init__(self):

        self.Headings = ['ID', 'User name', 'password', 'roleId', 'status']

        self.lstAccounts = AccountsBiz().get_all_accounts()
        self.result = []

        for item in self.lstAccounts:
            item = list(item)
            item[0] = AccountsBiz().to_str_id(id=item[0])

            self.result.append(item)
        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('DANH SÁCH TÀI KHOẢN',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['ID','USERNAME','PASSWORD','ROLE_ID','STATUS'], default_value="id", key='-COMBO_SEARCH-',enable_events=True),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22,enable_events=True)],
                      [sg.Text('Id:',size=15), sg.Text(key=self.Headings[0])],
                      [sg.Text('Username:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Password:',size=15),  sg.Input(key=self.Headings[2]),
                      [sg.Text('Role_id:',size=15), sg.Input(key=self.Headings[3])],
                      [sg.Text('Status:',size=15), sg.Input(key=self.Headings[4])],
                      [sg.Button('NEW ID'), sg.Button('ADD'),sg.Button('UPDATE'), sg.Button('DELETE'),sg.Button('RESET')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý tai khoan', layout)
    def empty(self):
        for item in self.Headings:
            self.window[item].update('')
    def reset(self):
        self.lstAccounts = AccountsBiz().get_all_accounts()
        self.result = []

        for item in self.lstAccounts:
            item = list(item)
            item[0] = AccountsBiz().to_str_id(id=item[0])

            self.result.append(item)


        self.window["-TABLE-"].update(self.result)
    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == 'NEW ID':
                newId = AccountsBiz().get_new_id()

                self.empty()

                self.window[self.Headings[0]].update(newId)
                self.window[self.Headings[4]].update(1)

            elif event == 'ADD':
                id = self.window[self.Headings[0]].get()
                username = values[self.Headings[1]]
                password = values[self.Headings[2]]
                role_id = values[self.Headings[3]]
                status = values[self.Headings[4]]

                account = {"id":id[2:], 'username': username, 'password': password, 'role_id': role_id, 'status': status, 'is_active': 1}
                add = AccountsBiz().add_accounts(accounts=accounts)
                if add != -1:
                    sg.popup('Success')
                self.empty()
                self.reset()
            elif event == "RESET":
                self.empty()
                self.reset()

            elif event == "-TABLE-":
                selected_row = values["-TABLE-"]
                # binding dữ liệu đến input field
                if selected_row:
                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row[0]][idx])
            elif event == "DELETE":
                id = self.window[self.Headings[0]].get()
                if id == "":
                    self.reset()
                sg.popup("Something error with server")

                while True:
                    # getPopupComfirm() có thể sài nhiều lần nên t để trong common
                    event, values = getPopupComfirm().read()
                    if event in (sg.WIN_CLOSED, 'Cancel'):
                        break
                    elif event == "OK":
                        result = AccountsBiz().delete_accounts(id=id[2:])
                        if result:
                            sg.popup("Xóa thành công")
                            self.empty()
                            self.reset()
                            break
                        else:
                            self.empty()
                            self.reset()
                            sg.popup("Something error with db")
            elif event == "UPDATE":
                biz = AccountsBiz()
                id = values[self.Headings[0]]
                username = values[self.Headings[1]]
                password = values[self.Headings[2]]
                role_id = values[self.Headings[3]]
                status = values[self.Headings[4]]
                is_active = values[self.Headings[5]]

                data  = {"id":id[2:], 'username': username, 'password': password, 'role_id': role_id, 'status': status, 'is_active': is_active}

                flag = any(value == '' for value in data.values())
                flagUpt = False
                if flag:
                    sg.popup("Invalid!")
                    flagUpt = True
                if not flagUpt:
                    upd = AccountsBiz().update_accounts(accounts=data, cond={"id": id[2:]})

                    if upd != -1:
                        sg.popup('Update Success')
                        self.empty()
                        self.reset()
                    else:
                        self.reset()
                        self.empty()
                        sg.popup("Something error with db")

                    # sự kiện search onchange
                elif event == "-CONTENT-":
                    value_search = values["-CONTENT-"]
                    search_with = values["-COMBO_SEARCH-"]

                    # binding list to listProduct
                    productEntitys = []
                    for item in self.result:
                        product = Acccounts(*item)
                        productEntitys.append(product)

                    result = []
                    for idx in range(len(productEntitys)):
                        if value_search in str(getattr(productEntitys[idx], search_with)):
                            result.append(self.result[idx])

                    self.window["-TABLE-"].update(result)

            self.window.close()






