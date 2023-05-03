import PySimpleGUI as sg

from Business.PromotionDetailsBiz import PromotionDetailsBiz
from Entity.PromotionDetails import PromotionDetails
from Gui.SelectProductGui import SelectProductGui


class PromotionDetailsGui:
    def __init__(self,promotion_id):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        self.dulieu = PromotionDetailsBiz().get_all_promotion_details(cond={"promotion_id":promotion_id})
        self.result = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionDetailsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[1] = PromotionDetailsBiz().to_str_id_product(id=item[1])
            # tùy chỉnh ID Type
            self.result.append(item)
        print(self.result)

        self.Headings = ['Mã khuến mãi', 'Mã sản phẩm', 'Giá', 'Trạng thái']
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
        layout3 = [[sg.Text('Chọn từ khóa search:', size=15), sg.Combo([ 'promotion_id', 'product_id', 'price', 'is_active'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22, enable_events=True)]]
        layout = [[layout1],[layout3], [sg.Column(layout2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý khuyến mãi', layout)

    def empty(self):
         # self.window[self.Headings[0]].update('')
         self.window[self.Headings[1]].update('')
         self.window[self.Headings[2]].update('')
         self.window[self.Headings[3]].update('')
    def reset(self):
        promotion_id = self.window[self.Headings[0]].get()
        print(promotion_id)
        self.dulieu = PromotionDetailsBiz().get_all_promotion_details(cond={"promotion_id": promotion_id[2:]})
        self.result = []
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionDetailsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[1] = PromotionDetailsBiz().to_str_id_product(id=item[1])
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
            elif event == '-TABLE-':
                if values['-TABLE-']:
                    selected_row = values['-TABLE-'][0]
                else:
                    self.empty()
                # print(self.result[selected_row][0])
                # Điền dữ liệu vào các text element tương ứng
                self.window[self.Headings[1]].update(self.result[selected_row][1])
                self.window[self.Headings[2]].update(self.result[selected_row][2])
                self.window[self.Headings[3]].update(self.result[selected_row][3])
            elif event == 'Thêm':
                promotion_id = self.window[self.Headings[0]].get()
                product_id = values[self.Headings[1]]
                price = values[self.Headings[2]]
                status = values[self.Headings[3]]
                add = PromotionDetailsBiz().add_promotion_details({'promotion_id': promotion_id[2:], 'product_id':product_id[2:],'price': price, 'is_active': 1})
                if add:
                    # Hiển thị kết quả
                    sg.popup('THÊM THÀNH CÔNG')
                    # self.result.append(promotion_id,product_id,price,status)
                    self.reset()
                    self.window['-TABLE-'].update(values=self.result)
                    self.empty()
                else:
                    sg.popup('THÊM thất bại')
            elif event == "Sửa":
                product_id_old = self.result[selected_row][1]
                promotion_id = self.window[self.Headings[0]].get()
                product_id = values[self.Headings[1]]
                price = values[self.Headings[2]]
                status = values[self.Headings[3]]
                update = PromotionDetailsBiz().update_promotion_detais({'product_id': product_id[2:], 'price':price,
                      'is_active': status}, {'promotion_id': promotion_id[2:] , 'product_id':product_id_old[2:]})
                if update:
                    sg.popup("Sửa thành công")
                    # self.result.pop(selected_row)
                    # self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]],
                    #                     values[self.Headings[3]], values[self.Headings[4]]])
                    # self.window['-TABLE-'].update(values=self.result)
                    self.reset()
                    self.empty()
                else:
                    sg.popup("Sửa thất bại")

            elif event == "Xóa":
                promotion_id = self.window[self.Headings[0]].get()
                product_id = values[self.Headings[1]]
                result = PromotionDetailsBiz().delete_promotion(promotion_id=promotion_id[2:] , product_id=product_id[2:])
                if result:
                    sg.popup("Xóa thành công")
                    # del self.result[values['-TABLE-'][0]]
                    # self.window['-TABLE-'].update(values=self.result)
                    self.reset()
                    self.empty()
                else:
                    sg.popup("Xóa thất bại")
            # Sự kiện khi click vào cell trong table

            elif event =='REFRESH':
                self.reset()
                self.empty()
            elif event == '-CONTENT-':
                value_search = values['-CONTENT-']
                search_with = values["-KEY-"]
                # binding list to listpromotion
                promotionEntitys = []
                for item in self.result:
                    promotion = PromotionDetails(*item)
                    promotionEntitys.append(promotion)
                result = []
                for idx in range(len(promotionEntitys)):
                    if value_search in str(getattr(promotionEntitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window['-TABLE-'].update(result)
            elif event =='SELECT_PRODUCT':
                selectproduct = SelectProductGui()
                selectproduct.run()
                product_id = selectproduct.product_selected()
                self.window[self.Headings[1]].update(product_id)

