

import PySimpleGUI as sg
from Business.StaffsBiz import StaffsBiz
from DataAccess.StaffsDal import StaffsDal
from Entity.StaffsEntity import Staffs


class StaffsGui:
    def __init__(self):
        biz = StaffsBiz()
        self.dulieu = biz.get_all()
        self.result=[[]]
        for i in self.dulieu:
            self.result.append(list(i))
        self.Headings = ['ID', 'Tên', 'Ngày sinh', 'Số điện thoại', 'Mail', 'account']

        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('DANH SÁCH NHÂN VIÊN',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['ID','PASS','NAME','BIRTHDAY','PHONE','MAIL','ACCOUNT'], key='-KEY-'),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=23),sg.Button('SEARCH')],
                      [sg.Text('Mã nhân viên:',size=15), sg.Input(key=self.Headings[0])],
                      [sg.Text('Tên nhân viên:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Ngày sinh:',size=15), sg.Input(key=self.Headings[2])],
                      [sg.Text('Số điện thoại:',size=15), sg.Input(key=self.Headings[3])],
                      [sg.Text('Mail:',size=15), sg.Input(key=self.Headings[4])],
                      [sg.Text('account:',size=15), sg.Input(key=self.Headings[5])],
                      [sg.Button('Tạo mới'), sg.Button('Sửa'),sg.Button('Đổ dữ liệu'), sg.Button('Xóa'),sg.Button('Thêm')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý nhân viên', layout)
    def empty(self):
        self.window[self.Headings[0]].update('')
        self.window[self.Headings[1]].update('')
        self.window[self.Headings[2]].update('')
        self.window[self.Headings[3]].update('')
        self.window[self.Headings[4]].update('')
        self.window[self.Headings[5]].update('')

    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == 'Tạo mới':

                biz= StaffsBiz()
                id = values[self.Headings[0]]
                name = values[self.Headings[1]]
                age = values[self.Headings[2]]
                phone = values[self.Headings[3]]
                mail = values[self.Headings[4]]
                account = values[self.Headings[5]]

                add = biz.add({'id': id, 'name': name, 'birthday': age, 'phone': phone, 'mail': mail, 'account': account, 'is_active': 1})

                if add:
                    sg.popup('THÊM THÀNH CÔNG')
                    self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]], values[self.Headings[5]], values[self.Headings[6]]])
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup('THÊM thất bại')

            elif event == "Sửa":
                biz = StaffsBiz()
                id = values[self.Headings[0]]
                name = values[self.Headings[1]]
                age = values[self.Headings[2]]
                phone = values[self.Headings[3]]
                mail = values[self.Headings[4]]
                account = values[self.Headings[5]]

                result = biz.update({'name': name, 'birthday': age, 'phone': phone, 'mail': mail,'account': account}, {'id': id})
                if result:
                    sg.popup("Sửa thành công")
                    self.result[values['-TABLE-'][0]] = [values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]], values[self.Headings[5]], values[self.Headings[6]]]
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()

            elif event == "Đổ dữ liệu":
                editRow = values['-TABLE-'][0]
                sg.popup('Đổ dữ liệu thành công')
                for i in range(7):
                    self.window[self.Headings[i]].update(value=self.result[editRow][i])

            elif event == "Xóa":

                biz = StaffsBiz()
                id = values[self.Headings[0]]

                result = biz.update({'is_active': 0}, {'id': id})
                if result:
                    sg.popup("Xóa thành công")
                    del self.result[values['-TABLE-'][0]]
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup("Xóa thất bại")
            elif event == 'SEARCH':
                key = values['-KEY-']
                biz = StaffsBiz()
                id = values['-CONTENT-']
                if key == 'ID':
                    self.result = biz.get_id(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")

                elif key == 'NAME':
                    self.result = biz.get_name(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'BIRTHDAY':
                    self.result = biz.get_bir(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'PHONE':
                    self.result = biz.get_phone(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'ACCOUNT':
                    self.result = biz.get_account(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'MAIL':
                    self.result = biz.get_mail(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                else:
                    biz = StaffsBiz()
                    self.dulieu = biz.get_all()
                    self.result = [[]]
                    for self.row in self.dulieu:
                        self.result.append(list(self.row))
                    self.window['-TABLE-'].update(values= self.result)









