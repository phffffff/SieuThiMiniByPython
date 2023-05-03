import PySimpleGUI as sg
class Statistical:
    def __init__(self):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')
        default_with =900
        default_height = 500
        # TABLAYOUT Tổng kết
        self.key_statistical = ['accounts','staff','memberships','product_types','products','suppliers','coupous','promotions']
        layout_00 = [[sg.Text('Tài khoản',font=17)],[sg.Text('1',size=10,justification='center' , font=13, key=self.key_statistical[0] )]]
        layout_01 = [[sg.Text('Nhân viên',font=17)],[sg.Text('2',size=10,justification='center', font=13 , key=self.key_statistical[1])]]
        layout_02 = [[sg.Text('Thành viên',font=17)],[sg.Text('3',size=10,justification='center', font=13, key=self.key_statistical[2])]]
        layout_10 = [[sg.Text('Loại Sản Phẩm',font=17)],[sg.Text('4',size=10,justification='center', font=13, key=self.key_statistical[3])]]
        layout_11 = [[sg.Text('Sản phẩm',font=17)],[sg.Text('5',size=10,justification='center', font=13, key=self.key_statistical[4])]]
        layout_12 = [[sg.Text('Nhà cung cấp',font=17)],[sg.Text('6',size=10,justification='center', font=13, key=self.key_statistical[5])]]
        layout_20 = [[sg.Text('Phiếu giảm giá',font=17)],[sg.Text('7',size=10,justification='center', font=13, key=self.key_statistical[6])]]
        layout_21 = [[sg.Text('Chương trình khuyến mãi',font=17)],[sg.Text('8',size=10,justification='center', font=13, key=self.key_statistical[7])]]
        frame_size = (int(default_with/3) , int(default_height/3)) #đặt kích thước chung trừ chương trình khuyến mãi
        # Tạo layout Tổng quát
        grid_layout = [
            [sg.Frame('',layout_00 , size=frame_size), sg.Frame('',layout_01, size=frame_size), sg.Frame('',layout_02, size=frame_size)],
            [sg.Frame('',layout_10, size=frame_size), sg.Frame('',layout_11, size=frame_size), sg.Frame('',layout_12, size=frame_size)],
            [sg.Frame('',layout_20, size=frame_size), sg.Frame('',layout_21 , size=(int(default_with*2/3),int(default_height/5)))]
        ]
        # Giao diện tab Hóa đơn
        frame_size_order = (int(default_with/4) , int(default_height/8))
        top_01 = [[sg.Input('',key='DATE_FROM_ORDER',size=12,justification='center'), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target='DATE_FROM_ORDER',size=(24,24))]]
        top_02 = [[sg.Combo(['Mã hóa đơn'] , key='TYPE_SEARCH')]]
        top_03 = [[sg.Input('',key='CONTENT_SEARCH')]]
        top_04 = [[sg.Input('',key='DATE_TO_ORDER',size=12), sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d', target='DATE_TO_ORDER',size=(24,24))]]
        top_11 = [[sg.Button( image_filename='Picture/refresh-30.png',key='REFRESH',pad=(10 ,10)),sg.Button( image_filename='Picture/preview-file-24.png',key='REVIEW' , image_size=(30,30))]]
        top_12 = [[sg.Combo(['Tổng tiền'] , key='PRICE_SEARCH')]]
        top_13 = [[sg.Input('',key='PRICE_FROM_SEARCH')]]
        top_14 = [[sg.Input('',key='PRICE_TO_SEARCH')]]
        top_15 = [[sg.Button( image_filename='Picture/excel-30.png',key='EXCEL',pad=(10 ,10)),sg.Button( image_filename='Picture/chart-30.png',key='CHART' , image_size=(30,30))]]

        # Tạo table
        self.key_statistical_order = ['Mã hóa đơn','Ngày xuất','Mã nhân viên','Nhân viên xuất ','Mã thành viên','Tên thàng viên','Tổng tiền ','Giảm','Tiền còn lại ','Mã phiếu giảm giá','Điểm']
        self.data_order = [[]]
        table_order = [[sg.Table(values=self.data_order, headings=self.key_statistical_order, justification="center", key='-TABLE_ORDER-', enable_events=True ,vertical_scroll_only=False)]]

        # bottom  order
        bottom_01 = [[sg.Text('Hóa đơn lớn nhất')],
                     [sg.Text('1', size=10, justification='center', key='ORDER_MAX')]]
        bottom_02 = [[sg.Text('Hóa đơn nhỏ nhất')],
                     [sg.Text('1', size=10, justification='center', key='ORDER_MIN')]]
        bottom_03 = [[sg.Text('Doanh thu năm hiện tại')],
                     [sg.Text('1', size=10, justification='center', key='REVENUE_YEAR')]]
        bottom_04 =[[sg.Text('Doanh thu tháng hiện tại ')],
                     [sg.Text('1', size=10, justification='center', key='REVENUE_MONTH')]]
        bottom_05 = [[sg.Text('Doanh thu ngày hiện tại')],
                     [sg.Text('1', size=10, justification='center', key='REVENUE_DAY')]]
        bottom_size = (int(default_with/5) , int(default_height/10))
        #main thống kê hóa đơn
        statistical_order =[[sg.Frame('Từ ngày',top_01 ,size=frame_size_order ,element_justification='center' ) ,sg.Frame('Thống kê theo',top_02,size=(int(default_with/8) , int(default_height/8)),element_justification='center'),sg.Frame('Tìm kiếm ',top_03,size=frame_size_order ,element_justification='center') ,sg.Frame('Đến ngày',top_04,size=frame_size_order ,element_justification='center')],
                    [sg.Frame('',top_11,size=frame_size_order , element_justification='center',border_width=0),sg.Frame('Thống kê theo giá',top_12,size=(int(default_with/8) , int(default_height/8)),element_justification='center') ,
                     sg.Frame('Từ',top_13 ,size=(int(default_with/8) , int(default_height/8)),element_justification='center'), sg.Frame('Đến',top_14 ,size=(int(default_with/8) , int(default_height/8)),element_justification='center'),
                     sg.Frame('',top_15,size=frame_size_order , element_justification='center' , border_width=0)],
                     [sg.Frame('',table_order ,size= (int(default_with) , int(default_height/3)))],
                    [  sg.Frame('',bottom_01 , size=(int(default_with/6.5) , int(default_height/10))) ,sg.Frame('',bottom_02 , size=(int(default_with/6.5) , int(default_height/10))),sg.Frame('',bottom_03 , size=bottom_size),
                       sg.Frame('',bottom_04 , size=bottom_size) ,sg.Frame('',bottom_05 , size=bottom_size)]
                        ]


        # Tạo layout cho Thống kê đơn nhập
        frame_size_entry  = (int(default_with / 4), int(default_height / 8))
        top_entry_01 = [[sg.Input('', key='DATE_FROM_ENTRY', size=12, justification='center'),
                   sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d',
                                     target='DATE_FROM_ENTRY', size=(24, 24))]]
        top_entry_02 = [[sg.Combo(['Mã hóa đơn'], key='TYPE_ENTRY_SEARCH')]]
        top_entry_03 = [[sg.Input('', key='CONTENT_ENTRY_SEARCH')]]
        top_entry_04 = [[sg.Input('', key='DATE_TO_ENTRY', size=12),
                   sg.CalendarButton('', image_filename='Picture/calendar-24.png', format='%Y-%m-%d',
                                     target='DATE_TO_ENTRY', size=(24, 24))]]
        top_entry_11 = [[sg.Button(image_filename='Picture/refresh-30.png', key='REFRESH_ENTRY', pad=(10, 10)),
                   sg.Button(image_filename='Picture/preview-file-24.png', key='REVIEW_ENTRY', image_size=(30, 30))]]
        top_entry_13 = [[sg.Input('', key='PRICE_ENTRY_FROM_SEARCH')]]
        top_entry_14 = [[sg.Input('', key='PRICE_ENTRY_TO_SEARCH')]]
        top_entry_15 = [[sg.Button(image_filename='Picture/excel-30.png', key='EXCEL_ENTRY', pad=(10, 10)),
                   sg.Button(image_filename='Picture/chart-30.png', key='CHART_ENTRY', image_size=(30, 30))]]

        # Tạo table
        self.key_statistical_entry = ['Mã đơn đặt' ,'Mã NCC' ,'Tên NCC' ,'Ngày đặt' , 'Tổng tiền đặt']
        self.data_entry = [[]]
        table_entry = [[sg.Table(values=self.data_entry, headings=self.key_statistical_entry, justification="center",
                                 key='-TABLE_ENTRY-', enable_events=True,hide_vertical_scroll=True)]]

        # bottom  order
        bottom_entry_01 = [[sg.Text('Đơn nhập lớn nhất')],
                     [sg.Text('1', size=10, justification='center', key='ENTRY_MAX')]]
        bottom_entry_02 = [[sg.Text('Đơn nhập nhỏ nhất')],
                     [sg.Text('1', size=10, justification='center', key='ENTRY_MIN')]]
        bottom_entry_03 = [[sg.Text('Chí phí nhập năm hiện tại')],
                     [sg.Text('1', size=10, justification='center', key='ENTRY_YEAR')]]
        bottom_entry_04 = [[sg.Text('Chi phí nhập tháng hiện tại ')],
                     [sg.Text('1', size=10, justification='center', key='ENTRY_MONTH')]]
        bottom_entry_05 = [[sg.Text('Chi phí nhập ngày hiện tại')],
                     [sg.Text('1', size=10, justification='center', key='ENTRY_DAY')]]
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

    def run(self):
        # Vòng lặp chính
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break

        # Đóng cửa sổ
            self.window.close()
