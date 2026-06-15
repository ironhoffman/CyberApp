import flet as ft


def main(page: ft.Page):
    page.title = "My Tasks"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 800
    page.padding = 20
    page.bgcolor = "#0F172A"

    tasks = ft.Column(spacing=15)

    def add_task(e):
        if task_input.value.strip():
            tasks.controls.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.CHECK_CIRCLE,
                                color="#22C55E",
                            ),
                            ft.Text(
                                task_input.value,
                                size=18,
                                color="white",
                            ),
                        ]
                    ),
                    bgcolor="#1E293B",
                    padding=15,
                    border_radius=20,
                    animate=ft.Animation(400, "easeOut"),
                )
            )

            task_input.value = ""
            page.update()

    title = ft.Text(
        "✨ My Tasks",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="white",
    )

    subtitle = ft.Text(
        "Organize your day",
        color="#94A3B8",
        size=16,
    )

    task_input = ft.TextField(
        hint_text="Enter a task...",
        border_radius=15,
        filled=True,
        bgcolor="#1E293B",
        color="white",
        border_color="transparent",
    )

    add_button = ft.ElevatedButton(
        "Add Task",
        icon=ft.Icons.ADD,
        bgcolor="#3B82F6",
        color="white",
        on_click=add_task,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15)
        ),
    )

    tasks.controls.extend(
        [
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(
                            ft.Icons.CHECK_CIRCLE,
                            color="#22C55E",
                        ),
                        ft.Text(
                            "Learn Python",
                            color="white",
                            size=18,
                        ),
                    ]
                ),
                bgcolor="#1E293B",
                padding=15,
                border_radius=20,
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(
                            ft.Icons.CHECK_CIRCLE,
                            color="#22C55E",
                        ),
                        ft.Text(
                            "Build iPhone app",
                            color="white",
                            size=18,
                        ),
                    ]
                ),
                bgcolor="#1E293B",
                padding=15,
                border_radius=20,
            ),
        ]
    )

    page.add(
        ft.Column(
            [
                title,
                subtitle,
                ft.Divider(color="transparent", height=20),
                task_input,
                add_button,
                ft.Divider(color="transparent", height=10),
                tasks,
            ],
            scroll=ft.ScrollMode.AUTO,
        )
    )


ft.app(target=main)