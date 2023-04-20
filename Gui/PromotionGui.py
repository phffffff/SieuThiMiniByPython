import PySimpleGUI as sg
from Business.PromotionsBiz import PromotionsBiz

class PromotionsGUI:
    def __init__(self):
        biz = PromotionsBiz()
        self.dulieu = biz.get_all()
        self.result = [[]]
        print(self.dulieu)
        for i in self.dulieu:
            self.result.append(list(i))
        self.Headings = ['ID', 'Tên chương trình', 'Ngày bắt đầu', 'Ngày kết thúc', 'Trạng thái']
        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện

        layout1 = [[sg.Text('Mã khuyến mãi:', size=15), sg.Input(key=self.Headings[0])],
                   [sg.Text('Tên chương trình:', size=15), sg.Input(key=self.Headings[1])],
                   [sg.Text('Ngày bắt đầu:', size=15),sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[2], size=22), sg.Input(size=20 ,key=self.Headings[2])],
                   [sg.Text('Ngày kết thúc:', size=15), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[3], size=22), sg.Input(size=20 ,key=self.Headings[3])],
                   [sg.Text('Trạng thái:', size=15), sg.Input(key=self.Headings[4])],
                   [ sg.Button('Thêm'), sg.Button('Sửa'), sg.Button('Chi tiết'), sg.Button('Xóa')],
                   [sg.Text('Chọn từ khóa search:', size=15), sg.Combo(['ID', 'Tên chương trình', 'Ngày bắt đầu', 'Ngày kết thúc', 'Trạng thái'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22), sg.Button('SEARCH')]]
        # tạo table
        table = sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', enable_events=True)
        layout2 = [[sg.Text('DANH SÁCH CHƯƠNG TRÌNH KHUYẾN MÃI', font="blod", size=70, justification="center")],
                  [table]]
        layout = [[layout1], [sg.Column(layout2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý khuyến mãi', layout)

    def empty(self):
         self.window[self.Headings[0]].update('')
         self.window[self.Headings[1]].update('')
         self.window[self.Headings[2]].update('')
         self.window[self.Headings[3]].update('')
         self.window[self.Headings[4]].update('')

    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == 'Thêm':
                biz= PromotionsBiz()
                id = values[self.Headings[0]]
                promotion_name = values[self.Headings[1]]
                date_from = values[self.Headings[2]]
                date_to = values[self.Headings[3]]
                status = values[self.Headings[4]]

                add = biz.add({'id': id, 'promotion_name':promotion_name,'date_from': date_from, 'date_to': date_to, 'status': status, 'is_active': 1})
                if add:
                    sg.popup('THÊM THÀNH CÔNG')
                    self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]]])
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup('THÊM thất bại')
            elif event == "Sửa":
                biz = PromotionsBiz()
                id = values[self.Headings[0]]
                promotion_name = values[self.Headings[1]]
                date_from = values[self.Headings[2]]
                date_to = values[self.Headings[3]]
                status = values[self.Headings[4]]

                update = biz.update(
                    {'promotion_name': promotion_name, 'date_from': date_from, 'date_to': date_to,
                     'status': status, 'is_active': 1}, {'id': id})
                if update:
                    sg.popup("Sửa thành công")
                    self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]],
                                        values[self.Headings[3]], values[self.Headings[4]]])
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup("Sửa thất bại")
            elif event == "Xóa":
                biz = PromotionsBiz()
                id = values[self.Headings[0]]
                result = biz.update({'is_active': 0}, {'id': id})
                if result:
                    sg.popup("Xóa thành công")
                    del self.result[values['-TABLE-'][0]]
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup("Xóa thất bại")

