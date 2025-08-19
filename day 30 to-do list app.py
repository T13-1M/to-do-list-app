import flet as ft

def main(page: ft.Page):
    page.title = "To-DO List"

    def new_task(e):
        if task_input.value:
            task_list.controls.append(
                ft.Checkbox(label=task_input.value)
            )
            task_input.value = ""
            page.update()


    task_input = ft.TextField(hint_text="Add Your Task", expand=True, on_submit=new_task)
    add_task = ft.IconButton(icon=ft.Icons.ADD, on_click=new_task)
    input_line = ft.Row(
        controls = [
            task_input,
            add_task
        ]
    )

    all_tab = ft.Tabs(
        selected_index=1,
        tabs=[
            ft.Tab(text='ALL'),
            ft.Tab(text='Active'),
            ft.Tab(text='Completed')
        ]
    )

    task_list = ft.ListView(expand=True)

    page.add(
        input_line,
        all_tab,
        task_list
    )

ft.app(target=main)