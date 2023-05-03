import PySimpleGUI as sg
from Business.MembershipsBiz import MembershipsBiz
from Common.PopupComfirm import getPopupComfirm
from Entity.MembershipsEntity import Memberships

class MembershipRegisterGui:
    def __init__(self):


        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        self.newId = MembershipsBiz().get_new_id()

        layout1=  [[sg.Text('Register',font="blod",size=50,justification="center")],
                      [sg.Text('ID:',size=15), sg.Input(key='id',default_text=self.newId)],
                      [sg.Text('Verfication code:', size=15), sg.Input(key='code')],
                      [sg.Text('Name:',size=15), sg.Input(key='name')],
                      [sg.Text('Birthday:', size=15), sg.Input(key='day'), sg.CalendarButton('', image_filename='Picture/calendar-24.png',target='day', format='%Y-%m-%d', size=22)],
                      [sg.Text('Phone:',size=15), sg.Input(key='phone')],
                      [sg.Text('Mail:',size=15), sg.Input(key='mail')],

                      [sg.Button('TẠO',size=62)]]



        # tạo cửa sổ giao diện
        self.window = sg.Window('Quản lý thành viên', layout1)

    def empty(self):
        self.window['id'].update('')
        self.window['code'].update('')
        self.window['day'].update('')
        self.window['phone'].update('')
        self.window['mail'].update('')
        self.window['name'].update('')


    def run(self):
            # xử lý sự kiện cho cửa sổ giao diện
            while True:
                event, values = self.window.read()

                if event == "Exit" or event == sg.WINDOW_CLOSED:
                    break
                elif event == 'TẠO':
                    verification_code = values['code']
                    name = values['name']
                    birthday = values['day']
                    phone = values['phone']
                    mail = values['mail']


                    membership = {"id": self.newId[2:], "verification_code": verification_code, "name": name,
                                  "birthday": birthday, "phone": phone, "mail": mail, "point": 0, "is_active": 1}
                    add = MembershipsBiz().add_memberships(memberships=membership)
                    if add != -1:
                        sg.popup('Success')
                        self.empty()
                    else:
                        sg.popup('ADD ERROR')