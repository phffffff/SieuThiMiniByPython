

import PySimpleGUI as sg
from Business.MembershipsBiz import MembershipsBiz
from DataAccess.MembershipsDal import MembershipsDal
from Entity.MembershipsEntity import Memberships


class MembershipsGui:
    def __init__(self):
        biz = MembershipsBiz()
        self.dulieu = biz.get_all()
        self.result=[[]]
        print(self.dulieu)
        for i in self.dulieu:
            self.result.append(list(i))
        self.Headings = ['ID', 'Mã xác nhận', 'Tên', 'Ngày sinh', 'Số điện thoại', 'Mail', 'Point']

        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('DANH SÁCH THÀNH VIÊN',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['ID','PASS','NAME','BIRTHDAY','PHONE','MAIL','POINT'], key='-KEY-'),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=23),sg.Button('SEARCH')],
                      [sg.Text('Mã thành viên:',size=15), sg.Input(key=self.Headings[0])],
                      [sg.Text('Tên thành viên:',size=15), sg.Input(key=self.Headings[2])],
                      [sg.Text('Ngày sinh:',size=15), sg.Input(key=self.Headings[3])],
                      [sg.Text('Số điện thoại:',size=15), sg.Input(key=self.Headings[4])],
                      [sg.Text('Mail:',size=15), sg.Input(key=self.Headings[5])],
                      [sg.Text('Điểm:',size=15), sg.Input(key=self.Headings[6])],
                      [sg.Text('Mã xác nhận:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Button('Tạo mới'), sg.Button('Sửa'),sg.Button('Đổ dữ liệu'), sg.Button('Xóa'),sg.Button('Thêm')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý thành viên', layout)
    def empty(self):
        self.window[self.Headings[0]].update('')
        self.window[self.Headings[1]].update('')
        self.window[self.Headings[2]].update('')
        self.window[self.Headings[3]].update('')
        self.window[self.Headings[4]].update('')
        self.window[self.Headings[5]].update('')
        self.window[self.Headings[6]].update('')

    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == 'Tạo mới':

                biz= MembershipsBiz()
                id = values[self.Headings[0]]
                commit = values[self.Headings[1]]
                name = values[self.Headings[2]]
                age = values[self.Headings[3]]
                phone = values[self.Headings[4]]
                mail = values[self.Headings[5]]
                point = values[self.Headings[6]]

                add = biz.add({'id': id, 'verification_code': commit, 'name': name, 'birthday': age, 'phone': phone, 'mail': mail, 'point': point, 'is_active': 1})

                if add:
                    sg.popup('THÊM THÀNH CÔNG')
                    self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]], values[self.Headings[5]], values[self.Headings[6]]])
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup('THÊM thất bại')

            elif event == "Sửa":
                biz = MembershipsBiz()
                id = values[self.Headings[0]]
                commit = values[self.Headings[1]]
                name = values[self.Headings[2]]
                age = values[self.Headings[3]]
                phone = values[self.Headings[4]]
                mail = values[self.Headings[5]]
                point = values[self.Headings[6]]

                result = biz.update({'verification_code': commit, 'name': name, 'birthday': age, 'phone': phone, 'mail': mail,'point': point}, {'id': id})
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

                biz = MembershipsBiz()
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
                biz = MembershipsBiz()
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
                elif key == 'POINT':
                    self.result = biz.get_point(id)
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
                    biz = MembershipsBiz()
                    self.dulieu = biz.get_all()
                    self.result = [[]]
                    for self.row in self.dulieu:
                        self.result.append(list(self.row))
                    self.window['-TABLE-'].update(values= self.result)










