import PySimpleGUI as sg
from Business.ProductBiz import ProductBiz
from Business.ProductTypesBiz import ProductTypesBiz
from Business.PurchaseOrdersBiz import PurchaseOrdersBiz
from Business.PurchaseOrderDetailsBiz import PurchaseOrderDetailsBiz
from Business.SuppliersBiz import SuppliersBiz
from Business.ProductType_SupplierBiz import ProductTypeSupplierBiz
from Common.PopupInput import getPopupInput
import datetime

class ImportGUI:
    def __init__(self):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')

        # get list supplier

        self.lstSpplr = SuppliersBiz().get_all_suppliers(cond={"is_active": 1},fields=["id"])
        self.resultNameSpplr = []

        for item in self.lstSpplr:
            item = list(item)
            item[0] = SuppliersBiz().get_A_from_B(A="name", nameB="id", valueB=item[0])
            self.resultNameSpplr.append(item[0])
        # kết thúc       
        
        self.cachedNameSupplier = self.resultNameSpplr[0]
        self.supplier_id = self.lstSpplr[0][0]

        self.total = 0
        
        # get list product_type
        self.lstProductType = ProductTypeSupplierBiz().get_all_product_type_supplier(cond={"supplier_id": self.supplier_id, "is_active":1},fields=["product_type_id"])
        self.resultNamePrdctTp = []

        for item in self.lstProductType:
            item = list(item)
            item[0] = ProductTypesBiz().get_A_from_B(A="name", nameB="id", valueB=item[0])

            self.resultNamePrdctTp.append(item[0])

        self.lstProductTypeWithSupplier = ProductTypeSupplierBiz().get_all_product_type_supplier(cond={"is_active": 1})
        self.resultPrdctTpSpplr = []

        self.cachedProduct = ""

        for item in self.lstProductTypeWithSupplier:
            item = list(item)
            self.resultPrdctTpSpplr.append(item)
        # kết thúc       

        # get list product 
        self.lstProduct = ProductBiz().get_all_product(cond={"is_active":1}, fields=['id','name','price', "product_type_id"])
        self.resultPrdctWthTp = []
        self.resultPrdct = []

        for item in self.lstProduct:
            item = list(item)

            item[0] = ProductBiz().to_str_id(id=item[0])# tùy chỉnh ID
            itemProductType = item.copy()
            
            self.resultPrdct.append(item)
            del itemProductType[3]
            self.resultPrdctWthTp.append(itemProductType)

        # kết thúc

        self.resultPrchslDtl = []

        self.HeadingsProduct = ['Id','Name', 'Price']
        self.HeadingsPurcharDetail = ['Id','Name', 'Count', 'Price' ,'Total']
        sg.theme('DarkAmber')  # thiết lập theme
        

        # tạo table
        table_purchase_detail = sg.Table(values=[], headings=self.HeadingsPurcharDetail, justification="center", key='-TABLE_DETAIL_PURCHASE-', enable_events=True)

        table_list_product = sg.Table(values=self.resultPrdctWthTp, headings=self.HeadingsProduct, justification="center", key='-TABLE_LIST_PRODUCT-', enable_events=True)

        self.spinCount = sg.Spin([i for i in range(10)],initial_value=1, key="-SPIN_COUNT-", enable_events=True, font="blod")

        # định nghĩa layout cho giao diện
        layout1 = [[sg.Text(text='PRODUCT LIST', font="blod", size=13, justification="center")],
                   [table_list_product]]
        layout2 = [[sg.Text(text='PURCHASE BILL', font="blod")],
                   [table_purchase_detail]]
        
        layout3 =[[sg.Text(text='Supplier', font="blod", size=13),sg.Combo(values=self.resultNameSpplr,default_value=self.resultNameSpplr[0],key="-COMBO_SUPPLIER-", enable_events=True)],
                  [sg.Text(text='Product type', font="blod", size=13),sg.Combo(values=self.resultNamePrdctTp, key="-COMBO_PRODUCT_TYPE-", enable_events=True)],
                  [sg.Text(text='Count', font="blod", size=13),self.spinCount,sg.Button("ADD"),sg.Button("DELETE")]]
        
        layout4 = [[sg.Text('Total', font="blod", size=13),
                    sg.Text(text="{} VNĐ".format(self.total), key="-TOTAL-", font="blod", size=13)],
                   [sg.Button("Payment")]]
        
        layout6 = [[sg.Col(layout3)],[sg.Col(layout2)],[sg.Col(layout4)]]
        
        layout = [layout1,layout6]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Home', layout)

    def sum_money(self):
        self.window["-TOTAL-"].update("{}VNĐ".format(float(self.total)))

    def reset(self):
        self.cachedProduct = ''
        self.total = 0
        self.resultPrchslDtl = []

        # get list product 
        self.lstProduct = ProductBiz().get_all_product(cond={"is_active":1}, fields=['id','name','price', "product_type_id"])
        self.resultPrdctWthTp = []
        self.resultPrdct = []

        for item in self.lstProduct:
            item = list(item)

            item[0] = ProductBiz().to_str_id(id=item[0])# tùy chỉnh ID
            itemProductType = item.copy()
            
            self.resultPrdct.append(item)
            del itemProductType[3]
            self.resultPrdctWthTp.append(itemProductType)

        # kết thúc

        self.sum_money()
        self.window["-TABLE_DETAIL_PURCHASE-"].update([])
        self.window["-TABLE_LIST_PRODUCT-"].update([])


    def run(self):
        # xử lý sự kiện cho cửa sổ giao diện
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break
            elif event == "-TABLE_LIST_PRODUCT-":
                selected_row = values["-TABLE_LIST_PRODUCT-"]

                count = 0

                if selected_row:
                    for item in self.resultPrchslDtl:
                        if item[0] == self.resultPrdctWthTp[selected_row[0]][0]:
                            count = item[2]
                            break

                    self.spinCount.Update(value=0, values=[i for i in range(-count,100-count+1,1)])
            elif event == "-COMBO_SUPPLIER-":
                if len(self.resultPrchslDtl) == 0:
                    spplr_id = SuppliersBiz().get_A_from_B(A="id", nameB="name", valueB=values["-COMBO_SUPPLIER-"])
                    self.supplier_id = spplr_id
                    self.cachedNameSupplier = values["-COMBO_SUPPLIER-"]

                    self.lstProductType = ProductTypeSupplierBiz().get_all_product_type_supplier(cond={"supplier_id": spplr_id, "is_active":1},fields=["product_type_id"])
                    self.resultNamePrdctTp = []

                    for item in self.lstProductType:
                        item = list(item)
                        item[0] = ProductTypesBiz().get_A_from_B(A="name", nameB="id", valueB=item[0])

                        self.resultNamePrdctTp.append(item[0])

                    self.window["-COMBO_PRODUCT_TYPE-"].update(values=self.resultNamePrdctTp)
                else: 
                    self.window["-COMBO_SUPPLIER-"].update(value = self.cachedNameSupplier)
                    sg.popup("Chi co the dat hang tai 1 nha cung cap tren 1 lan nhap")

            elif event == "-COMBO_PRODUCT_TYPE-":
                type_id = ProductTypesBiz().get_A_from_B(A="id", nameB="name", valueB=values["-COMBO_PRODUCT_TYPE-"])
                
                # print(type_id)
                self.resultPrdctWthTp = []
                for idx in range(len(self.resultPrdct)):
                    if self.resultPrdct[idx]:
                        if self.resultPrdct[idx][3] == type_id:
                            item = self.resultPrdct[idx].copy()
                            del item[3]
                            self.resultPrdctWthTp.append(item)

                self.window["-TABLE_LIST_PRODUCT-"].update(self.resultPrdctWthTp)

            elif event == "ADD":
                
                selected_row = values["-TABLE_LIST_PRODUCT-"]
                selected_row_purchase = values["-TABLE_DETAIL_PURCHASE-"]

                if selected_row and not selected_row_purchase:
                    count = int(values["-SPIN_COUNT-"])
                    if count:
                        self.cachedProduct = self.resultPrdctWthTp[selected_row[0]][0]
                        if len(self.resultPrchslDtl) == 0:
                            item_click = self.resultPrdctWthTp[selected_row[0]].copy()
                            total = float(item_click[2]*count)
                            item = [item_click[0], item_click[1], count, item_click[2], total]

                            self.resultPrchslDtl.append(item)

                            self.window["-SPIN_COUNT-"].Update(value=1, values=[i for i in range(-count,100-count+1,1)])

                        elif len(self.resultPrchslDtl) > 0:
                            j = 0
                            for idx in range(len(self.resultPrchslDtl)):
                                if self.resultPrchslDtl[idx][0] == self.cachedProduct:
                                    j = idx
                                    break
                                j = -1    
                            if j != -1:
                                self.resultPrchslDtl[j][2] = int(self.resultPrchslDtl[j][2] + count)
                                self.resultPrchslDtl[j][4] = self.resultPrchslDtl[j][2]*self.resultPrchslDtl[j][3]

                                self.window["-SPIN_COUNT-"].Update(value=0, values=[i for i in range(-self.resultPrchslDtl[j][2],100-self.resultPrchslDtl[j][2]+1,1)])
                            else:
                                item_click = self.resultPrdctWthTp[selected_row[0]].copy()
                                total = float(item_click[2]*count)
                                item = [item_click[0], item_click[1], count, item_click[2], total]

                                self.window["-SPIN_COUNT-"].Update(value=0, values=[i for i in range(-count,100-count+1,1)])
                                
                                self.resultPrchslDtl.append(item)

                    
                elif selected_row_purchase and not selected_row:
                    count = int(values["-SPIN_COUNT-"])
                    if count:
                        if len(self.resultPrchslDtl) > 0:
                            self.resultPrchslDtl[selected_row_purchase[0]][2] = int(self.resultPrchslDtl[selected_row_purchase[0]][2] + count)
                            self.resultPrchslDtl[selected_row_purchase[0]][4] = self.resultPrchslDtl[selected_row_purchase[0]][2]*self.resultPrchslDtl[selected_row_purchase[0]][3]

                
                indexFlag = -1
                for idx in range(len(self.resultPrchslDtl)):
                    if self.resultPrchslDtl[idx][2] == 0:
                        indexFlag = idx
                        break
                
                if indexFlag != -1:
                    del self.resultPrchslDtl[indexFlag]

                self.window["-TABLE_DETAIL_PURCHASE-"].update(self.resultPrchslDtl)

                self.total = 0
                if self.resultPrchslDtl:
                    for item in self.resultPrchslDtl:
                        self.total += float(item[4])
                self.sum_money()

            elif event == "DELETE":
                selected_row = values["-TABLE_DETAIL_PURCHASE-"]
                if selected_row:
                    newResult = self.resultPrchslDtl

                    del newResult[selected_row[0]]
                
                    
                    self.total = 0
                    for item in newResult:
                        self.total += float(item[3])
                    

                    self.window["-TABLE_DETAIL_PURCHASE-"].update(newResult)
                    
                    self.sum_money()

            elif event == "-TABLE_DETAIL_PURCHASE-":
                selected_row_purchase = values["-TABLE_DETAIL_PURCHASE-"]

                if selected_row_purchase:
                    itemClick = self.resultPrchslDtl[selected_row_purchase[0]]

                    count = itemClick[2]
                   
                    self.spinCount.Update(value=0, values=[i for i in range(-count,100-count+1,1)])

            elif event == "Payment":
                id = PurchaseOrdersBiz().get_new_id()
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                supplier_id = self.supplier_id
                total_price = self.total
                isActive = 1 

                purchase = {'id':id[2:],"supplier_id": supplier_id, 'date':date, 'total_price':total_price, 'is_active': isActive}

                for key in list(purchase.keys()):
                    if purchase[key] == '' or purchase[key] is None:
                        
                        del purchase[key]

                add = PurchaseOrdersBiz().add_purchase_orders(data=purchase)

                if add != -1:
                    for product in self.resultPrchslDtl:
                        purchase_detail = {'purchase_order_id':id[2:],'product_id':product[0][2:],'product_name':product[1],'count': product[2],'price': product[3],'subtotal':product[4],'is_active':1}

                        flagIvd = PurchaseOrderDetailsBiz().add_purchase_order_details(data=purchase_detail)
                        if flagIvd == -1:
                            break
                        
                        flagPrdct = ProductBiz().update_payment(count=purchase_detail["count"],cond={'id':purchase_detail["product_id"]},key="increase")
                        if flagPrdct == -1:
                            break
                    self.reset()

                    
        self.window.close()

