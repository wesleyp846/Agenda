import flet as ft

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("AGENDA"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Mostar Contatos", on_click=lambda _: page.go("/mostar_contatos")),
                    ft.ElevatedButton("Buscar Contatos", on_click=lambda _: page.go("/buscar_contatos")),
                    ft.ElevatedButton("Incluir Contato", on_click=lambda _: page.go("/incluir_contato")),
                    ft.ElevatedButton("Editar Contato", on_click=lambda _: page.go("/editar_contato")),
                    ft.ElevatedButton("Excluir Contato", on_click=lambda _: page.go("/excluir_contato")),
                    ft.ElevatedButton("Salvar Contato", on_click=lambda _: page.go("/salvar_contato")),
                    ft.ElevatedButton("Importar Contatos", on_click=lambda _: page.go("/importar_contatos")),
                    ft.ElevatedButton("Exportar Contatos", on_click=lambda _: page.go("/exportar_contatos")),
                ],
            )
        )

        if page.route == "/incluir_contato":
            page.views.append(
                ft.View(
                    "/incluir_contato",
                    [
                        ft.AppBar(title=ft.Text("Incluir Contato"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)