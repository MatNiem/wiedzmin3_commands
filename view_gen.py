import flet as ft
from flet import DataTable, DataColumn, DataRow, DataCell, ElevatedButton, Text, TextField, View, AppBar
from flet import MainAxisAlignment, CrossAxisAlignment


def gen_view(page, i, name):
    with open(f"fandom{i}.csv", "r") as f:
        f.readline()
        dane = f.readlines()

    wiersze = [wiersz.strip().split(";") for wiersz in dane]

    rows = []

    def button_clicked(e: ft.ControlEvent):
        print(e.control.text)
        if e.control.text == "additem('name',#)":
            page.go('/items')
        elif e.control.text == "learnskill(skill)":
            page.go('/skills')
        elif e.control.text == "additem(card,#)":
            page.go('/gwent')
        page.set_clipboard(e.control.text)

    for wiersz in wiersze:
        komenda = wiersz[0]
        opis = wiersz[1]
        rows.append(
            DataRow(cells=[
                DataCell(ElevatedButton(komenda, on_click=button_clicked)),
                DataCell(Text(opis))
            ]),
        )

    table = DataTable(
        columns=[
            DataColumn(Text("Command")),
            DataColumn(Text("Description"))
        ],
        rows=rows,
    )

    view = View(
        route=f'/fandom{i}',
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
