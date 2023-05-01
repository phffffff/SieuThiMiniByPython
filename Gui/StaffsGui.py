

import PySimpleGUI as sg
from Business.StaffsBiz import StaffsBiz
from DataAccess.StaffsDal import StaffsDal
from Common.PopupComfirm import getPopupComfirm
from Entity.StaffsEntity import Staffs


class StaffsGui:


    def __init__(self):

        self.Headings = ['ID', 'Tên', 'Ngày sinh', 'Số điện thoại', 'Mail', 'account']

        self.lstStaffs = StaffsBiz().get_all_staffs()
        self.result = []

        for item in self.lstStaffs:
            item = list(item)
            item[0] = StaffsBiz().to_str_id(id=item[0])

            self.result.append(item)
        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('DANH SÁCH NHÂN VIÊN',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['ID','NAME','BIRTHDAY','PHONE','MAIL','ACCOUNT'], default_value="id", key='-COMBO_SEARCH-',enable_events=True),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22,enable_events=True)],
                      [sg.Text('Id:',size=15), sg.Text (key=self.Headings[0])],
                      [sg.Text('Name:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Birthday:',size=15),  sg.Input(size=20, key=self.Headings[2]), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[2], size=22)],
                      [sg.Text('Phone:',size=15), sg.Input(key=self.Headings[3])],
                      [sg.Text('Mail:',size=15), sg.Input(key=self.Headings[4])],
                      [sg.Text('account:',size=15), sg.Input(key=self.Headings[5])],
                      [sg.Button('NEW ID'), sg.Button('ADD'),sg.Button('UPDATE'), sg.Button('DELETE'),sg.Button('RESET')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý nhân viên', layout)
    def empty(self):
        for item in self.Headings:
            self.window[item].update('')
    def reset(self):
        self.lstStaffs = StaffsBiz().get_all_staffs()
        self.result = []

        for item in self.lstStaffs:
            item = list(item)
            item[0] = StaffsBiz().to_str_id(id=item[0])

            self.result.append(item)


        self.window["-TABLE-"].update(self.result)
    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == 'NEW ID':
                newId = StaffsBiz().get_new_id()

                self.empty()

                self.window[self.Headings[0]].update(newId)
                self.window[self.Headings[5]].update(1)

            elif event == 'ADD':
                id = self.window[self.Headings[0]].get()
                name = values[self.Headings[1]]
                age = values[self.Headings[2]]
                phone = values[self.Headings[3]]
                mail = values[self.Headings[4]]
                account = values[self.Headings[5]]

                staff = {"id":id[2:], 'name': name, 'birthday': age, 'phone': phone, 'mail': mail, 'account': account, 'is_active': 1}
                add = StaffsBiz().add_staffs(staffs=staffs)
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
                        result = StaffsBiz().delete_staffs(id=id[2:])
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
                biz = StaffsBiz()
                id = values[self.Headings[0]]
                name = values[self.Headings[1]]
                age = values[self.Headings[2]]
                phone = values[self.Headings[3]]
                mail = values[self.Headings[4]]
                account = values[self.Headings[5]]
                is_active = values[self.Headings[6]]

                data  = {"id":id[2:], 'name': name, 'birthday': age, 'phone': phone, 'mail': mail, 'account': account, 'is_active': is_active}

                flag = any(value == '' for value in data.values())
                flagUpt = False
                if flag:
                    sg.popup("Invalid!")
                    flagUpt = True
                if not flagUpt:
                    upd = StaffsBiz().update_staffs(staffs=data, cond={"id": id[2:]})

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
                        product = Staffs(*item)
                        productEntitys.append(product)

                    result = []
                    for idx in range(len(productEntitys)):
                        if value_search in str(getattr(productEntitys[idx], search_with)):
                            result.append(self.result[idx])

                    self.window["-TABLE-"].update(result)

            self.window.close()






