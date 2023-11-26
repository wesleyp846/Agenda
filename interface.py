import flet as ft

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 700
    page.update()

    c0= ft.Container(
        content = ft.ElevatedButton("Area do titulo"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c1= ft.Container(
        content = ft.ElevatedButton("Mostar Contatos"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c2= ft.Container(
        content = ft.ElevatedButton("Buscar Contatos"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c3= ft.Container(
        content = ft.ElevatedButton("Incluir Contato"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c4= ft.Container(
        content = ft.ElevatedButton("Editar Contato"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c5= ft.Container(
        content = ft.ElevatedButton("Excluir Contato"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c6= ft.Container(
        content = ft.ElevatedButton("Importar Contatos"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c7= ft.Container(
        content = ft.ElevatedButton("Exportar Contatos"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    c8= ft.Container(
        content = ft.ElevatedButton("Salvar Contato"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    page.add(c0, c1, c2, c3, c4, c5, c6, c7, c8)    

ft.app(target=main)