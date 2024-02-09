import flet as ft
from flet import (Page, AppBar, ElevatedButton, MainAxisAlignment, CrossAxisAlignment,
                  Text, View, DataColumn, DataRow, DataTable, DataCell)


def buffs_view_gen(page: Page, name: str):
    with open(f"csv_files/buffs.csv", "r") as f:
        f.readline()
        dane = f.readlines()

    wiersze = [wiersz.strip().split(";") for wiersz in dane]

    rows = []

    def button_clicked(e: ft.ControlEvent):
        print(e.control.text)
        page.set_clipboard(e.control.text)

    for wiersz in wiersze:
        nazwa = wiersz[0]
        komenda = wiersz[1]
        if name == "Remove buffs":
            komenda = f"rmvabl{komenda[6:]}"
        rows.append(
            DataRow(cells=[
                DataCell(Text(nazwa)),
                DataCell(ElevatedButton(komenda, on_click=button_clicked))
            ]),
        )

    table = DataTable(
        columns=[
            DataColumn(Text("Name")),
            DataColumn(Text("Code"))
        ],
        rows=rows,
    )

    route_name = f'/buffs_add'

    if name == "Remove buffs":
        route_name = f'/buffs_rmv'

    view = View(
        route=route_name,
        controls=[
            AppBar(title=Text(name), bgcolor='blue'),
            table,
            # Text(value="name"),
            ElevatedButton(text="home", on_click=lambda _: page.go('/'))
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26,
    )
    view.scroll = True

    return view
