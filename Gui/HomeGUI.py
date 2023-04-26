import PySimpleGUI as sg

class HomeGUI:
    def __init__(self):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        self.lstProduct = biz.get_all()
        self.result = []
        print(self.dulieu)
        for i in self.dulieu:
            self.result.append(list(i))
        self.Headings = ['ID', 'Tên chương trình', 'Ngày bắt đầu', 'Ngày kết thúc', 'Trạng thái']
        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện

        layout1 = [[sg.Text('Mã khuyến mãi:', size=15), sg.Input(size=25 , key=self.Headings[0])],
                   [sg.Text('Tên chương trình:', size=15), sg.Input(size=25 ,key=self.Headings[1])],
                   [sg.Text('Ngày bắt đầu:', size=15),sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[2], size=22), sg.Input(size=20 ,key=self.Headings[2])],
                   [sg.Text('Ngày kết thúc:', size=15), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[3], size=22), sg.Input(size=20 ,key=self.Headings[3])],
                   [sg.Text('Trạng thái:', size=15), sg.Combo(['Áp dụng','Không áp dụng'],default_value='Áp dụng', key='-COMBO_STATUS-')],
                   [ sg.Button('Thêm'), sg.Button('Sửa'), sg.Button('Chi tiết'), sg.Button('Xóa')],
                   ]
        # tạo table
        table = sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', enable_events=True)
        layout2 = [[sg.Text('DANH SÁCH CHƯƠNG TRÌNH KHUYẾN MÃI', font="blod", size=70, justification="center")], [table]]
        layout3 = [[sg.Text('Chọn từ khóa search:', size=15), sg.Combo(['ID', 'Tên chương trình', 'Trạng thái'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22), sg.Button('SEARCH')]]
        layout = [[layout1],[layout3], [sg.Column(layout2)]]

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
                    if values['-COMBO_STATUS-'] == 'Áp dụng':
                        self.Headings[4] = 1
                    else:
                        self.Headings[4] = 0
                    # Hiển thị kết quả
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
                    self.result.pop(selected_row)
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
            # Sự kiện khi click vào cell trong table
            elif event == '-TABLE-':
                if values['-TABLE-']:
                    selected_row = values['-TABLE-'][0]
                else:
                    self.empty()
                print(self.result[selected_row][0])
                print(selected_row)
                # Điền dữ liệu vào các text element tương ứng
                self.window[self.Headings[0]].update(self.result[selected_row][0])
                self.window[self.Headings[1]].update(self.result[selected_row][1])
                self.window[self.Headings[2]].update(self.result[selected_row][2])
                self.window[self.Headings[3]].update(self.result[selected_row][3])
                if self.result[selected_row][4]==1 :
                    self.window['-COMBO_STATUS-'].update('Áp dụng')
                elif self.result[selected_row][4]==0 :
                    self.window['-COMBO_STATUS-'].update('Không Áp dụng')
            elif event == 'SEARCH':
                key = values['-KEY-']
                biz = PromotionsBiz()
                id = values['-CONTENT-']
                if key == 'ID':
                    self.result = biz.get_id(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'Tên chương trình':
                    self.result = biz.get_promotion_name(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")
                elif key == 'Trạng thái':
                    self.result = biz.get_bir(id)
                    if self.result:
                        sg.popup("Tìm thành công")
                        self.window['-TABLE-'].update(values=self.result)
                    else:
                        sg.popup("Tìm thất bại")


    