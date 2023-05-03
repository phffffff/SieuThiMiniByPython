import PySimpleGUI as sg
from Business.MembershipsBiz import MembershipsBiz

class MembershipViewGui:
    def __init__(self, id):

        sg.theme('DarkAmber')  # thiết lập theme

        # định nghĩa layout cho giao diện
        self.result = MembershipsBiz().find_memberships_with_cond(key="id", value=id)

        layout1=  [[sg.Text('View',font="blod",size=50,justification="center")],
                      [sg.Text('ID:',size=15), sg.Text(key='id',text=self.result[0])],
                      [sg.Text('Verfication code:', size=15), sg.Text(key='code',text=self.result[1])],
                      [sg.Text('Name:',size=15), sg.Text(key='name',text=self.result[2])],
                      [sg.Text('Birthday:', size=15), sg.Text(key='day',text=self.result[3])],
                      [sg.Text('Phone:',size=15), sg.Text(key='phone',text=self.result[4])],
                      [sg.Text('Mail:',size=15), sg.Text(key='mail',text=self.result[5])],
                      [sg.Text('Point:',size=15), sg.Text(key='point',text=self.result[6])]
                      ]



        # tạo cửa sổ giao diện
        self.window = sg.Window('Membership Detail', layout1)

    def run(self):
            # xử lý sự kiện cho cửa sổ giao diện
            while True:
                event, values = self.window.read()

                if event == "Exit" or event == sg.WINDOW_CLOSED:
                    break    