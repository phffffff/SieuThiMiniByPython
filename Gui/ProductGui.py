import PySimpleGUI as sg
from Business.ProductBiz import ProductBiz
from Business.ProductTypesBiz import ProductTypesBiz
from Entity.ProductEntity import ProductEntity
from Common.PopupComfirm import getPopupComfirm


class ProductGUI:
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
        layou2 = [[sg.Text('PRODUCT MANAGEMENT', font="blod", size=70, justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',
                            enable_events=True)]]
        layout1 = [[sg.Text('Search with:', size=15),
                    sg.Combo(['id', 'name', 'count', 'price', 'discount', 'remaining', 'type', 'status'],
                             default_value="id", key='-COMBO_SEARCH-', enable_events=True), sg.Text('Content:'),
                    sg.Input(key='-CONTENT-', size=22, enable_events=True)],
                   [sg.Text('Id :', size=15), sg.Text(text="", key=self.Headings[0])],
                   [sg.Text('Name:', size=15), sg.Input(key=self.Headings[1])],
                   [sg.Text('Count:', size=15), sg.Text(text="", key=self.Headings[2])],
                   [sg.Text('Price:', size=15), sg.Input(key=self.Headings[3])],
                   [sg.Text('Type:', size=15),
                    sg.Combo(values=self.resultNamePrdctTp, default_value=self.resultNamePrdctTp[0],
                             key=self.Headings[6], enable_events=True)],
                   [sg.Text('Status:', size=15), sg.Input(key=self.Headings[7], default_text="1")],
                   [sg.Button('New ID'), sg.Button('Add'), sg.Button('Update'), sg.Button('Delete'),
                    sg.Button('Reset')]]

        layout = [[sg.Col(layou2), sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Product', layout)
        self.window.read()

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

            elif event == 'New ID':
                newId = ProductBiz().get_new_id()

                self.empty()

                self.window[self.Headings[0]].update(newId)
                self.window[self.Headings[2]].update(0)
                self.window[self.Headings[6]].update(self.resultNamePrdctTp[0])
                self.window[self.Headings[7]].update(1)

            elif event == "Add":
                id = self.window[self.Headings[0]].get()
                name = values[self.Headings[1]]
                price = values[self.Headings[3]]
                # values[self.Headings[6]] là name đó
                type_id = ProductTypesBiz().get_A_from_B(A="id", nameB="name", valueB=values[self.Headings[6]])

                # xử lý để lấy discount
                # //
                # kết thúc

                product = {"id": id[2:], "name": name, "count": 0, "price": price, "discount": 0,
                           "product_type_id": type_id, "is_active": 1}

                add = ProductBiz().add_product(products=product)

                if add != -1:
                    sg.popup('Success')
                    self.reset()

            elif event == "Reset":
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

            elif event == "Delete":
                id = self.window[self.Headings[0]].get()
                if id == "":
                    self.reset()
                    sg.popup("Something error with server")

                while True:
                    # getPopupComfirm() có thể sài nhiều lần nên t để trong common
                    event, values = getPopupComfirm().read()
                    if event in (sg.WIN_CLOSED, 'Cancel'):
                        break
                    elif event == "OK":
                        result = ProductBiz().delete_product(id=id[2:])
                        if result:
                            sg.popup("Xóa thành công")
                            self.reset()
                            break
                        else:
                            self.reset()
                            sg.popup("Something error with db")

            elif event == "Update":
                id = self.window[self.Headings[0]].get()
                name = values[self.Headings[1]]
                price = values[self.Headings[3]]
                type_id = ProductTypesBiz().get_A_from_B(A="id", nameB="name", valueB=values[self.Headings[6]])
                is_active = values[self.Headings[7]]

                data = {"id": id[2:], "name": name, "price": price, "product_type_id": type_id, "is_active": is_active}

                flag = any(value == '' for value in data.values())
                if flag:
                    sg.popup("Invalid!")
                    break

                upd = ProductBiz().update_product(product=data, cond={"id": id[2:]})
                if upd != -1:
                    sg.popup('Update Success')
                    self.reset()
                else:
                    self.reset()
                    sg.popup("Something error with db")

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

        self.window.close()
