import flet as ft
from flet import (Page, Tabs, Tab, Container, Stack, ElevatedButton,
                  Text, TextField, View, Row, AppBar, Image, UserControl, GridView)

import csv


class CardsTab(UserControl):
    def __init__(self, deck: str, page: Page) -> None:
        super().__init__()
        self.deck = deck
        self.page = page
        self.grid = self.gen_row()

    def button_clicked(self, e: ft.ControlEvent) -> None:
        print(e.control.data)
        self.page.set_clipboard(e.control.data)

    def gen_row(self):
        grid = GridView(max_extent=self.page.width/5, child_aspect_ratio=0.5)

        data = []
        with open("gwent_cards.csv", "r") as f:
            f.readline()
            file_content = f.readlines()

        data = [line.strip().split(",") for line in file_content]

        for d in data:
            deck = d[0]
            name = d[1]
            picture_url = d[2]
            card_id = d[3]
            # print(name)
            if deck == self.deck:
                grid.controls.append(
                    Container(
                        content=
                        # Text(name),
                        Image(src=picture_url, border_radius=ft.border_radius.all(10)),
                        # ink=True,
                        bgcolor='',
                        margin=10,
                        padding=10,
                        height=200,
                        width=100,
                        alignment=ft.alignment.center,
                        on_click=self.button_clicked,
                        data=f"additem('{card_id}')"
                    )

                    # ElevatedButton(text=name,
                    #                data=f"additem('{card_id}')",
                    #                on_click=self.button_clicked,
                    #                )


                    # ElevatedButton(text=name,
                    #                height=300,
                    #                width=150,
                    #                content=Image(src=picture_url,
                    #                              border_radius=ft.border_radius.all(10),
                    #                              ),
                    #                data=f"additem('{card_id}')",
                    #                on_click=self.button_clicked)
                )
        return grid

    def build(self) -> GridView:
        return self.grid


def gen_cards_view(page: Page):

    tabs = Tabs(
                selected_index=1,
                animation_duration=300,
                tabs=[
                    Tab(
                        text="Northern Realms",
                        content=CardsTab(deck="Northern Realms", page=page)
                    ),
                    Tab(
                        text="Nilfgaard",
                        content=CardsTab(deck="Nilfgaard", page=page)
                    ),
                    Tab(
                        text="Monsters",
                        content=CardsTab(deck="Monsters", page=page)
                    ),
                    Tab(
                        text="Scoia'tael",
                        content=CardsTab(deck="Scoia'tael", page=page)
                    ),
                    Tab(
                        text="Neutral",
                        content=CardsTab(deck="Neutral", page=page)
                    ),
                    Tab(
                        text="Skellige",
                        content=CardsTab(deck="Skellige", page=page),
                    )
                ],
                width=page.window_width,
                height=page.window_height - 40,
            )

    view = View(
        route='/items',
        controls=[
            AppBar(title=Text("Cards"), bgcolor='blue'),
            tabs

        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

# allows tab to resize
    def page_resize(e):
        tabs.width = page.window_width
        tabs.height = page.window_height - 40
        page.update()

    page.on_resize = page_resize

    view.scroll = False
    return view
