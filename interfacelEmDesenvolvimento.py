import flet as ft
from nucleo import *

carregar_contatos()

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
                    ft.AppBar(title=ft.Text("AGENDA"), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                    ft.ElevatedButton("Mostar Contatos", on_click=lambda _: page.go("/mostar_contatos"), width=170),
                    ft.ElevatedButton("Buscar Contatos", on_click=lambda _: page.go("/buscar_contatos"), width=170),
                    ft.ElevatedButton("Salvar Contato", on_click=lambda _: page.go("/salvar_contato"), width=170),
                    ft.ElevatedButton("Editar Contato", on_click=lambda _: page.go("/editar_contato"), width=170),
                    ft.ElevatedButton("Excluir Contato", on_click=lambda _: page.go("/excluir_contato"), width=170),
                    ft.ElevatedButton("Importar Contatos", on_click=lambda _: page.go("/importar_contatos"), width=170),
                    ft.ElevatedButton("Exportar Contatos", on_click=lambda _: page.go("/exportar_contatos"), width=170),
                ],
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            )
        )
        
        if page.route == "/mostar_contatos":

            def contato_card(nome, telefone):
                return ft.Container(
                content=ft.Column([ 
                    ft.Text(nome),
                    ft.Text(telefone)
                    ]),
                #on_click=lambda: view_contato(nome),
                on_click=lambda _: view_contato(nome),
                width=350,
                bgcolor=ft.colors.SURFACE_VARIANT,
                border_radius=10,
                padding=10,
                )

            def view_contato(nome):
                info = AGENDA[nome]
                page.views.append(
                ft.View("/contato", [
                    ft.Text(nome),
                    ft.Text(info["telefone"]),
                    ft.Text(info["email"]),  
                    ft.Text(info["endereco"]),
                    ft.ElevatedButton("Voltar", on_click=lambda: page.pop())
                ])
                )

            contatos_cards = [
                contato_card(nome, info["tel"]) 
                for nome, info in AGENDA.items()
            ]
            
            page.views.append(
                ft.View(
                "/mostar_contatos",
                [
                    ft.Column(contatos_cards),
                    ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                ],
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/buscar_contatos":
            page.views.append(
                ft.View(
                    "/buscar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Buscar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/salvar_contato":

            nome_texto = ft.TextField(label="Nome", border_radius=10)
            telefone_texto = ft.TextField(label="Telefone", border_radius=10)
            email_texto = ft.TextField(label="E-mail", border_radius=10)
            endereco_texto = ft.TextField(label="Endereço", border_radius=10)

            def salvar_contato(e):
                nome = nome_texto.value
                telefone = telefone_texto.value
                email = email_texto.value
                endereco = endereco_texto.value
                
                incluir_editar_contato(nome, telefone, email, endereco)
                page.go("/")

            buttons_row = ft.Row([
                ft.ElevatedButton("Salvar Contato", on_click=salvar_contato, width=170),
                ft.ElevatedButton("Cancelar", on_click=lambda _: page.go("/"), width=170)
            ], alignment=ft.MainAxisAlignment.CENTER)

            page.views.append(
                ft.View("/salvar_contato", [
                    ft.AppBar(title=ft.Text("Salvar Contato")),
                    nome_texto,
                    telefone_texto,
                    email_texto,
                    endereco_texto,
                    buttons_row
                ])
            )

        if page.route == "/editar_contato":
            page.views.append(
                ft.View(
                    "/editar_contato",
                    [
                        ft.AppBar(title=ft.Text("Editar Contato"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/excluir_contato":
            page.views.append(
                ft.View(
                    "/excluir_contato",
                    [
                        ft.AppBar(title=ft.Text("Excluir Contato"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/importar_contatos":
            page.views.append(
                ft.View(
                    "/importar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Importar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/exportar_contatos":
            page.views.append(
                ft.View(
                    "/exportar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Exportar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
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