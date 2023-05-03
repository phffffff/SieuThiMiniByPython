import PySimpleGUI as sg

from Business.PurchaseOrderDetailsBiz import PurchaseOrderDetailsBiz
from Business.PurchaseOrdersBiz import PurchaseOrdersBiz
from Business.ProductBiz import ProductBiz
from Entity.PuchaseDetailEntity import PurchaseDetail


class PurchaseDetailsGui:
    def __init__(self,purchase_id):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        self.id = purchase_id
        print(self.id)

        self.lst = PurchaseOrderDetailsBiz().get_all_purchase_order_details(cond={"purchase_order_id":purchase_id,"is_active":1})
        self.result = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.lst:
            item = list(item)
            item[0] = PurchaseOrdersBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[1] = ProductBiz().to_str_id(id=item[1])
            if item[6] == 1:
                item[6] = "Hoạt động"
            else:
                item[6] = "Không hoạt động"
            self.result.append(item)

        self.Headings = ['Purchase Order Id', 'Product Id','Product Name','Count' ,'Price','Total', 'Status']
        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện
        layout1 = [[sg.Text('Purchase Order Id:', size=15),sg.Text(text='',size=20 , key=self.Headings[0])],
                   [sg.Text('Product Id:', size=15),sg.Text(text='',  key=self.Headings[1])],
                   [sg.Text('Product Name:', size=15),sg.Text(text='',  key=self.Headings[2])],
                   [sg.Text('Count:', size=15), sg.Text(text='',key=self.Headings[3])],
                   [sg.Text('Price:', size=15), sg.Text(text='',key=self.Headings[4])],
                   [sg.Text('Total:', size=15), sg.Text(text='',key=self.Headings[5])],
                   [sg.Text('Status:', size=15), sg.Text(text='',size=20,key=self.Headings[6] )],
                   ]
        # tạo table
        table = sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', enable_events=True)
        layout2 = [[sg.Text('PURCHASE ORDER DETAIL MANAGEMENT', font="blod", justification="center"),sg.Button(image_filename='Picture/refresh-30.png',key='REFRESH')], [table]]
        layout3 = [[sg.Text('Search with:', size=15), sg.Combo([ 'purchase_order_id', 'product_id', 'product_name', 'count','price','total','status'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22, enable_events=True)]]
        layout = [[layout1],[layout3], [sg.Column(layout2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('purchase order details', layout)

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
                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row[0]][idx])

            elif event == 'REFRESH':
                self.window["-CONTENT-"].update('')
                self.lst = PurchaseOrderDetailsBiz().get_all_purchase_order_details(cond={"purchase_order_id":self.id,"is_active":1})
                self.result = []
                # for i in self.dulieu:
                #     self.result.append(list(i))
                for item in self.lst:
                    item = list(item)
                    item[0] = PurchaseOrdersBiz().to_str_id(id=item[0])  # tùy chỉnh ID
                    item[1] = ProductBiz().to_str_id(id=item[1])
                    if item[6] == 1:
                        item[6] = "Hoạt động"
                    else:
                        item[6] = "Không hoạt động"
                    self.result.append(item)
                self.window['-TABLE-'].update(self.result)
            
            elif event == '-CONTENT-':
                value_search = values['-CONTENT-']
                search_with = values["-KEY-"]
                # binding list to listpromotion
                Entitys = []
                for item in self.result:
                    entity = PurchaseDetail(*item)
                    Entitys.append(entity)
                result = []
                for idx in range(len(Entitys)):
                    if value_search in str(getattr(Entitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window['-TABLE-'].update(result)

