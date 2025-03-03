import flet as ft

class Message:
    def __init__(self, user: str, text: str, message_type: str):
        self.user = user
        self.text = text
        self.message_type = message_type

class ChatMessage(ft.Row):
    COLOR_PALETTE = [
        ft.colors.AMBER, ft.colors.BLUE, ft.colors.BROWN, ft.colors.CYAN,
        ft.colors.GREEN, ft.colors.INDIGO, ft.colors.LIME, ft.colors.ORANGE,
        ft.colors.PINK, ft.colors.PURPLE, ft.colors.RED, ft.colors.TEAL, ft.colors.YELLOW
    ]
    
    def __init__(self, message: Message):
        super().__init__(vertical_alignment="start")
        self.controls = [
            self._create_avatar(message.user),
            self._create_message_column(message)
        ]
    
    def _create_avatar(self, user: str):
        return ft.CircleAvatar(
            content=ft.Text(self._get_initials(user)),
            color=ft.colors.WHITE,
            bgcolor=self._get_avatar_color(user),
        )
    
    def _create_message_column(self, message: Message):
        return ft.Column(
            [
                ft.Text(message.user, weight="bold"),
                ft.Text(message.text, selectable=True),
            ],
            tight=True,
            spacing=5,
        )
    
    def _get_initials(self, user: str) -> str:
        return user[:1].capitalize()
    
    def _get_avatar_color(self, user: str):
        return self.COLOR_PALETTE[hash(user) % len(self.COLOR_PALETTE)]
