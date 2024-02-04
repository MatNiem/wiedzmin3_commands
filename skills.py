import flet as ft
from flet import Page, View, AppBar, Row, ElevatedButton, Text, MainAxisAlignment, CrossAxisAlignment
import csv


def gen_skills_view(page: Page, name):

    def command_func(e: ft.ControlEvent):
        print(e.control.data)
        page.set_clipboard(e.control.data)

    view = View(
        route=f'/skills/{name}',
        controls=[
            AppBar(title=Text(name), bgcolor='blue'),
            # Text(value="Home"),
            ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.STRETCH,
        spacing=26
    )

    with open(f"{name}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            datarow = Row(vertical_alignment=CrossAxisAlignment.CENTER, alignment=MainAxisAlignment.CENTER)
            for data in row:
                datarow.controls.append(
                    ElevatedButton(text=" ", icon=ft.icons.EXPOSURE_PLUS_1, icon_color='purple', data=data, on_click=command_func, width=page.width/6, height=page.height/6)
                )
            view.controls.append(datarow)
    return view

table = []

if __name__ == '__main__':
    with open("sword.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            table.append(row)
    print(table)
