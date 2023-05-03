import PySimpleGUI as sg
from Business.SuppliersBiz import SuppliersBiz
from Entity.SupplierEntity import Suppliers
from Common.PopupComfirm import getPopupComfirm

class SupplierGUI:
    def __init__(self):
        
    
        self.Headings = ['ID', 'Name', 'Address','Status']
        self.lstSuppliers = SuppliersBiz().get_all_suppliers()
        self.result = []

        for item in self.lstSuppliers:
            item = list(item)
            item[0] = SuppliersBiz().to_str_id(id=item[0])# tùy chỉnh ID
            if item[3] == 1:
                item[3] = "Hoạt động"
            elif item[3] == 0 :
                item[3] = "Không hoạt động"

            self.result.append(item)
        
        sg.theme('DarkAmber')#thiết lập theme
        # định nghĩa layout cho giao diện
        layou2 = [[sg.Text('SUPPLIER MANAGEMENT',font="blod",size=70,justification="center")],
                  [sg.Table(values=self.result, headings=self.Headings, justification="center", key='-TABLE-',enable_events=True)]]
        layout1=  [[sg.Text('Search with:',size=15),sg.Combo(['id','name','addr','status'],default_value="id", key='-COMBO_SEARCH-',enable_events=True),sg.Text('Content:'),sg.Input(key='-CONTENT-',size=22,enable_events=True)],  
                      [sg.Text('Id :',size=15), sg.Text(text="", key=self.Headings[0])],
                      [sg.Text('Name:',size=15), sg.Input(key=self.Headings[1])],
                      [sg.Text('Address:',size=15), sg.Input(key=self.Headings[2])],
                      [sg.Text('Status:',size=15), sg.Combo(values=["Hoạt động", "Không hoạt động"],default_value="Hoạt động",key=self.Headings[3])],
                      [sg.Button('New ID'), sg.Button('Add'),sg.Button('Update'), sg.Button('Delete'),sg.Button('Reset')]]

        layout=[[sg.Col(layou2),sg.Col(layout1)]]

        # tạo cửa sổ giao diện
        self.window = sg.Window('Supplier', layout)
        self.window.read()
        

    def empty(self):
        for item in self.Headings:
            self.window[item].update('')

    def reset(self):
        self.lstSuppliers = SuppliersBiz().get_all_suppliers()
        self.result = []

        for item in self.lstSuppliers:
            item = list(item)
            item[0] = SuppliersBiz().to_str_id(item[0])
            if item[3] == 1:
                item[3] = "Hoạt động"
            elif item[3] == 0 :
                item[3] = "Không hoạt động"
            self.result.append(item)
            
        self.window["-TABLE-"].update(self.result)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == "Exit" or event == sg.WINDOW_CLOSED:
                break

            elif event == 'New ID':
                newId = SuppliersBiz().get_new_id()

                self.empty()

                self.window[self.Headings[0]].update(newId)
                self.window[self.Headings[3]].Update(value = "Hoạt động")

            elif event == "Add":   
                id = self.window[self.Headings[0]].get()
                name = values[self.Headings[1]]
                addr = values[self.Headings[2]]

                add = SuppliersBiz().add_supplier(data={"id":id[2:],"name":name, 'addr': addr})

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
                selected_row = values["-TABLE-"]

                if selected_row:
                    # có thể duyệt for nếu thích
                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row[0]][idx])
                        
                    id = self.window[self.Headings[0]].get()

                    while True:
                        # getPopupComfirm() có thể sài nhieuf lần nên t để trong common
                        wd = getPopupComfirm()
                        event, values = wd.read()
                        if event == sg.WIN_CLOSED or event == "Cancel":
                            break
                        elif event == "OK":
                            result = SuppliersBiz().delete_supplier(id=id[2:])
                            if result:
                                sg.popup("Success")
                                self.reset()
                                wd.close()
                            else:
                                self.reset()
                                sg.popup("Something error with db")
                                wd.close()
                else:
                    sg.popup("Chưa chọn nhà cung ứng cần xóa")

            elif event == "Update":
                selected_row = values["-TABLE-"]

                if selected_row:

                    for idx in range(len(self.Headings)):
                        self.window[self.Headings[idx]].update(self.result[selected_row[0]][idx])

                    id = self.window[self.Headings[0]].get()
                    name = values[self.Headings[1]]
                    addr = values[self.Headings[2]]
                    is_active = 0
                    if values[self.Headings[3]] == "Hoạt động":
                        is_active = 1

                    data = {"id": id[2:], "name":name, "addr": addr, "is_active":is_active}

                    flag = any(value == '' for value in data.values())
                    if flag:
                        sg.popup("Invalid!")
                    else:    
                        upd = SuppliersBiz().update_supplier(data=data, cond={"id":id[2:]})
                        if upd != -1:
                            sg.popup('Update Success')
                            self.reset()
                else:
                    sg.popup("Chưa chọn nhà cung ứng")
            
            # sự kiện search onchange
            elif event == "-CONTENT-":
                value_search = values["-CONTENT-"]
                search_with = values["-COMBO_SEARCH-"]

                # binding list to listProduct
                Entitys = []
                for item in self.result:
                    supplier = Suppliers(*item)
                    Entitys.append(supplier)

                result = []
                for idx in range(len(Entitys)):
                    if value_search in str(getattr(Entitys[idx], search_with)):
                        result.append(self.result[idx])

                self.window["-TABLE-"].update(result)

        self.window.close()

