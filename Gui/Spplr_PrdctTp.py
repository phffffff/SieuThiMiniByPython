import PySimpleGUI as sg

from Business.SuppliersBiz import SuppliersBiz
from Business.ProductTypesBiz import ProductTypesBiz
from Business.SpplrPrdctTpBiz import SpplrPrdctTpBiz
from Entity.SpplrPrdctTpEntity import SpplrPrdctTpEntity

class SpplrPrdctTpGui:
    def __init__(self,supplier_id):
        sg.theme('DarkBlue2')
        sg.set_options(background_color='#272727', text_color='#ffffff')

        self.supplier_id = supplier_id

        self.dulieu = SpplrPrdctTpBiz().get_all_spplrPrdctTp(cond={"supplier_id":supplier_id[2:]})
        self.result = []
        self.resultName = []
        # for i in self.dulieu:
        #     self.result.append(list(i))
        for item in self.dulieu:
            item = list(item)
            item[0] = SuppliersBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[1] = ProductTypesBiz().get_A_from_B(A="name", valueB=item[1], nameB="id")
            if item[2] == 1:
                item[2] = "Hoạt động"
            else:
                item[2] = "Không hoạt động"
            # tùy chỉnh ID Type
            self.result.append(item)
            self.resultName.append(item[1])
        
        self.lstProductType = ProductTypesBiz().get_all_product_types(cond={"is_active":1}, fields=["name"])
        self.resultPrdctTp = []

        for item in self.lstProductType:
            item=list(item)
        
            self.resultPrdctTp.append(item[0])
        
        self.newResultPrdct = [x for x in self.resultPrdctTp if x not in self.resultName]

        self.Headings = ['Supplier Id', 'Product Type Id', 'Status']
        sg.theme('DarkAmber')  # thiết lập theme
        # định nghĩa layout cho giao diện
        layout1 = [[sg.Text('Supplier Id:', size=15),sg.Text(text=self.supplier_id,size=20 , key=self.Headings[0])],
                   [sg.Text('Product Type Id:', size=15),sg.Combo(values=self.newResultPrdct, default_value=self.newResultPrdct[0], key=self.Headings[1])],
                   [sg.Text('Status:', size=15), sg.Combo(values=["Hoạt động", "Không hoạt động"],size=20,key=self.Headings[2] ,default_value="Hoạt động")],
                   [ sg.Button('Thêm'), sg.Button('Sửa'), sg.Button('Xóa')],
                   ]
        # tạo table
        table = sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-', enable_events=True)
        layout2 = [[sg.Text('SUPPLIER PRODUCT TYPE MANAGEMENT', font="blod", justification="center"),sg.Button(image_filename='Picture/refresh-30.png',key='REFRESH')], [table]]
        layout3 = [[sg.Text('Search with:', size=15), sg.Combo([ 'supplier_id', 'product_type_id', 'status'], key='-KEY-'),
                    sg.Text('Content:'), sg.Input(key='-CONTENT-', size=22, enable_events=True)]]
        layout = [[layout1],[layout3], [sg.Column(layout2)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Supplier Product type details', layout)

    def empty(self):
         # self.window[self.Headings[0]].update('')
         self.window[self.Headings[1]].update('')
         self.window[self.Headings[2]].update('')
    def reset(self):
        supplier_id = self.window[self.Headings[0]].get()

        self.dulieu = SpplrPrdctTpBiz().get_all_spplrPrdctTp(cond={"supplier_id": supplier_id[2:]})
        self.result = []
        self.resultName = []
        for item in self.dulieu:
            item = list(item)
            item[0] = SuppliersBiz().to_str_id(id=item[0])  # tùy chỉnh ID
            item[1] = ProductTypesBiz().get_A_from_B(A="name", valueB=item[1], nameB="id")
            if item[2] == 1:
                item[2] = "Hoạt động"
            else:
                item[2] = "Không hoạt động"
            # tùy chỉnh ID Type
            self.result.append(item)
            self.resultName.append(item[1])

        self.lstProductType = ProductTypesBiz().get_all_product_types(cond={"is_active":1}, fields=["name"])
        self.resultPrdctTp = []

        for item in self.lstProductType:
            item=list(item)
        
            self.resultPrdctTp.append(item[0])

        self.newResultPrdct = []
        self.newResultPrdct = [x for x in self.resultPrdctTp if x not in self.resultName]
        
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
            elif event == 'Thêm':
                supplier_id = self.window[self.Headings[0]].get()
                product_type_id = ProductTypesBiz().get_A_from_B(A="id",nameB="name",valueB=values[self.Headings[1]]) 
                status = 0
                if values[self.Headings[2]] == "Hoạt động":
                    status = 1
                data = {'supplier_id': supplier_id[2:], 'product_type_id':product_type_id, 'is_active': status}
                print(data)
                add = SpplrPrdctTpBiz().add_spplrPrdctTp(data=data)
                if add != -1:
                    # Hiển thị kết quả
                    sg.popup('Success')
                    self.reset()
                    
                else:
                    sg.popup('THÊM thất bại')
                    self.reset()
            elif event == "Sửa":
                selected_row = values["-TABLE-"]
                if selected_row:
                    product_type_name_old = self.result[selected_row[0]][1]
                    product_type_id_old = ProductTypesBiz().get_A_from_B(A="id", nameB="name", valueB=product_type_name_old) 
                    id = ProductTypesBiz().get_A_from_B(A="id", nameB="name", valueB=values[self.Headings[1]])
                    if product_type_id_old != id:
                        self.window[self.Headings[1]].Update(value=product_type_name_old)
                        sg.popup("Không được thay đổi mã loại sản phẩm")
                    else:
                        supplier_id = self.window[self.Headings[0]].get()
                        # product_id = values[self.Headings[1]]
                        status = 0
                        if values[self.Headings[2]] == "Hoạt động":
                            status = 1
                        data = {'is_active': status}
                        flag = any(value == '' for value in data.values())
                        flagUpt = False
                        if flag:
                            sg.popup("Invalid!")
                            flagUpt = True
                        if not flagUpt:
                            update = SpplrPrdctTpBiz().update_spplrPrdctTp(data=data,cond={'supplier_id': supplier_id[2:] , 'product_type_id':product_type_id_old})
                            if update != -1:
                                sg.popup('Update Success')
                                self.reset()
                            else:
                                self.reset()
                                sg.popup("Something error with db")
                else:
                    sg.popup("Vui lòng chọn sản phẩm cần sửa") 

            elif event == "Xóa":
                supplier_id = self.window[self.Headings[0]].get()
                product_type_id = ProductTypesBiz().get_A_from_B(A="id", nameB="name", valueB=values[self.Headings[1]])
                result = SpplrPrdctTpBiz().delete_spplrPrdctTp(id_supplier=supplier_id[2:] , id_prdctTp=product_type_id)
                if result:
                    sg.popup("Xóa thành công")
                    self.reset()
                    self.empty()
                else:
                    sg.popup("Xóa thất bại")
            # Sự kiện khi click vào cell trong table

            elif event =='REFRESH':
                self.reset()
                self.empty()

            elif event == '-CONTENT-':
                value_search = values['-CONTENT-']
                search_with = values["-KEY-"]
                # binding list to listpromotion
                Entitys = []
                for item in self.result:
                    entity = SpplrPrdctTpEntity(*item)
                    Entitys.append(entity)
                result = []
                for idx in range(len(Entitys)):
                    if value_search in str(getattr(Entitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window['-TABLE-'].update(result)
            # elif event =='SELECT_PRODUCT':
            #     selectproduct = SelectProductGui()
            #     selectproduct.run()
            #     product_id = selectproduct.product_selected()
            #     self.window[self.Headings[1]].update(product_id)

