

import PySimpleGUI as sg
from Business.CoupousBiz import CoupousBiz
from DataAccess.CoupousDal import CoupouDal


class CoupousGUI:
    def __init__(self):
        biz = CoupousBiz()
        self.dulieu = biz.get_all()
        self.result=[[]]
        for i in self.dulieu:
            self.result.append(list(i))
        self.Headings = ['ID', 'Code', 'Discount', 'Ngày bắt đầu', 'Ngày kết thúc', 'Trạng thái']

        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('DANH SÁCH PHIẾU GIẢM GIÁ',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['ID','CODE','DISCOUNT','DATE-FROM','DATE-TO','STATUS'], key='-KEY-'),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22),sg.Button('SEARCH')],
                      [sg.Text('Mã giảm giá:',size=15), sg.Input(key=self.Headings[0])],
                      [sg.Text('Code:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Discount:',size=15), sg.Input(key=self.Headings[2])],
                      [sg.Text('Ngày bắt đầu:',size=15), sg.Input(key=self.Headings[3])],
                      [sg.Text('Ngày kết thúc:',size=15), sg.Input(key=self.Headings[4])],
                      [sg.Text('Trạng thái:',size=15), sg.Input(key=self.Headings[5])],
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


    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == 'Tạo mới':

                biz= CoupousBiz()
                id = values[self.Headings[0]]
                code = values[self.Headings[1]]
                discount = values[self.Headings[2]]
                date_from = values[self.Headings[3]]
                date_to = values[self.Headings[4]]
                status = values[self.Headings[5]]

                add = biz.add({'id': id, 'coupou_code': code, 'discount': discount, 'date_from': date_from, 'date_to': date_to, 'status': status, 'is_active': 1})
                if add:
                    sg.popup('THÊM THÀNH CÔNG')
                    self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]], values[self.Headings[5]]])
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup('THÊM thất bại')
            elif event == "Sửa":
                biz = CoupousBiz()
                id = values[self.Headings[0]]
                code = values[self.Headings[1]]
                discount = values[self.Headings[2]]
                date_from = values[self.Headings[3]]
                date_to = values[self.Headings[4]]
                status = values[self.Headings[5]]

                update = biz.update({'coupou_code': code, 'discount': discount, 'date_from': date_from, 'date_to': date_to, 'status': status, 'is_active': 1},{'id': id})
                if update:
                    sg.popup("Sửa thành công")
                    self.result[values['-TABLE-'][0]] = [values[self.Headings[0]], values[self.Headings[1]],
                                                         values[self.Headings[2]], values[self.Headings[3]],
                                                         values[self.Headings[4]], values[self.Headings[5]]]
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()

            elif event == "Đổ dữ liệu":
                editRow = values['-TABLE-'][0]
                sg.popup('Đổ dữ liệu thành công')
                for i in range(6):
                    self.window[self.Headings[i]].update(value=self.result[editRow][i])
            elif event == "Xóa":
                biz = CoupousBiz()
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
                biz = CoupousBiz()
                id = values['-CONTENT-']
                if key == 'ID':
                    self.result = biz.get_id(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")

                elif key == 'DISCOUNT':
                    self.result = biz.get_discount(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'DATE-FROM':
                    self.result = biz.get_date_from(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'DATE-TO':
                    self.result = biz.get_date_to(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'STATUS':
                    self.result = biz.get_status(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                else:
                    self.dulieu = biz.get_all()
                    self.result = [[]]
                    for self.row in self.dulieu:
                        self.result.append(list(self.row))
                    self.window['-TABLE-'].update(values= self.result)






