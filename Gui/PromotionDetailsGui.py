import PySimpleGUI as sg
from Business.PromotionsBiz import PromotionsBiz
from Entity.Promotions import Promotions


class PromotionDetailsGui:
    def __init__(self,promotion_id):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        self.dulieu = PromotionsBiz().get_all_promotion()
        self.result = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            # tùy chỉnh ID Type
            self.result.append(item)
        print(self.result)

        self.Headings = ['Mã khuến mãi', 'Tên chương trình', 'Ngày bắt đầu', 'Ngày kết thúc', 'Trạng thái','Kích hoạt']
        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện
        layout1 = [[sg.Text('Mã khuyến mãi:', size=15),sg.Text(text='KM'+promotion_id,size=20 , key=self.Headings[0])],
                   [sg.Text('Mã sản phẩm:', size=15),sg.Button('...', key='SELECT_PRODUCT') ,sg.Input(size=15 ,key=self.Headings[1])],
                   [sg.Text('Giá:', size=15), sg.Input(size=20 ,key=self.Headings[2])],
                   [sg.Text('Trạng thái:', size=15), sg.Input(size=20,key=self.Headings[3] ,default_text=1)],
                   [ sg.Button('Thêm'), sg.Button('Sửa'), sg.Button('Xóa')],
                   ]
        # tạo table
        table = sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', enable_events=True)
        layout2 = [[sg.Text('DANH SÁCH CHƯƠNG TRÌNH KHUYẾN MÃI', font="blod", justification="center"),sg.Button(image_filename='Picture/refresh-30.png',key='REFRESH')], [table]]
        layout3 = [[sg.Text('Chọn từ khóa search:', size=15), sg.Combo(['id','promotion_name', 'date_from', 'date_to', 'status', 'isActive'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22, enable_events=True)]]
        layout = [[layout1],[layout3], [sg.Column(layout2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý khuyến mãi', layout)

    def empty(self):
         self.window[self.Headings[0]].update('')
         self.window[self.Headings[1]].update('')
         self.window[self.Headings[2]].update('')
         self.window[self.Headings[3]].update('')
    def reset(self):
        self.dulieu = PromotionsBiz().get_all_promotion()
        self.result = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            # tùy chỉnh ID Type
            self.result.append(item)
        print(self.result)
        self.window['-TABLE-'].update(self.result)
    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event =='NEWID':
                newId = PromotionsBiz().get_new_id()
                self.window[self.Headings[0]].update(newId)
            elif event == 'Thêm':
                id = values[self.Headings[0]]
                promotion_name = values[self.Headings[1]]
                date_from = values[self.Headings[2]]
                date_to = values[self.Headings[3]]
                if values['-COMBO_STATUS-'] == 'Áp dụng':
                   status = 1
                else:
                   status = 0
                values[self.Headings[4]] = status
                # status = self.window[self.Headings[4]].get()

                add = PromotionsBiz().add_promotion({'id': id[2:], 'promotion_name':promotion_name,'date_from': date_from, 'date_to': date_to, 'status': status, 'is_active': 1})
                if add:
                    # Hiển thị kết quả
                    sg.popup('THÊM THÀNH CÔNG')
                    self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]]])
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup('THÊM thất bại')
            elif event == "Sửa":
                id = values[self.Headings[0]]
                promotion_name = values[self.Headings[1]]
                date_from = values[self.Headings[2]]
                date_to = values[self.Headings[3]]
                if values['-COMBO_STATUS-'] == 'Áp dụng':
                    status= 1
                else:
                  status = 0
                values[self.Headings[4]] = status
                update = PromotionsBiz().update_promotion({'promotion_name': promotion_name, 'date_from': date_from, 'date_to': date_to,
                     'status': status, 'is_active': 1}, {'id': id})
                if update:
                    sg.popup("Sửa thành công")
                    self.result.pop(selected_row)
                    self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]],
                                        values[self.Headings[3]], values[self.Headings[4]]])
                    # self.window['-TABLE-'].update(values=self.result)
                    self.reset()
                    self.empty()
                else:
                    sg.popup("Sửa thất bại")

            elif event == "Xóa":
                id = values[self.Headings[0]]
                result = PromotionsBiz().delete_promotion(id=id[2:])
                if result:
                    sg.popup("Xóa thành công")
                    del self.result[values['-TABLE-'][0]]
                    # self.window['-TABLE-'].update(values=self.result)
                    self.reset()
                    self.empty()
                else:
                    sg.popup("Xóa thất bại")
            # Sự kiện khi click vào cell trong table
            elif event == '-TABLE-':
                if values['-TABLE-']:
                    selected_row = values['-TABLE-'][0]
                else:
                    self.empty()
                # print(self.result[selected_row][0])
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
            elif event =='REFRESH':
                self.empty()
                self.reset()
            elif event == '-CONTENT-':
                value_search = values['-CONTENT-']
                search_with = values["-KEY-"]
                # binding list to listpromotion
                promotionEntitys = []
                for item in self.result:
                    promotion = Promotions(*item)
                    promotionEntitys.append(promotion)

                result = []
                for idx in range(len(promotionEntitys)):
                    if value_search in str(getattr(promotionEntitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window['-TABLE-'].update(result)



