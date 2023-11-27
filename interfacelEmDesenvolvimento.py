import flet as ft

def main(page: ft.Page):
    #Adicionar controles ns pagina
    page.title = "Agenda de Contatos"
    page.padding = 10
    #Tamanho do app
    page.window_width = 400
    page.window_height = 700
    page.update()
    #Caixa de texto

    c1= ft.Container(
        content = ft.Text("Agenda de Contatos", style=ft.TextThemeStyle.DISPLAY_LARGE)
    )

    c2= ft.Container(
        content = ft.ElevatedButton("Salvar Contato"), 
        bgcolor=ft.colors.AMBER,
        padding=5,
        width=300
    )

    #Adicioando o container
    page.add(c1, c2)

    #page.add(ft.Text("AGENDA"))
    

#ft.app(target=main)
#ft.app(port=8550, target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)