import PySimpleGUI as sg

from Business.PromotionDetailsBiz import PromotionDetailsBiz
from Business.ProductBiz import ProductBiz
from Entity.PromotionDetails import PromotionDetails
from Gui.SelectProductGui import SelectProductGui


class PromotionDetailsGui:
    def __init__(self,promotion_id, status):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        self.stts = status

        self.dulieu = PromotionDetailsBiz().get_all_promotion_details(cond={"promotion_id":promotion_id})
        self.result = []
        self.resultName = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionDetailsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[1] = ProductBiz().get_A_from_B(A="name", valueB=item[1], nameB="id")
            if item[3] == 1:
                item[3] = "Hoạt động"
            else:
                item[3] = "Không hoạt động"
            # tùy chỉnh ID Type
            self.result.append(item)
            self.resultName.append(item[1])
        
        self.lstProduct = ProductBiz().get_all_product(cond={"is_active":1}, fields=["name"])
        self.resultPrdct = []

        for item in self.lstProduct:
            item=list(item)
        
            self.resultPrdct.append(item[0])
        
        self.newResultPrdct = [x for x in self.resultPrdct if x not in self.resultName]

        self.Headings = ['Promotion Id', 'Product Id', 'Price', 'Status']
        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện
        layout1 = [[sg.Text('Promotion Id:', size=15),sg.Text(text='KM'+promotion_id,size=20 , key=self.Headings[0])],
                   [sg.Text('Product Id:', size=15),sg.Combo(values=self.newResultPrdct, default_value=self.newResultPrdct[0], key=self.Headings[1])],
                   [sg.Text('Price:', size=15), sg.Input(size=20 ,key=self.Headings[2])],
                   [sg.Text('Status:', size=15), sg.Combo(values=["Hoạt động", "Không hoạt động"],size=20,key=self.Headings[3] ,default_value="Hoạt động")],
                   [ sg.Button('Thêm'), sg.Button('Sửa'), sg.Button('Xóa')],
                   ]
        # tạo table
        table = sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', enable_events=True)
        layout2 = [[sg.Text('PROMOTION PRODUCT MANAGEMENT', font="blod", justification="center"),sg.Button(image_filename='Picture/refresh-30.png',key='REFRESH')], [table]]
        layout3 = [[sg.Text('Search with:', size=15), sg.Combo([ 'promotion_id', 'product_id', 'price', 'is_active'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22, enable_events=True)]]
        layout = [[layout1],[layout3], [sg.Column(layout2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Promotion details', layout)

    def empty(self):
         # self.window[self.Headings[0]].update('')
         self.window[self.Headings[1]].update('')
         self.window[self.Headings[2]].update('')
         self.window[self.Headings[3]].update('')
    def reset(self):
        promotion_id = self.window[self.Headings[0]].get()

        self.dulieu = PromotionDetailsBiz().get_all_promotion_details(cond={"promotion_id": promotion_id[2:]})
        self.result = []
        self.resultName = []
        for item in self.dulieu:
            item = list(item)
            item[0] = PromotionDetailsBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[1] = ProductBiz().get_A_from_B(A="name", valueB=item[1], nameB="id")
            if item[3] == 1:
                item[3] = "Hoạt động"
            else:
                item[3] = "Không hoạt động"
            # tùy chỉnh ID Type
            self.result.append(item)
            self.resultName.append(item[1])

        self.lstProduct = ProductBiz().get_all_product(cond={"is_active":1}, fields=["name"])
        self.resultPrdct = []

        for item in self.lstProduct:
            item=list(item)
        
            self.resultPrdct.append(item[0])

        self.newResultPrdct = []
        self.newResultPrdct = [x for x in self.resultPrdct if x not in self.resultName]
        
        self.window[self.Headings[1]].Update(values=self.newResultPrdct, value=self.newResultPrdct[0])
        self.window['-TABLE-'].update(self.result)
    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == '-TABLE-':
                selected_row = values["-TABLE-"]
                # binding dữ liệu đến input field
                if selected_row:
                    # có thể duyệt for nếu thích
                    self.window[self.Headings[1]].update(self.result[selected_row[0]][1])
                    self.window[self.Headings[2]].update(self.result[selected_row[0]][2])
                    self.window[self.Headings[3]].update(self.result[selected_row[0]][3])
            elif event == 'Thêm':
                if self.stts != "Áp dụng":
                    promotion_id = self.window[self.Headings[0]].get()
                    product_id = ProductBiz().get_A_from_B(A="id",nameB="name",valueB=values[self.Headings[1]]) 
                    price = values[self.Headings[2]]
                    status = 0
                    if values[self.Headings[3]] == "Hoạt động":
                        status = 1
                    data = {'promotion_id': promotion_id[2:], 'product_id':product_id,'price': price, 'is_active': status}
                    print(data)
                    add = PromotionDetailsBiz().add_promotion_details(promotions=data)
                    if add != -1:
                        # Hiển thị kết quả
                        sg.popup('Success')
                        self.reset()
                        
                    else:
                        sg.popup('THÊM thất bại')
                        self.reset()
                else:
                    sg.popup("Không được thêm mới khi đã áp dụng")
            elif event == "Sửa":
                if self.stts != "Áp dụng":
                    selected_row = values["-TABLE-"]
                    if selected_row:
                        product_name_old = self.result[selected_row[0]][1]
                        product_id_old = ProductBiz().get_A_from_B(A="id", nameB="name", valueB=product_name_old) 
                        id = ProductBiz().get_A_from_B(A="id", nameB="name", valueB=values[self.Headings[1]])
                        if product_id_old != id:
                            self.window[self.Headings[1]].Update(value=product_name_old)
                            sg.popup("Không được thay đổi mã sản phẩm")
                        else:
                            promotion_id = self.window[self.Headings[0]].get()
                            # product_id = values[self.Headings[1]]
                            price = values[self.Headings[2]]
                            status = 0
                            if values[self.Headings[3]] == "Hoạt động":
                                status = 1
                            data = {'price':price,'is_active': status}
                            flag = any(value == '' for value in data.values())
                            flagUpt = False
                            if flag:
                                sg.popup("Invalid!")
                                flagUpt = True
                            if not flagUpt:
                                update = PromotionDetailsBiz().update_promotion_detais(promotion=data,cond={'promotion_id': promotion_id[2:] , 'product_id':product_id_old})
                                if update != -1:
                                    sg.popup('Update Success')
                                    self.reset()
                                else:
                                    self.reset()
                                    sg.popup("Something error with db")
                    else:
                        sg.popup("Vui lòng chọn sản phẩm cần sửa") 

                else: 
                    sg.popup("Không được sửa mới khi đã áp dụng") 

            elif event == "Xóa":
                if self.stts != "Áp dụng":
                    promotion_id = self.window[self.Headings[0]].get()
                    product_id = ProductBiz().get_A_from_B(A="id", nameB="name", valueB=values[self.Headings[1]])
                    result = PromotionDetailsBiz().delete_promotion(promotion_id=promotion_id[2:] , product_id=product_id)
                    if result:
                        sg.popup("Xóa thành công")
                        self.reset()
                        self.empty()
                    else:
                        sg.popup("Xóa thất bại")
                else: 
                    sg.popup("Không được sửa mới khi đã áp dụng") 
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
            # elif event =='SELECT_PRODUCT':
            #     selectproduct = SelectProductGui()
            #     selectproduct.run()
            #     product_id = selectproduct.product_selected()
            #     self.window[self.Headings[1]].update(product_id)

