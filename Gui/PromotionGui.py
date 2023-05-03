import PySimpleGUI as sg
from Business.PromotionsBiz import PromotionsBiz
from Business.PromotionDetailsBiz import PromotionDetailsBiz
from Business.ProductBiz import ProductBiz
from Entity.Promotions import Promotions
from Gui.PromotionDetailsGui import PromotionDetailsGui
from Common.PopupComfirm import getPopupComfirm

from datetime import date


class PromotionsGUI:
    def __init__(self):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        self.dulieu = PromotionsBiz().get_all_promotion()
        self.result = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            if item[4] == 1:
                item[4] = "Áp dụng"
            else:
                item[4] = "Không áp dụng" 
            if item[5] == 1:
                item[5] = "Hoạt động" 
            else:
                item[5] = "Không hoạt động"
            # tùy chỉnh ID Type
            self.result.append(item)
        print(self.result)

        self.Headings = ['Id', 'Name', 'Date from', 'Date to', 'Status','IsActive']
        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện
        layout1 = [[sg.Text('Id:', size=15),sg.Button("ID" , key= "NEWID") ,sg.Text(size=20 , key=self.Headings[0])],
                   [sg.Text('Name:', size=15), sg.Input(size=25 ,key=self.Headings[1])],
                   [sg.Text('Date from:', size=15),sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[2], size=22), sg.Input(size=20 ,key=self.Headings[2])],
                   [sg.Text('Date to:', size=15), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target=self.Headings[3], size=22), sg.Input(size=20 ,key=self.Headings[3])],
                   [sg.Text('Status:', size=15), sg.Text(text='Không áp dụng', key=self.Headings[4])],
                   [sg.Text('IsActive:', size=15), sg.Combo(['Hoạt động','Không hoạt động'],default_value='Hoạt động', key=self.Headings[5])],
                   [ sg.Button('Thêm'), sg.Button('Sửa'), sg.Button('Chi tiết'), sg.Button('Xóa'), sg.Button("Áp dụng"), sg.Button("Ngưng áp dụng")],
                   ]
        # tạo table
        table = sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', enable_events=True)
        layout2 = [[sg.Text('PROMOTIONS MANAGEMENT', font="blod", justification="center"),sg.Button(image_filename='Picture/refresh-30.png',key='REFRESH')], [table]]
        layout3 = [[sg.Text('Search with:', size=15), sg.Combo(['id','promotion_name', 'date_from', 'date_to', 'status', 'isActive'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22, enable_events=True)]]
        layout = [[layout1],[layout3], [sg.Column(layout2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Promotion management', layout)

    def empty(self):
         for item in self.Headings:
             self.window[item].update('')
    def reset(self):
        self.dulieu = PromotionsBiz().get_all_promotion()
        self.result = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            if item[4] == 1:
                item[4] = "Áp dụng"
            else:
                item[4] = "Không áp dụng" 
            if item[5] == 1:
                item[5] = "Hoạt động" 
            else:
                item[5] = "Không hoạt động"
        
            # tùy chỉnh ID Type
            self.result.append(item)
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
                self.window[self.Headings[4]].update("Không áp dụng")
            elif event == 'Thêm':
                id = self.window[self.Headings[0]].get()
                promotion_name = values[self.Headings[1]]
                date_from = values[self.Headings[2]]
                date_to = values[self.Headings[3]]
                status = 0
                if self.window[self.Headings[4]].get() == 'Áp dụng':
                   status = 1
                is_active = 0
                if values[self.Headings[5]] == "Hoạt động":
                    is_active = 1

                add = PromotionsBiz().add_promotion({'id': id[2:], 'promotion_name':promotion_name,'date_from': date_from, 'date_to': date_to, 'status': status, 'is_active': is_active})
                if add != -1:
                    # Hiển thị kết quả
                    sg.popup('Success')
                    # self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]]])
                    # self.window['-TABLE-'].update(values=self.result)
                    # self.empty()
                    self.reset()
                else:
                    sg.popup('Something error with db')
            elif event == "Sửa":
                if self.window[self.Headings[4]].get() == "Áp dụng":
                    sg.popup("Chương trình đang áp dụng.\nKhông thể sửa đổi")
                else:
                    id = self.window[self.Headings[0]].get()
                    promotion_name = values[self.Headings[1]]
                    date_from = values[self.Headings[2]]
                    date_to = values[self.Headings[3]]
                    is_active = 0
                    status = 0
                    if values[self.Headings[5]] == "Hoạt động":
                        is_active = 1

                    promotion={'promotion_name': promotion_name, 'date_from': date_from, 'date_to': date_to, 'status':status, 'is_active': is_active}
                    
                    flag = any(value == '' for value in promotion.values())
                    flagUpt = False
                    if flag:
                        sg.popup("Invalid!")
                        flagUpt = True
                    if not flagUpt:
                        update = PromotionsBiz().update_promotion(promotion=promotion, cond={'id': id[2:]})
                        if update != -1:
                            sg.popup('Update Success')
                            self.empty()
                            self.reset()
                        else:
                            self.reset()
                            self.empty()
                            sg.popup("Something error with db")

            elif event == "Xóa":
                selected_row = values["-TABLE-"][0]

                if selected_row:
                    # có thể duyệt for nếu thích
                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row][idx])
                    if self.result[selected_row][4] == "Không áp dụng":
                        id = self.window[self.Headings[0]].get()

                        while True:
                            
                            event, values = getPopupComfirm().read()
                            
                            if event == sg.WIN_CLOSED or event == "Cancel":
                                break
                            elif event == "OK":
                                result = PromotionsBiz().delete_promotion(id=id[2:])
                                if result:
                                    sg.popup("Delete Success")
                                    self.reset()
                                else:
                                    self.reset()
                                    sg.popup("Something error with db")
                    else:
                        sg.popup("Không thể xóa khuyến mãi đang được áp dụng")
            # Sự kiện khi click vào cell trong table
            elif event == '-TABLE-':
                selected_row = values["-TABLE-"]
                # binding dữ liệu đến input field
                if selected_row:
                    # có thể duyệt for nếu thích
                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row[0]][idx])
            elif event =='REFRESH':
                self.reset()
                self.empty()
                
                
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

            elif event=='Chi tiết':
                id = self.window[self.Headings[0]].get()
                status = self.window[self.Headings[4]].get()
                if id=="":
                    sg.popup('Bạn chưa chọn CT khuyến mãi !')
                else:
                    promotiondetail = PromotionDetailsGui(promotion_id=id[2:], status =status)
                    promotiondetail.run()
            elif event=='Áp dụng':
                dem = 0
                for item in self.result:
                    if item[4] == "Áp dụng":
                        dem += 1
                if dem == 0:
                    id = self.window[self.Headings[0]].get()

                    if id=="":
                        sg.popup('Bạn chưa chọn CT khuyến mãi !')
                    else:
                        today = date.today()
                        flag = False
                        for item in self.result:
                            if item[0] == id:
                                if item[2] < today and today < item[3]:
                                    flag = True
                        if flag:
                            dulieu = PromotionDetailsBiz().get_all_promotion_details(cond={"promotion_id": id[2:], "is_active":1})
                            result = []
                            for item in dulieu:
                                item = list(item)
                                result.append(item)
                            
                            upd = PromotionsBiz().update_promotion(promotion={"status":1}, cond={"id":id[2:]})
                            if upd == -1:
                                sg.popup("Áp dụng thất bại")
                            else:
                                isErr = False
                                for item in result:
                                    updPrdct = ProductBiz().update_product(product={"discount":item[2]}, cond={"id":item[1]})
                                    if updPrdct == -1:
                                        isErr = True
                                if not isErr:
                                    self.reset()
                                    sg.popup("Áp dụng thành công")
                                else:
                                    sg.popup("Chưa cập nhật được giảm giá")
                        else:
                            sg.popup("Đã hết thời gian khuyến mãi")
                elif dem == 1:
                    sg.popup("Chỉ được áp dụng 1 chương trình khuyến mãi")
                else:
                    sg.popup("Chỉ được áp dụng 1 chương trình khuyến mãi")

            elif event=='Ngưng áp dụng':
                selected_row = values["-TABLE-"]
                id = self.window[self.Headings[0]].get()
                if id=="":
                    sg.popup('Bạn chưa chọn CT khuyến mãi !')
                else:
                    if selected_row:
                        if self.result[selected_row[0]][4] == "Áp dụng":
                            dulieu = PromotionDetailsBiz().get_all_promotion_details(cond={"promotion_id": id[2:], "is_active":1})
                            result = []
                            for item in dulieu:
                                item = list(item)
                                result.append(item)
                            
                            upd = PromotionsBiz().update_promotion(promotion={"status":0}, cond={"id":id[2:]})
                            if upd == -1:
                                sg.popup("Không thể ngưng")
                            else:
                                isErr = False
                                for item in result:
                                    updPrdct = ProductBiz().update_product(product={"discount":0}, cond={"id":item[1]})
                                    if updPrdct == -1:
                                        isErr = True
                                if not isErr:
                                    self.reset()
                                    sg.popup("Ngưng thành công")
                                else:
                                    sg.popup("Ngưng thất bại, chưa cập nhật lại giá")                        
                        else:
                            sg.popup("Khuyến mãi chưa được áp dụng")
 


