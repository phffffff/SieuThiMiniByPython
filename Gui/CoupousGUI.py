

import PySimpleGUI as sg
from SieuThiMiniByPython.Business.CoupousBiz import CoupousBiz
from SieuThiMiniByPython.DataAccess.CoupousDal import CoupouDal
from SieuThiMiniByPython.Entity.Coupous import Coupous
from SieuThiMiniByPython.Common.PopupComfirm import getPopupComfirm

class CoupousGUI:
    def __init__(self):
        self.lstCoupous = CoupousBiz().get_all_coupous(cond={"is_active": 1})
        self.result = []

        for item in self.lstCoupous:
            item = list(item)
            item[0] = CoupousBiz().to_str_id(id=item[0])

            self.result.append(item)
        self.Headings = [' ID ', 'CODE', 'DISCOUNT', 'DATE FROM', 'DATE TO', 'STATUS']

        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('DANH SÁCH PHIẾU GIẢM GIÁ',font="blod",size=50,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['id','code','discount','date_from','date_to','status'], default_value="id", key='-COMBO_SEARCH-',enable_events=True),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22,enable_events=True)],
                      [sg.Text('ID:',size=15), sg.Text(key=self.Headings[0])],
                      [sg.Text('CODE:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('DISCOUNT:',size=15), sg.Input(key=self.Headings[2])],
                      [sg.Text('DATE FROM:', size=15), sg.Input(size=20, key=self.Headings[3]), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[3], size=22)],
                      [sg.Text('DATE TO:', size=15), sg.Input(size=20, key=self.Headings[4]),sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[4], size=22)],
                      [sg.Text('STATUS:',size=15), sg.Input(key=self.Headings[5])],
                      [sg.Button('NEW ID'), sg.Button('ADD'),sg.Button('UPDATE'), sg.Button('DELETE'),sg.Button('RESET')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý thành viên', layout)

    def empty(self):
        for item in self.Headings:
            if item == "Remaining" or item == "Discount":
                continue
            self.window[item].update('')

    def reset(self):
        self.lstCoupous = CoupousBiz().get_all_coupous(cond={"is_active": 1})
        self.result = []

        for item in self.lstCoupous:
            item = list(item)
            item[0] = CoupousBiz().to_str_id(id=item[0])

            self.result.append(item)

        self.window["-TABLE-"].update(self.result)



    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == 'NEW ID':
                newId = CoupousBiz().get_new_id()

                self.empty()

                self.window[self.Headings[0]].update(newId)
            elif event == 'ADD':
                id = self.window[self.Headings[0]].get()
                code = values[self.Headings[1]]
                discount = values[self.Headings[2]]
                date_from = values[self.Headings[3]]
                date_to = values[self.Headings[4]]
                status = values[self.Headings[5]]

                data = {"id": id[2:], "coupou_code": code, "discount": discount, "date_from": date_from,
                        "date_to": date_to, "status": status, "is_active": 1}
                add = CoupousBiz().add_coupous(coupous=data)
                if add != -1:
                    sg.popup('Success')
                    self.reset()

            elif event == "RESET":
                self.empty()
                self.reset()

            elif event == "-TABLE-":
                selected_row = values["-TABLE-"]
                # binding dữ liệu đến input field
                if selected_row:
                    for idx in range(len(self.Headings)):
                        if self.Headings[idx] == "Discount" or self.Headings[idx] == "Remaining":
                            continue
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
                        result = CoupousBiz().delete_coupous(id=id[2:])
                        if result:
                            sg.popup("Xóa thành công")
                            self.reset()
                            break
                        else:
                            self.reset()
                            sg.popup("Something error with db")
            elif event == "UPDATE":
                id = self.window[self.Headings[0]].get()
                code = values[self.Headings[1]]
                discount = values[self.Headings[2]]
                date_from = values[self.Headings[3]]
                date_to = values[self.Headings[4]]
                status = values[self.Headings[5]]

                data = {"id": id[2:], "coupou_code": code, "discount": discount, "date_from": date_from,
                        "date_to": date_to, "status": status, "is_active": 1}

                flag = any(value == '' for value in data.values())
                if flag:
                    sg.popup("Invalid!")
                    break

                upd = CoupousBiz().update_coupous(coupous=data, cond={"id": id[2:]})
                if upd != -1:
                    sg.popup('Update Success')
                    self.reset()
                else:
                    self.reset()
                    sg.popup("Something error with db")

                # sự kiện search onchange
            elif event == "-CONTENT-":
                value_search = values["-CONTENT-"]
                search_with = values["-COMBO_SEARCH-"]

                # binding list to listProduct
                productEntitys = []
                for item in self.result:
                    product = Coupous(*item)
                    productEntitys.append(product)

                result = []
                for idx in range(len(productEntitys)):
                    if value_search in str(getattr(productEntitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window["-TABLE-"].update(result)

        self.window.close()







