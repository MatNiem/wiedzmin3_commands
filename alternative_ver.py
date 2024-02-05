import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, Row
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import view_gen
import item_view
import skills
import cards


def main(page: Page) -> None:
    page.title = "Alternative Ver"
    page.scroll = True
    page.window_min_width = page.width
    page.window_min_height = page.height

    skills_view = View(
        route='/skills',
        controls=[
            AppBar(title=Text('Home'), bgcolor='blue'),
            ElevatedButton(text="Red", on_click=lambda _: page.go('/skills/red'), color="red",
                           width=page.window_width * 0.3, height=page.window_height * 0.15),
            ElevatedButton(text="Blue", on_click=lambda _: page.go('/skills/blue'), color="blue",
                           width=page.window_width * 0.3, height=page.window_height * 0.15),
            ElevatedButton(text="Green", on_click=lambda _: page.go('/skills/green'), color="green",
                           width=page.window_width * 0.3, height=page.window_height * 0.15),
            ElevatedButton(text="Yellow", on_click=lambda _: page.go('/skills/yellow'), color="yellow",
                           width=page.window_width * 0.3, height=page.window_height * 0.15),
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='blue'),
                    # Text(value="Home"),
                    Row(controls=[
                        ElevatedButton(text="Player commands", on_click=lambda _: page.go('/fandom1'),
                                       width=page.window_width*0.3, height=page.window_height*0.15),
                        ElevatedButton(text="Character commands", on_click=lambda _: page.go('/fandom2'),
                                       width=page.window_width*0.3, height=page.window_height*0.15),
                        ElevatedButton(text="Gwent commands", on_click=lambda _: page.go('/fandom10'),
                                       width=page.window_width*0.3, height=page.window_height*0.15)
                        ],
                        alignment=MainAxisAlignment.CENTER),
                    Row(controls=[
                        ElevatedButton(text="Inventory commands", on_click=lambda _: page.go('/fandom4'),
                                       width=page.window_width*0.3, height=page.window_height*0.15),
                        ElevatedButton(text="Combat commands", on_click=lambda _: page.go('/fandom5'),
                                       width=page.window_width*0.3, height=page.window_height*0.15),
                        ElevatedButton(text="Weather commands", on_click=lambda _: page.go('/fandom6'),
                                       width=page.window_width*0.3, height=page.window_height*0.15)
                        ],
                        alignment=MainAxisAlignment.CENTER),
                    Row(controls=[
                        ElevatedButton(text="Game state commands", on_click=lambda _: page.go('/fandom7'),
                                       width=page.window_width*0.3, height=page.window_height*0.15),
                        ElevatedButton(text="Time commands", on_click=lambda _: page.go('/fandom8'),
                                       width=page.window_width*0.3, height=page.window_height*0.15),
                        ElevatedButton(text="Map commands", on_click=lambda _: page.go('/fandom9'),
                                       width=page.window_width*0.3, height=page.window_height*0.15)
                        ],
                        alignment=MainAxisAlignment.CENTER),
                    ElevatedButton(text="Debug commands", on_click=lambda _: page.go('/fandom3'),
                                   width=page.window_width*0.9, height=page.window_height*0.15)
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        match page.route:
            case '/fandom1':
                page.views.append(view_gen.gen_view(page, 1, "Player commands"))
            case '/fandom2':
                page.views.append(view_gen.gen_view(page, 2, "Character commands"))
            case '/fandom3':
                page.views.append(view_gen.gen_view(page, 3, "Debug commands"))
            case '/fandom4':
                page.views.append(view_gen.gen_view(page, 4, "Inventory commands"))
            case '/fandom5':
                page.views.append(view_gen.gen_view(page, 5, "Combat commands"))
            case '/fandom6':
                page.views.append(view_gen.gen_view(page, 6, "Weather commands"))
            case '/fandom7':
                page.views.append(view_gen.gen_view(page, 7, "Game state commands"))
            case '/fandom8':
                page.views.append(view_gen.gen_view(page, 8, "Time commands"))
            case '/fandom9':
                page.views.append(view_gen.gen_view(page, 9, "Map commands"))
            case '/fandom10':
                page.views.append(view_gen.gen_view(page, 10, "Gwent commands"))
            case '/items':
                page.views.append(item_view.gen_item_view(page))
            case '/skills':
                page.views.append(skills_view)
            case '/skills/red':
                page.views.append(skills.gen_skills_view(page, "red"))
            case '/skills/blue':
                page.views.append(skills.gen_skills_view(page, "blue"))
            case '/skills/green':
                page.views.append(skills.gen_skills_view(page, "green"))
            case '/skills/yellow':
                page.views.append(skills.gen_skills_view(page, "yellow"))
            case '/gwent':
                page.views.append(cards.gen_cards_view(page))
            case _:
                pass

        page.scroll = True
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir="skills_icons")
