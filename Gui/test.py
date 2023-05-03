import PySimpleGUI as sg

# Khởi tạo dữ liệu mẫu
data = [['', '', ''], ['', '', ''], ['', '', '']]

# Tạo layout cho 9 ô vuông
layout = [
    [sg.InputText(size=(5, 1), key=(i, j), default_text=data[i][j]) for j in range(3)]
    for i in range(3)
]

# Thêm button "Lưu" và "Thoát"
layout.append([sg.Button('Lưu'), sg.Button('Thoát')])

# Tạo cửa sổ
window = sg.Window('9 ô vuông', layout)

# Vòng lặp chính
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Thoát':
        break
    if event == 'Lưu':
        # Lưu dữ liệu vào biến data
        data = [[values[(i, j)] for j in range(3)] for i in range(3)]
        print(data)

# Đóng cửa sổ
window.close()