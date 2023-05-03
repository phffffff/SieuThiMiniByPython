import PySimpleGUI as sg
from Business.ProductBiz import ProductBiz
from Business.ProductTypesBiz import ProductTypesBiz
from Entity.ProductEntity import ProductEntity

class SelectProductGui:
    def __init__(self):
        self.Headings = ['ID', 'Name', 'Count', 'Price', 'Discount', 'Remaining', 'Type', 'Status']
        # get list product type
        self.lstProductType = ProductTypesBiz().get_all_product_types(cond={"is_active": 1}, fields=["name"])
        self.resultNamePrdctTp = []

        for item in self.lstProductType:
            item = list(item)
            self.resultNamePrdctTp.append(item[0])
        # Kết thúc

        # get list product
        self.lstProduct = ProductBiz().get_all_product()
        self.result = []

        for item in self.lstProduct:
            item = list(item)

            item[0] = ProductBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[5] = ProductTypesBiz().get_A_from_B(A="name", nameB="id", valueB=item[5])  # tùy chỉnh ID Type
            remain = item[3] - item[4]  # tính remain
            item.insert(5, remain)  # đẩy ramain vào list, lưu ý thứu tự nha

            self.result.append(item)
        # kết thúc

        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('PRODUCT MANAGEMENT', font="blod", justification="center"),sg.Button(image_filename='Picture/refresh-30.png',key='REFRESH')],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', auto_size_columns=True,
              size=(10, len(self.result)), enable_events=True)]]
        layout1 = [[sg.Text('Search with:', size=15),
                    sg.Combo(['id', 'name', 'count', 'price', 'discount', 'remaining', 'type', 'status'],
                             default_value="id", key='-COMBO_SEARCH-', enable_events=True), sg.Text('Content:'),
                    sg.Input(key='-CONTENT-', size=22, enable_events=True)],
                   [sg.Text('Mã sản phẩm :', size=15), sg.Text(text="", key=self.Headings[0])],
                   [sg.Text('Tên sản phẩm :', size=15), sg.Input(key=self.Headings[1])],
                   [sg.Text('Số lượng :', size=15), sg.Text(text="", key=self.Headings[2])],
                   [sg.Text('Giá :', size=15), sg.Input(key=self.Headings[3])],
                   [sg.Text('Loại:', size=15),
                    sg.Combo(values=self.resultNamePrdctTp, default_value=self.resultNamePrdctTp[0],
                             key=self.Headings[6], enable_events=True)],
                   [sg.Text('Trạng thái:', size=15), sg.Input(key=self.Headings[7], default_text="1")],
                   [sg.Button('Chọn sản phẩm',key='SELECT_PRODUCT'),
                    sg.Button('Đóng',key='CLOSE')]]

        layout = [[ sg.Col(layout1)],[sg.Col(layou2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Product', layout , no_titlebar=True)
        self.window.read()
    def product_selected(self):
        product_id = self.window[self.Headings[0]].get()
        return product_id
    def empty(self):
        for item in self.Headings:
            if item == "Remaining" or item == "Discount":
                continue
            self.window[item].update('')

    def reset(self):
        # get list product type
        self.lstProductType = ProductTypesBiz().get_all_product_types(cond={"is_active": 1}, fields=["name"])
        self.resultNamePrdctTp = []

        for item in self.lstProductType:
            item = list(item)
            self.resultNamePrdctTp.append(item[0])
        # Kết thúc

        # get list product
        self.lstProduct = ProductBiz().get_all_product()
        self.result = []

        for item in self.lstProduct:
            item = list(item)
            item[0] = ProductBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[5] = ProductTypesBiz().get_A_from_B(A="name", nameB="id", valueB=item[5])  # tùy chỉnh ID Type
            remain = item[3] - item[4]  # tính remain
            item.insert(5, remain)  # đẩy ramain vào list, lưu ý thứu tự nha

            self.result.append(item)
        # kết thúc

        self.window[self.Headings[6]].update(values=self.resultNamePrdctTp)
        self.window["-TABLE-"].update(self.result)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break

            elif event == "REFRESH":
                self.empty()
                self.reset()

            # onCLick element of table
            elif event == "-TABLE-":
                selected_row = values["-TABLE-"]
                # binding dữ liệu đến input field
                if selected_row:
                    for idx in range(len(self.Headings)):
                        if self.Headings[idx] == "Discount" or self.Headings[idx] == "Remaining":
                            continue
                        self.window[self.Headings[idx]].update(self.result[selected_row[0]][idx])

            # sự kiện search onchange
            elif event == "-CONTENT-":
                value_search = values["-CONTENT-"]
                search_with = values["-COMBO_SEARCH-"]

                # binding list to listProduct
                productEntitys = []
                for item in self.result:
                    product = ProductEntity(*item)
                    productEntitys.append(product)

                result = []
                for idx in range(len(productEntitys)):
                    if value_search in str(getattr(productEntitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window["-TABLE-"].update(result)
            elif event == 'SELECT_PRODUCT':
                self.window.close()
                return self.product_selected()
            elif event =='CLOSE':
                self.window.close()

        self.window.close()

