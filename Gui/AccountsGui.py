import PySimpleGUI as sg
from Business.AccountsBiz import AccountsBiz
from DataAccess.AccountsDal import AccountsDal
from Common.PopupComfirm import getPopupComfirm
from Entity.AccountEntity import Account


class AccountsGui:


    def __init__(self):

        self.Headings = ['Id', 'Username', 'Password', 'RoleId', 'Status', 'IsActive']

        self.lstAccounts = AccountsBiz().get_all_accounts()
        self.result = []

        for item in self.lstAccounts:
            item = list(item)
            item[0] = AccountsBiz().to_str_id(id=item[0])
            if item[4] == 1:
                item[4] = "Đã cấp"
            else:
                item[4] = "Chưa cấp" 
            if item[5] == 1:
                item[5] = "Hoạt động" 
            else:
                item[5] = "Không hoạt động"

            self.result.append(item)
        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layout2 = [[sg.Text('DANH SÁCH TÀI KHOẢN',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['id','username','password','role_id','status', "is_active"], default_value="id", key='-COMBO_SEARCH-',enable_events=True),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22,enable_events=True)],
                      [sg.Text('Id:',size=15), sg.Text(key=self.Headings[0])],
                      [sg.Text('Username:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Password:',size=15),  sg.Input(key=self.Headings[2])],
                      [sg.Text('Role_id:',size=15), sg.Input(key=self.Headings[3])],
                      [sg.Text('Status:',size=15), sg.Text(key=self.Headings[4], text="Chưa cấp")],
                      [sg.Text('IsActive:',size=15), sg.Combo(key=self.Headings[5], values=["Hoạt động", "Không hoạt động"], default_value="Hoạt động")],
                      [sg.Button('NEW ID'), sg.Button('ADD'),sg.Button('UPDATE'), sg.Button('DELETE'),sg.Button('RESET')]]

        layout=[[sg.Col(layout2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Accout management', layout)
    def empty(self):
        for item in self.Headings:
            self.window[item].update('')
    def reset(self):
        self.lstAccounts = AccountsBiz().get_all_accounts()
        self.result = []

        for item in self.lstAccounts:
            item = list(item)
            item[0] = AccountsBiz().to_str_id(id=item[0])
            if item[4] == 1:
                item[4] = "Đã cấp"
            else:
                item[4] = "Chưa cấp" 
            if item[5] == 1:
                item[5] = "Hoạt động" 
            else:
                item[5] = "Không hoạt động"

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
                
                self.window[self.Headings[4]].Update(value = "Chưa cấp")
                self.window[self.Headings[5]].Update(value = "Hoạt động")

            elif event == 'ADD':
                id = self.window[self.Headings[0]].get()
                username = values[self.Headings[1]]
                password = values[self.Headings[2]]
                role_id = values[self.Headings[3]]
                status = 0
                if self.window[self.Headings[4]].get() == "Đã cấp":
                    status = 1
                

                account = {"id":id[2:], 'username': username, 'password': password, 'role_id': role_id, 'status': status, 'is_active': 1}
                add = AccountsBiz().add_accounts(accounts=account)
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
                    sg.popup("Id invalid!")
                else:
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
                            else:
                                self.empty()
                                self.reset()
                                sg.popup("Something error with db")
                            
            elif event == "UPDATE":
                id = self.window[self.Headings[0]].get()
                username = values[self.Headings[1]]
                password = values[self.Headings[2]]
                role_id = values[self.Headings[3]]
                status = 0
                if self.window[self.Headings[4]].get() == "Đã cấp":
                    status = 1
                is_active = 0
                if values[self.Headings[5]] == "Hoạt động":
                    is_active = 1

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
                    product = Account(*item)
                    productEntitys.append(product)

                result = []
                for idx in range(len(productEntitys)):
                    if value_search in str(getattr(productEntitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window["-TABLE-"].update(result)

        self.window.close()






