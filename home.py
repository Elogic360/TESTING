import flet as ft

def main(page: ft.Page):
    page.title = "Maggot Growth Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    def responsive_layout(e):
        page.update()

    # Add a resize listener to update layout on window resize
    page.on_resized = responsive_layout

    # Main content container
    main_container = ft.Container(
        expand=True,
        bgcolor=ft.colors.BLACK,
        padding=50,
        content=ft.Column(
            [
                ft.Text("Welcome to Maggot Growth Tracker", 
                        color=ft.colors.WHITE, 
                        size=30, 
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                ),
                ft.Text("Manage production and track the growth progress of maggots from the early stages up to maturity. Dive into our application to ensure optimal production and growth tracking.", 
                        color=ft.colors.WHITE, 
                        size=18, 
                        text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.CircularProgressIndicator(color=ft.colors.WHITE, size=40),
                            ft.ElevatedButton("Login", on_click=lambda e: print("Login"), color=ft.colors.GREEN),
                            ft.TextButton("Apply for User Account", on_click=lambda e: print("Apply for User Account"), color=ft.colors.BLUE),
                            ft.TextButton("Apply for Admin Account", on_click=lambda e: print("Apply for Admin Account"), color=ft.colors.BLUE),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                    ),
                    margin=ft.EdgeInsets.only(top=20)
                ),
                ft.Text("Features", 
                        color=ft.colors.WHITE, 
                        size=24, 
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.LEFT
                ),
                # You can add more features content here
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )

    page.add(main_container)
    page.update()

ft.app(target=main)
