import PySimpleGUI as sg
from Business.AccountsBiz import AccountsBiz
from Business.StaffsBiz import StaffsBiz
from Business.ProductTypesBiz import ProductTypesBiz
from Business.ProductBiz import ProductBiz
from Business.PromotionsBiz import PromotionsBiz
from Business.CoupousBiz import CoupousBiz
from Business.SuppliersBiz import SuppliersBiz
from Business.MembershipsBiz import MembershipsBiz
from Business.InvoicesBiz import InvoicesBiz
from Business.PurchaseOrdersBiz import PurchaseOrdersBiz

from Entity.InvoiceEntity import InvoicesSearch
from Entity.InvoiceEntity import InvoicesValue

from Entity.PurchaseOrderEntity import PurchaseSearch
from Entity.PurchaseOrderEntity import PurchaseValue

from Gui.InvoiceDetailGui import InvoicesDetailsGui
from Gui.PurchaseDetailGui import PurchaseDetailsGui
import datetime
class Statistical:
    def __init__(self):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        default_with =900
        default_height = 500

        self.ttAccount = AccountsBiz().get_info_account()
        self.infoAccount = 'Số tài khoản được cấp: {}\nSố tài khoản hoạt động: {}\nSố tài khoản không hoạt động:{}'.format(self.ttAccount["cap"],self.ttAccount["hoatdong"],self.ttAccount["kohoatdong"])

        self.ttStaff = StaffsBiz().get_info_staff()
        self.infoStaff = 'Tổng số nhân viên hoạt động: {}\nTổng số nhân viên thôi làm:{}'.format(self.ttStaff["hoatdong"],self.ttStaff["kohoatdong"])

        self.ttPrdctTp = ProductTypesBiz().get_info_prdctTp()
        self.infoPrdctTp = 'Tổng số loại sản phẩm tồn tại: {}\nTổng số loại sản phẩm không tồn tại:{}'.format(self.ttPrdctTp["hoatdong"],self.ttPrdctTp["kohoatdong"])

        self.ttPrdct = ProductBiz().get_info_prdct()
        self.infoPrdct = 'Tổng số sản phẩm tồn tại: {}\nTổng số sản phẩm không tồn tại:{}'.format(self.ttPrdct["hoatdong"],self.ttPrdct["kohoatdong"])

        self.ttSpplr = SuppliersBiz().get_info_spplr()
        self.infoSpplr = 'Tổng số nhân viên hoạt động: {}\nTổng số nhân viên thôi làm:{}'.format(self.ttSpplr["hoatdong"],self.ttSpplr["kohoatdong"])

        self.ttPromotion = PromotionsBiz().get_info_promotion()
        self.infoPromotion = 'Tổng số ct khuyến mãi đã tạo: {}\nTổng số ct khuyến mãi đã xóa:{}\nCT Khuyến mãi đang áp dụng là: {}'.format(self.ttPromotion["hoatdong"],self.ttPromotion["kohoatdong"],self.ttPromotion["apdung"])

        self.ttCoupou = CoupousBiz().get_info_coupou()
        self.infoCoupou = 'Tổng số voucher đã tồn tại: {}\nTổng số voucher đã đã xóa:{}\nTổng số voucher đã chưa sử dụng: {}\nTổng số voucher đã sử dụng: {}'.format(self.ttCoupou["hoatdong"],self.ttCoupou["kohoatdong"],self.ttCoupou["sudung"],self.ttCoupou["chuasudung"])

        self.ttMem = MembershipsBiz().get_info_mem()
        self.infoMem = 'Tổng số thành viên tồn tại: {}\nSố thành viên ngừng sử dụng:{}'.format(self.ttMem["hoatdong"],self.ttMem["kohoatdong"])
        


        # TABLAYOUT Tổng kết
        self.key_statistical = ['accounts','staff','memberships','product_types','products','suppliers','coupous','promotions']
        layout_00 = [[sg.Text('Tài khoản',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoAccount,justification='center' , font=13, key=self.key_statistical[0])]]
        layout_01 = [[sg.Text('Nhân viên',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoStaff,justification='center', font=13 , key=self.key_statistical[1])]]
        layout_02 = [[sg.Text('Thành viên',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoMem,justification='center', font=13, key=self.key_statistical[2])]]
        layout_10 = [[sg.Text('Loại Sản Phẩm',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoPrdctTp,justification='center', font=13, key=self.key_statistical[3])]]
        layout_11 = [[sg.Text('Sản phẩm',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoPrdct,justification='center', font=13, key=self.key_statistical[4])]]
        layout_12 = [[sg.Text('Nhà cung cấp',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoSpplr,justification='center', font=13, key=self.key_statistical[5])]]
        layout_20 = [[sg.Text('Phiếu giảm giá',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoCoupou,justification='center', font=13, key=self.key_statistical[6])]]
        layout_21 = [[sg.Text('Chương trình khuyến mãi',font=17)],[sg.Multiline(disabled=True,size=(50,40),default_text=self.infoPromotion,justification='center', font=13, key=self.key_statistical[7])]]
        frame_size = (int(default_with/3) , int(default_height/3)) #đặt kích thước chung trừ chương trình khuyến mãi
        # Tạo layout Tổng quát
        grid_layout = [
            [sg.Frame('',layout_00 , size=frame_size), sg.Frame('',layout_01, size=frame_size), sg.Frame('',layout_02, size=frame_size)],
            [sg.Frame('',layout_10, size=frame_size), sg.Frame('',layout_11, size=frame_size), sg.Frame('',layout_12, size=frame_size)],
            [sg.Frame('',layout_20, size=frame_size), sg.Frame('',layout_21 , size=(int(default_with*2/3),int(default_height/5)))]
        ]
        # Giao diện tab Hóa đơn
        frame_size_order = (int(default_with/4) , int(default_height/8))
        top_01 = [[sg.Input('',key='DATE_FROM_ORDER',size=12,justification='center',enable_events=True), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target='DATE_FROM_ORDER',size=(24,24))]]
        top_02 = [[sg.Combo(['id',"staff_name","membership_name"] , key='TYPE_SEARCH')]]
        top_03 = [[sg.Input('',key='CONTENT_SEARCH',enable_events=True)]]
        top_04 = [[sg.Input('',key='DATE_TO_ORDER',size=12,enable_events=True), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target='DATE_TO_ORDER',size=(24,24))]]
        top_11 = [[sg.Button( image_filename='Picture/refresh-30.png',key='REFRESH',pad=(10 ,10))]]
        top_12 = [[sg.Combo(['total_price','discount','remain_price','point'] , key='PRICE_SEARCH')]]
        top_13 = [[sg.Input('',key='PRICE_FROM_SEARCH',enable_events=True)]]
        top_14 = [[sg.Input('',key='PRICE_TO_SEARCH',enable_events=True)]]
        top_15 = [[sg.Button( image_filename='Picture/preview-file-24.png',key='REVIEW' , image_size=(30,30))]]

        # Tạo table
        self.key_statistical_order = ['Id Invoice','Date','Staff','Membership','Total Price ','Discount','Remain Price','Coupou','Point']
        
        self.lstInvoice = InvoicesBiz().get_all_invoices(cond={"is_active":1})
        self.data_order = []
        for item in self.lstInvoice:
            item = list(item)
            item[0] = InvoicesBiz().to_str_id(item[0])
            item[2] = StaffsBiz().get_A_from_B(A="name",nameB="id",valueB=item[2])
            item[3] = MembershipsBiz().get_A_from_B(A="name",nameB="id",valueB=item[3])
            item[7] = CoupousBiz().get_A_from_B(A="coupou_code",nameB="id",valueB=item[7])

            i = item.copy()
            del i[9]

            self.data_order.append(i)

        self.lstPurchase = PurchaseOrdersBiz().get_all_purchase_orders(cond={"is_active":1})
        self.data_purchase = []

        for item in self.lstPurchase:
            item = list(item)
            item[0] = PurchaseOrdersBiz().to_str_id(item[0])
            item[1] = SuppliersBiz().to_str_id(id=item[1])
            name = SuppliersBiz().get_A_from_B(A="name",nameB="id",valueB=item[1][2:])
            item.insert(2, name)
            i = item.copy()
            del i[5]
            
            self.data_purchase.append(i)

        table_order = [[sg.Table(values=self.data_order, headings=self.key_statistical_order, justification="center", key='-TABLE_ORDER-', enable_events=True ,vertical_scroll_only=False)]]

        # bottom  order
        bottom_01 = [[sg.Text('Giá trị lớn nhất của hóa đơn trong danh sách')],
                     [sg.Text(text=InvoicesBiz().get_invoice_max_price(), size=10, justification='center', key='ORDER_MAX')]]
        bottom_02 = [[sg.Text('Giá trị nhỏ nhất của hóa đơn trong danh sách')],
                     [sg.Text(text=InvoicesBiz().get_invoice_min_price(), size=10, justification='center', key='ORDER_MIN')]]
        bottom_03 = [[sg.Text('Doanh thu năm hiện tại')],
                     [sg.Text(text=InvoicesBiz().get_invoice_by_year(), size=10, justification='center', key='REVENUE_YEAR')]]
        bottom_04 =[[sg.Text('Doanh thu tháng hiện tại ')],
                     [sg.Text(text=InvoicesBiz().get_invoice_by_month(), size=10, justification='center', key='REVENUE_MONTH')]]
        bottom_05 = [[sg.Text('Doanh thu ngày hiện tại')],
                     [sg.Text(text=InvoicesBiz().get_invoice_by_day(), size=10, justification='center', key='REVENUE_DAY')]]
        bottom_size = (int(default_with/5) , int(default_height/10))
        #main thống kê hóa đơn
        statistical_order =[[sg.Frame('Từ ngày',top_01 ,size=frame_size_order ,element_justification='center' ) ,sg.Frame('Thống kê theo',top_02,size=(int(default_with/8) , int(default_height/8)),element_justification='center'),sg.Frame('Tìm kiếm ',top_03,size=frame_size_order ,element_justification='center') ,sg.Frame('Đến ngày',top_04,size=frame_size_order ,element_justification='center')],
                    [sg.Frame('',top_11,size=frame_size_order , element_justification='center',border_width=0),sg.Frame('Thống kê theo',top_12,size=(int(default_with/8) , int(default_height/8)),element_justification='center') ,
                     sg.Frame('Từ',top_13 ,size=(int(default_with/8) , int(default_height/8)),element_justification='center'), sg.Frame('Đến',top_14 ,size=(int(default_with/8) , int(default_height/8)),element_justification='center'),
                     sg.Frame('',top_15,size=frame_size_order , element_justification='center' , border_width=0)],
                     [sg.Frame('',table_order ,size= (int(default_with) , int(default_height/3)))],
                    [  sg.Frame('',bottom_01 , size=(int(default_with/6.5) , int(default_height/10))) ,sg.Frame('',bottom_02 , size=(int(default_with/6.5) , int(default_height/10))),sg.Frame('',bottom_03 , size=bottom_size),
                       sg.Frame('',bottom_04 , size=bottom_size) ,sg.Frame('',bottom_05 , size=bottom_size)]
                        ]


        # Tạo layout cho Thống kê đơn nhập
        frame_size_entry  = (int(default_with / 4), int(default_height / 8))
        top_entry_01 = [[sg.Input('', key='DATE_FROM_ENTRY',enable_events=True, size=12, justification='center'),
                   sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d',
                                     target='DATE_FROM_ENTRY', size=(24, 24))]]
        top_entry_02 = [[sg.Combo(['id','supplier_id','name_supplier'], key='TYPE_ENTRY_SEARCH')]]
        top_entry_03 = [[sg.Input('', key='CONTENT_ENTRY_SEARCH',enable_events=True)]]
        top_entry_04 = [[sg.Input('', key='DATE_TO_ENTRY',enable_events=True, size=12),
                   sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d',
                                     target='DATE_TO_ENTRY', size=(24, 24))]]
        top_entry_11 = [[sg.Button(image_filename='Picture/refresh-30.png', key='REFRESH_ENTRY', pad=(10, 10))]]
        top_entry_13 = [[sg.Input('', key='PRICE_ENTRY_FROM_SEARCH',enable_events=True)]]
        top_entry_14 = [[sg.Input('', key='PRICE_ENTRY_TO_SEARCH',enable_events=True)]]
        top_entry_15 = [[sg.Button(image_filename='Picture/preview-file-24.png', key='REVIEW_ENTRY', image_size=(30, 30))]]

        # Tạo table
        self.key_statistical_entry = ['Id' ,'Supplier Id' ,'Supplier Name' ,'Date' , 'Total Price']
        table_entry = [[sg.Table(values=self.data_purchase, headings=self.key_statistical_entry, justification="center",key='-TABLE_ENTRY-', enable_events=True,hide_vertical_scroll=True)]]

        # bottom  order
        bottom_entry_01 = [[sg.Text('Chi phí đơn hàng lớn nhất trong danh sách')],
                     [sg.Text(text=PurchaseOrdersBiz().get_purchase_max_price(), size=10, justification='center', key='ENTRY_MAX')]]
        bottom_entry_02 = [[sg.Text('Chi phí đơn hàng nhỏ nhất trong danh sách')],
                     [sg.Text(text=PurchaseOrdersBiz().get_purchase_min_price(), size=10, justification='center', key='ENTRY_MIN')]]
        bottom_entry_03 = [[sg.Text('Chí phí nhập năm hiện tại')],
                     [sg.Text(text=PurchaseOrdersBiz().get_purchase_by_year(), size=10, justification='center', key='ENTRY_YEAR')]]
        bottom_entry_04 = [[sg.Text('Chi phí nhập tháng hiện tại ')],
                     [sg.Text(text=PurchaseOrdersBiz().get_purchase_by_month(), size=10, justification='center', key='ENTRY_MONTH')]]
        bottom_entry_05 = [[sg.Text('Chi phí nhập ngày hiện tại')],
                     [sg.Text(text=PurchaseOrdersBiz().get_purchase_by_day(), size=10, justification='center', key='ENTRY_DAY')]]
        bottom_entry_size = (int(default_with / 5), int(default_height / 10))
        # main thống kê hóa đơn
        statistical_entry = [[sg.Frame('Từ ngày', top_entry_01, size=frame_size_entry, element_justification='center'),
                              sg.Frame('Thống kê theo', top_entry_02, size=(int(default_with / 8), int(default_height / 8)),
                                       element_justification='center'),
                              sg.Frame('Tìm kiếm ', top_entry_03, size=frame_size_entry, element_justification='center'),
                              sg.Frame('Đến ngày', top_entry_04, size=frame_size_entry, element_justification='center')],
                             [sg.Frame('', top_entry_11, size=frame_size_entry, element_justification='center',
                                       border_width=0),
                              sg.Frame('Tổng tiền từ', top_entry_13, size=(int(default_with / 8), int(default_height / 8)),
                                       element_justification='center'),
                              sg.Frame('Đến', top_entry_14, size=(int(default_with / 8), int(default_height / 8)),
                                       element_justification='center'),
                              sg.Frame('', top_entry_15, size=frame_size_entry, element_justification='center',
                                       border_width=0)],
                             [sg.Frame('', table_entry, size=(int(default_with/1.5), int(default_height / 3)))],
                             [sg.Frame('', bottom_entry_01, size=(int(default_with / 6.6 + 2), int(default_height / 10))),
                              sg.Frame('', bottom_entry_02, size=(int(default_with / 6.6 +2), int(default_height / 10))),
                              sg.Frame('', bottom_entry_03, size=bottom_entry_size),
                              sg.Frame('', bottom_entry_04, size=bottom_entry_size), sg.Frame('', bottom_entry_05, size=bottom_entry_size)]
                             ]
        # Tạo TabGroup
        tabgroup_layout = [
            [sg.Tab('Tổng quát', grid_layout)],
            [sg.Tab('Hóa đơn', statistical_order)],
            [sg.Tab('Đơn nhập',statistical_entry)]
        ]

        # Tạo giao diện chính
        main_layout = [
            [sg.TabGroup(tabgroup_layout,size=(default_with,default_height))]
        ]

        # Tạo cửa sổ
        self.window = sg.Window('Tab Layout', main_layout ,size=(default_with,default_height))

    def empty(self):
        self.window["DATE_FROM_ORDER"].update('')
        self.window["DATE_TO_ORDER"].update('')
        self.window["CONTENT_SEARCH"].update('')
        self.window["PRICE_FROM_SEARCH"].update('')
        self.window["PRICE_TO_SEARCH"].update('')

    def empty_entry(self):
        self.window["DATE_FROM_ENTRY"].update('')
        self.window["DATE_TO_ENTRY"].update('')
        self.window["CONTENT_ENTRY_SEARCH"].update('')
        self.window["PRICE_ENTRY_FROM_SEARCH"].update('')
        self.window["PRICE_ENTRY_TO_SEARCH"].update('')

    def run(self):
        # Vòng lặp chính
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "REFRESH":
                self.empty()
                self.window["ORDER_MAX"].update(InvoicesBiz().get_invoice_max_price())
                self.window["ORDER_MIN"].update(InvoicesBiz().get_invoice_min_price())
                self.window["REVENUE_YEAR"].update(InvoicesBiz().get_invoice_by_year())
                self.window["REVENUE_MONTH"].update(InvoicesBiz().get_invoice_by_month())
                self.window["REVENUE_DAY"].update(InvoicesBiz().get_invoice_by_day())
                self.lstInvoice = InvoicesBiz().get_all_invoices()
                self.data_order = []
                for item in self.lstInvoice:
                    item = list(item)
                    item[0] = InvoicesBiz().to_str_id(item[0])
                    item[2] = StaffsBiz().get_A_from_B(A="name",nameB="id",valueB=item[2])
                    item[3] = MembershipsBiz().get_A_from_B(A="name",nameB="id",valueB=item[3])
                    item[7] = CoupousBiz().get_A_from_B(A="coupou_code",nameB="id",valueB=item[7])

                    i = item.copy()
                    del i[9]

                    self.data_order.append(i)

                self.window["-TABLE_ORDER-"].update(self.data_order)

            elif event == "DATE_FROM_ORDER":
                date_from = values["DATE_FROM_ORDER"]
                date_to = values["DATE_TO_ORDER"]
                if date_from and date_to:
                    date_from_obj = datetime.datetime.strptime(date_from, "%Y-%m-%d").date()
                    date_to_obj = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
                    result = []
                    for item in self.data_order:
                        if item[1] > date_from_obj and item[1] < date_to_obj:
                            result.append(item)

                    self.window["-TABLE_ORDER-"].update(result)

            elif event == "DATE_FROM_ENTRY":
                date_from = values["DATE_FROM_ENTRY"]
                date_to = values["DATE_TO_ENTRY"]
                if date_from and date_to:
                    date_from_obj = datetime.datetime.strptime(date_from, "%Y-%m-%d").date()
                    date_to_obj = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
                    result = []
                    for item in self.data_purchase:
                        if item[3] > date_from_obj and item[3] < date_to_obj:
                            result.append(item)

                    self.window["-TABLE_ENTRY-"].update(result)
                
            elif event == "DATE_TO_ORDER":
                date_from = values["DATE_FROM_ORDER"]
                date_to = values["DATE_TO_ORDER"]
                if date_from and date_to:
                    date_from_obj = datetime.datetime.strptime(date_from, "%Y-%m-%d").date()
                    date_to_obj = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
                    result = []
                    for item in self.data_order:
                        if item[1] > date_from_obj and item[1] < date_to_obj:
                            result.append(item)

                    self.window["-TABLE_ORDER-"].update(result)
            elif event == "DATE_TO_ENTRY":
                date_from = values["DATE_FROM_ENTRY"]
                date_to = values["DATE_TO_ENTRY"]
                if date_from and date_to:
                    date_from_obj = datetime.datetime.strptime(date_from, "%Y-%m-%d").date()
                    date_to_obj = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
                    result = []
                    for item in self.data_purchase:
                        if item[3] > date_from_obj and item[3] < date_to_obj:
                            result.append(item)

                    self.window["-TABLE_ENTRY-"].update(result)

            elif event == "PRICE_FROM_SEARCH":
                search_with = values["PRICE_SEARCH"]

                value_from = values["PRICE_FROM_SEARCH"]
                value_to = values["PRICE_TO_SEARCH"]

                if value_from and value_to:
                    Entitys = []
                    for item in self.data_order:
                        entity = InvoicesValue(item[4],item[5],item[6],item[8])
                        Entitys.append(entity)

                    result = []
                    for idx in range(len(Entitys)):
                        if int(value_from) < int(getattr(Entitys[idx], search_with)) and int(getattr(Entitys[idx], search_with)) < int(value_to) :
                            result.append(self.data_order[idx])

                    self.window["-TABLE_ORDER-"].update(result)
                else:
                    self.window["-TABLE_ORDER-"].update(self.data_order)

            elif event == "PRICE_TO_SEARCH":
                search_with = values["PRICE_SEARCH"]

                value_from = values["PRICE_FROM_SEARCH"]
                value_to = values["PRICE_TO_SEARCH"]

                if value_from and value_to:
                    Entitys = []
                    for item in self.data_order:
                        entity = InvoicesValue(item[4],item[5],item[6],item[8])
                        Entitys.append(entity)

                    result = []
                    for idx in range(len(Entitys)):
                        if int(value_from) < int(getattr(Entitys[idx], search_with)) and int(getattr(Entitys[idx], search_with)) < int(value_to) :
                            result.append(self.data_order[idx])

                    self.window["-TABLE_ORDER-"].update(result)
                else:
                    self.window["-TABLE_ORDER-"].update(self.data_order)

            elif event == "PRICE_ENTRY_FROM_SEARCH":
                value_from = values["PRICE_ENTRY_FROM_SEARCH"]
                value_to = values["PRICE_ENTRY_TO_SEARCH"]

                if value_from and value_to:
                    Entitys = []
                    for item in self.data_order:
                        entity = InvoicesValue(item[4])
                        Entitys.append(entity)

                    result = []
                    for idx in range(len(Entitys)):
                        if int(value_from) < int(getattr(Entitys[idx], search_with)) and int(getattr(Entitys[idx], search_with)) < int(value_to) :
                            result.append(self.data_order[idx])

                    self.window["-TABLE_ENTRY-"].update(result)
                else:
                    self.window["-TABLE_ENTRY-"].update(self.data_purchase)

            elif event == "PRICE_ENTRY_TO_SEARCH":
                value_from = values["PRICE_ENTRY_FROM_SEARCH"]
                value_to = values["PRICE_ENTRY_TO_SEARCH"]

                if value_from and value_to:
                    Entitys = []
                    for item in self.data_purchase:
                        entity = PurchaseValue(item[4])
                        Entitys.append(entity)

                    result = []
                    for idx in range(len(Entitys)):
                        if int(value_from) < int(getattr(Entitys[idx], 'total_price')) and int(getattr(Entitys[idx], 'total_price')) < int(value_to) :
                            result.append(self.data_purchase[idx])

                    self.window["-TABLE_ENTRY-"].update(result)
                else:
                    self.window["-TABLE_ENTRY-"].update(self.data_purchase)

            elif event == "CONTENT_SEARCH":
                value_search = values["CONTENT_SEARCH"]
                search_with = values["TYPE_SEARCH"]

                # binding list to listProduct
                Entitys = []
                for item in self.data_order:
                    entity = InvoicesSearch(item[0],item[2],item[3])
                    Entitys.append(entity)

                result = []
                for idx in range(len(Entitys)):
                    if value_search in str(getattr(Entitys[idx], search_with)):
                        result.append(self.data_order[idx])

                self.window["-TABLE_ORDER-"].update(result)


            elif event == "CONTENT_ENTRY_SEARCH":
                value_search = values["CONTENT_ENTRY_SEARCH"]
                search_with = values["TYPE_ENTRY_SEARCH"]

                # binding list to listProduct
                Entitys = []
                for item in self.data_purchase:
                    entity = PurchaseSearch(item[0],item[1],item[2])
                    Entitys.append(entity)

                result = []
                for idx in range(len(Entitys)):
                    if value_search in str(getattr(Entitys[idx], search_with)):
                        result.append(self.data_purchase[idx])

                self.window["-TABLE_ENTRY-"].update(result)

            elif event == "REVIEW":
                selector_row = values['-TABLE_ORDER-']
                if selector_row:
                    id = self.data_order[selector_row[0]][0]
                    
                    invoicesDetailsGui = InvoicesDetailsGui(invoice_id=id[2:])
                    invoicesDetailsGui.run()
                else:
                    sg.popup("Vui lòng nhấn chọn hóa đơn để xem chi tiết")

            elif event == "REVIEW_ENTRY":
                selector_row = values['-TABLE_ENTRY-']
                if selector_row:
                    id = self.data_purchase[selector_row[0]][0]
                    
                    purchaseDetailsGui = PurchaseDetailsGui(purchase_id=id[2:])
                    purchaseDetailsGui.run()
                else:
                    sg.popup("Vui lòng nhấn chọn hóa đơn để xem chi tiết")

            elif event == "REFRESH_ENTRY":
                self.empty_entry()
                self.window["ENTRY_MAX"].update(PurchaseOrdersBiz().get_purchase_max_price())
                self.window["ENTRY_MIN"].update(PurchaseOrdersBiz().get_purchase_min_price())
                self.window["ENTRY_YEAR"].update(PurchaseOrdersBiz().get_purchase_by_year())
                self.window["ENTRY_MONTH"].update(PurchaseOrdersBiz().get_purchase_by_month())
                self.window["ENTRY_DAY"].update(PurchaseOrdersBiz().get_purchase_by_day())
                self.lstPurchase = PurchaseOrdersBiz().get_all_purchase_orders(cond={"is_active":1})
                self.data_purchase = []

                for item in self.lstPurchase:
                    item = list(item)
                    item[0] = PurchaseOrdersBiz().to_str_id(item[0])
                    item[1] = SuppliersBiz().to_str_id(id=item[1])
                    name = SuppliersBiz().get_A_from_B(A="name",nameB="id",valueB=item[1][2:])
                    item.insert(2,name)
                    i = item.copy()
                    del i[5]
                    
                    self.data_purchase.append(i)

                self.window["-TABLE_ORDER-"].update(self.data_purchase)

                

        # Đóng cửa sổ
        self.window.close()
