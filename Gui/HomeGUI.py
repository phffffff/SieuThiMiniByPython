import PySimpleGUI as sg
from Business.ProductBiz import ProductBiz
from Business.ProductTypesBiz import ProductTypesBiz

class HomeGUI:
    def __init__(self):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')

        # get list product_type
        self.lstProductType = ProductTypesBiz().get_all_product_types(cond={"is_active": 1},fields=["name"])
        self.resultNamePrdctTp = []

        self.cachedProduct = ""

        for item in self.lstProductType:
            item = list(item)
            self.resultNamePrdctTp.append(item[0])
        # kết thúc

        
        # get list product 
        self.lstProduct = ProductBiz().get_all_product(cond={"is_active":1}, fields=['id','name','count','price','discount'])
        self.resultPrdct = []

        for item in self.lstProduct:
            item = list(item)

            item[0] = ProductBiz().to_str_id(id=item[0])# tùy chỉnh ID
            remain = item[3]-item[4] # tính remain
            item.insert(5, remain) #đẩy ramain vào list, lưu ý thứu tự nha
            
            self.resultPrdct.append(item)
        # kết thúc

        self.resultDtlInvc = []

        self.HeadingsProduct = ['Id','Name', 'Count', 'Price', 'Discount','Remaining']
        self.HeadingsDetailInvoices = ['Id','Name', 'Count', 'Price' ,'Discount','Remain Total','Total']
        sg.theme('DarkAmber')  # thiết lập theme
        

        # tạo table
        table_detail_invoices = sg.Table(values=[], headings=self.HeadingsDetailInvoices, justification="center", key='-TABLE_DETAIL_INVOICES-', enable_events=True)

        table_list_product = sg.Table(values=self.resultPrdct, headings=self.HeadingsProduct, justification="center", key='-TABLE_LIST_PRODUCT-', enable_events=True)

        self.spinCount = sg.Spin([i for i in range(10)],initial_value=1, key="-SPIN_COUNT-", enable_events=True, font="blod")
        self.spinSpoint = sg.Spin([i for i in range(10)],initial_value=1, key="-SPIN_SPOINT-", enable_events=True, font="blod")

        # định nghĩa layout cho giao diện
        layout1 = [[sg.Text(text='BILL', font="blod", size=70, justification="center")],
                   [table_detail_invoices]]
        
        layout2 = [[sg.Text(text='PRODUCT LIST', font="blod", size=13, justification="center")],
                   [table_list_product]]

        
        layout3 =[[sg.Text(text='Product type', font="blod", size=13),sg.Combo(values=self.resultNamePrdctTp, key="-COMBO_PRODUCT_TYPE-", enable_events=True)],
                  [sg.Text(text='Count', font="blod", size=13),self.spinCount,sg.Button("ADD"),sg.Button("DELETE")]]
        
        layout4 = [[sg.Text('SubTotal', font="blod", size=13),
                    sg.Text(text="", key="-SUB_TOTAL-", font="blod", size=13)],
                   [sg.Text('Discount', font="blod", size=13),
                    sg.Text(text="", key="-DISCOUNT-", font="blod", size=13),
                    sg.Button("Detail discount")],
                   [sg.Text('Total', font="blod", size=13),
                    sg.Text(text="", key="-TOTAL-", font="blod", size=13)],
                   [sg.Button("Payment")]]
        layout5 = [[sg.Text('Voucher', font="blod", size=13),
                    sg.Input(size=13 , key="-VOUCHER-"),
                    sg.Button("ACP Voucher")],
                   [sg.Text('Membership ID', font="blod", size=13),
                    sg.Input(size=13 , key="-MEMBERSHIP_ID-"),
                    sg.Button("ACP Membership"),
                    sg.Button("View Detail"),
                    sg.Button("Register")],
                   [sg.Text('Point', font="blod", size=13),
                    self.spinSpoint,
                    sg.Button("Change")]]
        layout6 = [[sg.Col(layout3)],[sg.Col(layout2)],[sg.Col(layout4),sg.Col(layout5)]]
        
        layout = [layout1,layout6]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Home', layout)

    def empty(self):
        pass


    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
             # onCLick element of table 
            elif event == "-TABLE_LIST_PRODUCT-":
                selected_row = values["-TABLE_LIST_PRODUCT-"]

                if selected_row:
                    count = self.resultPrdct[selected_row[0]][2]
                    self.spinCount.Update(value=1, values=[i for i in range(0,count+1,1)])
            elif event == "-COMBO_PRODUCT_TYPE-":
                type_id = ProductTypesBiz().get_A_from_B(A="id", nameB="name", valueB=values["-COMBO_PRODUCT_TYPE-"])
                
                newList = ProductBiz().get_all_product(cond={"is_active":1, "product_type_id":type_id},fields=['id','name','count','price','discount'])
                newResult = []
                for item in newList:
                    item = list(item)
                    item[0] = ProductBiz().to_str_id(id=item[0])# tùy chỉnh ID
                    remain = item[3]-item[4] # tính remain
                    item.insert(5, remain) #đẩy ramain vào list, lưu ý thứu tự nha
            
                    newResult.append(item)
                self.window["-TABLE_LIST_PRODUCT-"].update(newResult)
            elif event == "ADD":
                selected_row = values["-TABLE_LIST_PRODUCT-"]
                if selected_row:
                    count = int(values["-SPIN_COUNT-"])
                    if count:
                        self.cachedProduct = self.resultPrdct[selected_row[0]][0]
                        if len(self.resultDtlInvc) == 0:
                            item_click = self.resultPrdct[selected_row[0]].copy()
                            item_click[2] = count
                            total = item_click[2]*item_click[5]
                            item_click.insert(6, total)
                            
                            self.resultDtlInvc.append(item_click)

                        elif len(self.resultDtlInvc) > 0:
                            j = 0
                            for idx in range(len(self.resultDtlInvc)):
                                if self.resultDtlInvc[idx][0] == self.cachedProduct:
                                    j = idx
                                    break
                                j = -1    
                            if j != -1:
                                self.resultDtlInvc[j][2] = int(self.resultDtlInvc[j][2] + count)
                                self.resultDtlInvc[j][6] = self.resultDtlInvc[j][2]*self.resultDtlInvc[j][5]
                            else:
                                item_click = self.resultPrdct[selected_row[0]].copy()
                                item_click[2] = count
                                total = item_click[2]*item_click[5]
                                item_click.insert(6, total)
                                
                                self.resultDtlInvc.append(item_click)

                    countRemain = self.resultPrdct[selected_row[0]][2] - count
                    newResult = []
                    if countRemain > 0:
                        newResult = self.resultPrdct.copy()
                        newResult[selected_row[0]][2] = countRemain
                        self.spinCount.Update(value=1, values=[i for i in range(0,countRemain+1,1)])
                    else:
                        newResult = self.resultPrdct.copy()
                        newResult[selected_row[0]][2] = 0
                        self.spinCount.Update(value=0, values=[0])
                    
                    self.window["-TABLE_DETAIL_INVOICES-"].update(self.resultDtlInvc)
                    self.window["-TABLE_LIST_PRODUCT-"].update(newResult)

            elif event == "DELETE":
                selected_row = values["-TABLE_DETAIL_INVOICES-"]
                if selected_row:
                    newResult = self.resultDtlInvc

                    idProduct = newResult[selected_row[0]][0]
                    count = newResult[selected_row[0]][2]

                    del newResult[selected_row[0]]
                
                    newResultProduct = self.resultPrdct
                    for idx in range(len(newResultProduct)):
                        if newResultProduct[idx][0] == idProduct:
                            newResultProduct[idx][2] = newResultProduct[idx][2] + count

                    self.window["-TABLE_DETAIL_INVOICES-"].update(newResult)
                    self.window["-TABLE_LIST_PRODUCT-"].update(newResultProduct)
                    
        self.window.close()

