import flet as ft

class SignUpForm(ft.UserControl):
    def __init__(self, submit_values, btn_signin):
        super().__init__()
        self.submit_values = submit_values 
        self.btn_signin = btn_signin 
    
    def _btn_signup(self, e):
        if not self.text_user.value:
            self.text_user.error_text = "Name cannot be blank!"
            self.text_user.update()
        if not self.text_password.value:
            self.text_password.error_text = "Password cannot be blank!"
            self.text_password.update()
        else:
            self.submit_values(self.text_user.value, self.text_password.value)
    
    def build(self):
        return ft.Container(
            width=500,
            height=560,
            bgcolor=ft.colors.TEAL_800,
            padding=30,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    self._create_title_form(),
                    ft.Container(height=30),
                    self._create_user_input(),
                    self._create_password_input(),
                    ft.Container(height=10),
                    self._create_signup_button(),
                    ft.Container(height=20),
                    self._create_signin_link(),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    
    def _create_title_form(self):
        return ft.Text(value="Create your account", text_align=ft.TextAlign.CENTER, size=30)
    
    def _create_user_input(self):
        self.text_user = ft.TextField(label="User Name")
        return self.text_user
    
    def _create_password_input(self):
        self.text_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
        return self.text_password
    
    def _create_signup_button(self):
        return ft.ElevatedButton(text="Sign up", color=ft.colors.WHITE, width=150, height=50, on_click=self._btn_signup)
    
    def _create_signin_link(self):
        return ft.Row(
            controls=[
                ft.Text(value="Already have an account?"),
                ft.TextButton(text="Sign in", on_click=self.btn_signin),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
