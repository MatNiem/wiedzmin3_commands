import flet as ft
from flet import (Page, View, AppBar, Row, ElevatedButton, Text, Stack,
                  MainAxisAlignment, CrossAxisAlignment, Image, Icon, FilledButton)

import csv

from flet_core import ButtonStyle


def gen_skills_view(page: Page, name):

    def color_gen(p_name):
        p_color = p_name
        if p_name == 'red':
            p_color = ft.colors.RED_700
        elif p_name == 'green':
            p_color = ft.colors.GREEN_700
        elif p_name == 'blue':
            p_color = ft.colors.BLUE_700
        elif p_name == 'yellow':
            p_color = ft.colors.ORANGE_600
        return p_color

    def command_func(e: ft.ControlEvent):
        print(e.control.data)
        page.set_clipboard(e.control.data)

    '''function allowing to use one graphic for perks (I couldnt find all icons in one place and im lazy)'''
    def button_gen(p_name: str, skill_data: str):
        if skill_data.startswith("learnskill('perk_"):
            skill_data = "learnskill('perk')"
        gen_button = ElevatedButton(content=Image(src=f'/{p_name}/{skill_data[12:-2]}.png'), data=skill_data,
                                    on_click=command_func, width=page.width/6, height=page.height/6,
                                    style=ButtonStyle(
                                        shape=ft.BeveledRectangleBorder(radius=15),
                                        bgcolor=color_gen(name)
                                    ))
        return gen_button

    view = View(
        route=f'/skills/{name}',
        controls=[
            AppBar(title=Text(name), bgcolor=color_gen(name)),
            # Text(value="Home"),
            ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.STRETCH,
        spacing=26
    )

    with open(f"csv_files/{name}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            datarow = Row(vertical_alignment=CrossAxisAlignment.CENTER, alignment=MainAxisAlignment.CENTER)
            for data in row:
                datarow.controls.append(
                    button_gen(name, data),
                    # ElevatedButton(content=Image(src=f'/{name}/{data[12:-2]}.png'), data=data,
                    #                on_click=command_func, width=page.width/6, height=page.height/6),
                    # Text(f"{data[12:-2]}.png"),
                    # FilledButton(on_click=command_func, data=data, style=ButtonStyle(bgcolor=name, color=name)),
                    # FilledButton(content=Image(src=f'/skills_icons/red/sword_s1.png'), on_click=command_func,
                    #              data=data, ),
                    # Stack(
                        # controls=[
                            # Image(src=f"https://static.wikia.nocookie.net/witcher/images/5/59/Tw3_ability_aard_intensity.png/revision/latest?cb=20170317171727", fit=ft.ImageFit.CONTAIN,),

                            # ElevatedButton(text=" ", data=data,
                            #                on_click=command_func, width=page.width/6, height=page.height/6),

                        # ]
                    # )
                    # Image(src=f'/{name}/{data[12:-2]}.png')
                )
            view.controls.append(datarow)
    return view

table = []

if __name__ == '__main__':
    with open("csv_files/red.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            table.append(row)
    print(table)
