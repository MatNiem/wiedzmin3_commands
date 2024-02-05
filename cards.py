import flet as ft
from flet import Page, DataTable, DataColumn, DataRow, DataCell, ElevatedButton, Text, TextField, View, Row, AppBar, Image

import csv


def gen_cards_view(page: Page):
    with open("gwent_cards.csv", "r") as f:
        f.readline()
        dane = f.readlines()

    # Podziel dane na wiersze

    wiersze = [wiersz.strip().split(",") for wiersz in dane]

    rows = []

    def button_clicked(e: ft.ControlEvent):
        command = f"additem('{e.control.data}')"
        print(command)
        page.set_clipboard(command)

    def gen_table(wierszyk):
        for wiersz in wierszyk:
            deck = wiersz[0]
            name = wiersz[1]
            picture = wiersz[2]
            card_id = wiersz[3]
            rows.append(
                DataRow(cells=[
                    DataCell(Text(deck)),
                    DataCell(ElevatedButton(name, on_click=button_clicked, data=card_id)),
                    # DataCell(Image(src=picture))
                    DataCell(Text(card_id))
                ]),
            )

    gen_table(wiersze)

    view = View(
        route='/items',
        controls=[
            AppBar(title=Text("Items"), bgcolor='blue'),

            DataTable(
                columns=[
                    DataColumn(Text("Deck")),
                    DataColumn(Text("Card")),
                    DataColumn(Text("id"))
                ],
                rows=rows,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    view.scroll = True

    return view
