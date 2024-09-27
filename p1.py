from flet import *

#############Value###############
btn1 = ElevatedButton("زربة", color="black", bgcolor="white",)









def main(page: Page):
    page.title = "jalil app"
    page.window_width = 390
    page.window_height = 740
    page.window_top = 1
    page.window_left = 960
    page.bgcolor = "black"










####################################################


    page.add(
        Row(
            controls=[
                Text("برنامج جليل", color="white")
            ],
            alignment=MainAxisAlignment.CENTER),

        Row([
            btn1
            ],alignment=MainAxisAlignment.CENTER),
    )

    page.update()

app(target=main)
