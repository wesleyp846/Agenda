import flet as ft

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 700
    page.update()

    c0= ft.Container(
        content = ft.Text("Agenda de Contatos",
        style=ft.TextThemeStyle.DISPLAY_SMALL, color="PURPLE", text_align="CENTER")
    )

    c1= ft.Container(
        content = ft.ElevatedButton("Mostar Contatos"), 
        padding=5,
        width=300,
        on_click=lambda e: print("BOtão vai para")
    )

    c2= ft.Container(
        content = ft.ElevatedButton("Buscar Contatos"), 
        padding=5,
        width=300
    )

    c3= ft.Container(
        content = ft.ElevatedButton("Incluir Contato"), 
        padding=5,
        width=300
    )

    c4= ft.Container(
        content = ft.ElevatedButton("Editar Contato"), 
        padding=5,
        width=300
    )

    c5= ft.Container(
        content = ft.ElevatedButton("Excluir Contato"), 
        padding=5,
        width=300
    )

    c6= ft.Container(
        content = ft.ElevatedButton("Importar Contatos"), 
        padding=5,
        width=300
    )

    c7= ft.Container(
        content = ft.ElevatedButton("Exportar Contatos"), 
        padding=5,
        width=300
    )

    c8= ft.Container(
        content = ft.ElevatedButton("Salvar Contato"), 
        padding=5,
        width=300
    )

    page.add(c0, c1, c2, c3, c4, c5, c6, c7, c8)    

#ft.app(target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)