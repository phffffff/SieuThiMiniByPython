import PySimpleGUI as sg
from Business.ProductBiz import ProductBiz
from Entity.ProductEntity import ProductEntity

class ProductGUI:
    def __init__(self):
        biz = ProductBiz()

        self.Headings = ['ID', 'Tên Sản phẩm', 'số lượng', 'Giá', 'Giảm', 'Tên loại sản phẩm']
        self.lstProduct = biz.get_all_product()
        self.result = []
        print(self.lstProduct)
        for item in self.lstProduct:
            self.result.append(list(item))
        

        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('DANH SÁCH SẢN PHẨM',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Chọn từ khóa search:',size=15),sg.Combo(['ID','NAME','COUNT','PRICE','DISCOUNT','PRODUCT_TYPE_ID'], key='-KEY-'),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22),sg.Button('SEARCH')],
                      [sg.Text('Mã sản phẩm :',size=15), sg.Input(key=self.Headings[0])],
                      [sg.Text('Tên sản phẩm:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Số lượng:',size=15), sg.Input(key=self.Headings[2])],
                      [sg.Text('Giá tiền:',size=15), sg.Input(key=self.Headings[3])],
                      [sg.Text('Tên loại sản phẩm:',size=15), sg.Input(key=self.Headings[5])],
                      [sg.Button('Tạo mới'), sg.Button('Sửa'),sg.Button('Đổ dữ liệu'), sg.Button('Xóa'),sg.Button('Thêm')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Sản phẩm trong siêu thị', layout)
        self.window.read()

    def empty(self):
        self.window[self.Headings[0]].update('')
        self.window[self.Headings[1]].update('')
        self.window[self.Headings[2]].update('')
        self.window[self.Headings[3]].update('')
        self.window[self.Headings[4]].update('')
        self.window[self.Headings[5]].update('')

    def run(self):
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            # elif event == 'Tạo Mới':
            #     biz = ProductBiz()
            #     id = values[self.Headings[0]]
            #     name = values[self.Headings[1]]
            #     count = values[self.Headings[2]]
            #     price = values[self.Headings[3]]
            #     discount = values[self.Headings[4]]
            #     typeid = values[self.Headings[5]]

            #     add == biz.add({'id':id,'name':name,'count':count,'price':price,'discount':discount,'product_type_id':typeid,'is_active':1})

            #     if add:
            #         sg.popup('THÊM THÀNH CÔNG')
            #         self.result.append([values[self.Headings[0]], values[self.Headings[1]], values[self.Headings[2]], values[self.Headings[3]], values[self.Headings[4]], values[self.Headings[5]]])
            #         self.window['-TABLE-'].update(values=self.result)
            #         self.empty()

            # elif event == "Đổ dữ liệu":
            #     editRow = values['-TABLE-'][0]
            #     sg.popup('Đổ dữ liệu thành công')
            #     for i in range(6):
            #         self.window[self.Headings[i]].update(value=self.result[editRow][i])

            # elif event == "Xóa":

            #     biz = ProductBiz()
            #     id = values[self.Headings[0]]

            #     result = biz.update({'is_active': 0}, {'id': id})
            #     if result:
            #         sg.popup("Xóa thành công")
            #         del self.result[values['-TABLE-'][0]]
            #         self.window['-TABLE-'].update(values=self.result)
            #         self.empty()
            #     else:
            #         sg.popup("Xóa thất bại")
            # elif event == 'SEARCH':
            #     key = values['-KEY-']
            #     biz = ProductBiz()
            #     id = values['-CONTENT-']
            #     if key == 'ID':
            #         self.result = biz.get_id(id)
            #         if self.result:
            #             sg.popup("Tìm thành công")
            #             self.window['-TABLE-'].update(values=self.result)
            #         else:
            #             sg.popup("Tìm thất bại")

            #     elif key == 'NAME':
            #         self.result = biz.get_name(id)
            #         if self.result:
            #             sg.popup("Tìm thành công")
            #             self.window['-TABLE-'].update(values=self.result)
            #         else:
            #             sg.popup("Tìm thất bại")
            #     elif key == 'COUNT':
            #         self.result = biz.get_count(id)
            #         if self.result:
            #             sg.popup("Tìm thành công")
            #             self.window['-TABLE-'].update(values=self.result)
            #         else:
            #             sg.popup("Tìm thất bại")
            #     elif key == 'PRICE':
            #         self.result = biz.get_price(id)
            #         if self.result:
            #             sg.popup("Tìm thành công")
            #             self.window['-TABLE-'].update(values=self.result)
            #         else:
            #             sg.popup("Tìm thất bại")
            #     elif key == 'DISCOUNT':
            #         self.result = biz.get_discount(id)
            #         if self.result:
            #             sg.popup("Tìm thành công")
            #             self.window['-TABLE-'].update(values=self.result)
            #         else:
            #             sg.popup("Tìm thất bại")
            #     elif key == 'PRODUCT_TYPE_ID':
            #         self.result = biz.get_product_type_id(id)
            #         if self.result:
            #             sg.popup("Tìm thành công")
            #             self.window['-TABLE-'].update(values=self.result)
            #         else:
            #             sg.popup("Tìm thất bại")
            #     else:
            #         biz = ProductBiz()
            #         self.dulieu = biz.get_all_prodcut()
            #         self.result = [[]]
            #         for self.row in self.dulieu:
            #             self.result.append(list(self.row))
            #         self.window['-TABLE-'].update(values=self.result)

        self.window.close()

