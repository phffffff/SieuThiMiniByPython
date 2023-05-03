import PySimpleGUI as sg
from Business.ProductTypesBiz import ProductTypesBiz
from Entity.ProductTypesEntity import ProductTypes
from Common.PopupComfirm import getPopupComfirm

class ProductTypeGUI:
    def __init__(self):
        
    
        self.Headings = ['ID', 'Name', 'Status']
        self.lstProductTypes = ProductTypesBiz().get_all_product_types()
        self.result = []

        for item in self.lstProductTypes:
            item = list(item)
            item[0] = ProductTypesBiz().to_str_id(id=item[0])# tùy chỉnh ID
            if item[2] == 1:
                item[2] = "Hoạt động"
            elif item[2] == 0:
                item[2] = "Không hoạt động"
            self.result.append(item)
        
        sg.theme('DarkAmber')#thiết lập theme
        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('PRODUCT TYPE MANAGEMENT',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Search with:',size=15),sg.Combo(['id','name','is_active'],default_value="id", key='-COMBO_SEARCH-',enable_events=True),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22,enable_events=True)],  
                      [sg.Text('Id :',size=15), sg.Text(text="", key=self.Headings[0])],
                      [sg.Text('Name:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Status:',size=15), sg.Combo(key=self.Headings[2],values=["Hoạt động", "Không hoạt động"],default_value="Hoạt động")],
                      [sg.Button('New ID'), sg.Button('Add'),sg.Button('Update'), sg.Button('Delete'),sg.Button('Reset')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Product type', layout)
        self.window.read()
        

    def empty(self):
        for item in self.Headings:
            self.window[item].update('')

    def reset(self):
        self.lstProductTypes = ProductTypesBiz().get_all_product_types()
        self.result = []

        for item in self.lstProductTypes:
            item = list(item)
            item[0] = ProductTypesBiz().to_str_id(item[0])
            if item[2] == 1:
                item[2] = "Hoạt động"
            elif item[2] == 0:
                item[2] = "Không hoạt động"
            self.result.append(item)
            
        self.window["-TABLE-"].update(self.result)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break

            elif event == 'New ID':
                newId = ProductTypesBiz().get_new_id()

                self.empty()

                self.window[self.Headings[0]].update(newId)
                self.window[self.Headings[2]].update(1)

            elif event == "Add":   
                id = self.window[self.Headings[0]].get()
                name = values[self.Headings[1]]

                add = ProductTypesBiz().add_product_type(data={"id":id[2:],"name":name})

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
                    # có thể duyệt for nếu thích
                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row[0]][idx])

            elif event == "Delete":
                    # lấy row idx
                selected_row = values["-TABLE-"][0]

                if selected_row:
                    # có thể duyệt for nếu thích
                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row][idx])

                    id = self.window[self.Headings[0]].get()

                    while True:
                        
                        event, values = getPopupComfirm().read()
                        
                        if event == sg.WIN_CLOSED or event == "Cancel":
                            break
                        elif event == "OK":
                            result = ProductTypesBiz().delete_product_type(id=id[2:])
                            if result:
                                sg.popup("Xóa thành công")
                                self.reset()
                            else:
                                self.reset()
                                sg.popup("Something error with db")
                else:
                    sg.popup("Chưa chọn loại sản phẩm")

            elif event == "Update":
                selected_row = values["-TABLE-"][0]

                if selected_row:
                    # có thể duyệt for nếu thích
                    self.window[self.Headings[0]].update(self.result[selected_row][0])
                    self.window[self.Headings[1]].update(self.result[selected_row][1])
                    self.window[self.Headings[2]].update(self.result[selected_row][2])

                    id = self.window[self.Headings[0]].get()
                    name = values[self.Headings[1]]
                    is_active = 0
                    if values[self.Headings[2]] == "Hoạt động":
                        is_active = 1

                    data = {"id": id[2:], "name":name, "is_active":is_active}

                    upd = ProductTypesBiz().update_product_type(data=data, cond={"id":id[2:]})
                    if upd != -1:
                        sg.popup('Upđate Success')
                        self.reset()
                else:
                    sg.popup("Chưa chọn loại sản phẩm")
            
            # sự kiện search onchange
            elif event == "-CONTENT-":
                value_search = values["-CONTENT-"]
                search_with = values["-COMBO_SEARCH-"]

                # binding list to listProductType
                productTypeEntitys = []
                for item in self.result:
                    productType = ProductTypes(*item)
                    productTypeEntitys.append(productType)

                result = []
                for idx in range(len(productTypeEntitys)):
                    if value_search in str(getattr(productTypeEntitys[idx],search_with)):
                        result.append(self.result[idx])
                    
                self.window["-TABLE-"].update(result)

        self.window.close()

