import flet as ft
from flet import Page, DataTable, DataColumn, DataRow, DataCell, ElevatedButton, Text, TextField, View, Row, AppBar

def gen_item_view(page: Page):
    with open("items.csv", "r") as f:
        f.readline()
        dane = f.readlines()

    # Podziel dane na wiersze

    wiersze = [wiersz.strip().split(",") for wiersz in dane]

    rows = []

    def button_clicked(e: ft.ControlEvent):
        print(e.control.text)
        page.set_clipboard(e.control.text)

    def search_clicked(e: ft.ControlEvent):
        if len(search_field.value) < 3:
            search_field.value = ""
            search_field.hint_text = "name"
            search_field.update()
            return
        if len(view.controls) >= 2:
            view.controls[2] = Text("Empty")
        view.update()
        rows.clear()
        wierszyki = []
        for d in dane:
            wart = d.split(",")
            if search_field.value.lower() in wart[0].lower():
                wierszyki.append(d)
        gen_table([wiersz.strip().split(",") for wiersz in wierszyki])
        view.controls[2] = DataTable(
                columns=[
                    DataColumn(Text("Nazwa")),
                    DataColumn(Text("Komenda"))
                ],
                rows=rows,
            )

        view.update()

    def gen_table(wierszyk):
        for wiersz in wierszyk:
            nazwa = wiersz[0]
            komenda = wiersz[1]
            rows.append(
                DataRow(cells=[
                    DataCell(Text(nazwa)),
                    DataCell(ElevatedButton(komenda, on_click=button_clicked))
                ]),
            )

    search_field = TextField(label="szukajka", width=page.width*0.65, helper_text="at least 3 characters long", height=75)
    search_button = ElevatedButton("szukaj", on_click=search_clicked, width=page.width*0.15, height=50)
    home_button = ElevatedButton("cofnij", on_click=lambda _: page.go('/fandom4'), width=page.width*0.15, height=50)

    view = View(
        route='/items',
        controls=[
            AppBar(title=Text("Items"), bgcolor='blue'),
            Row(
                controls=[
                    search_field,
                    search_button,
                    home_button
                ],
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            DataTable(
                columns=[
                    DataColumn(Text("Nazwa")),
                    DataColumn(Text("Komenda"))
                ],
                rows=rows,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    view.scroll = True

    return view
