import flet as ft

class SignInForm(ft.UserControl):
    def __init__(self, submit_values, btn_signup):
        super().__init__()
        self.submit_values = submit_values 
        self.btn_signup = btn_signup 
        
    def _btn_signin(self, e):
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
                    self._create_signin_image(),
                    self._create_title_form(),
                    self._create_user_input(),
                    self._create_password_input(),
                    ft.Container(height=10),
                    self._create_signin_button(),
                    ft.Container(height=20),
                    self._create_signup_link(),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    
    def _create_signin_image(self):
        return ft.Container(
            content=ft.Icon(name=ft.icons.PERSON, color=ft.colors.BLUE, size=100),
            width=120,
            height=120,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
        )
    
    def _create_title_form(self):
        return ft.Text(value="Sign in", text_align=ft.TextAlign.CENTER, size=30)
    
    def _create_user_input(self):
        self.text_user = ft.TextField(label="User Name")
        return self.text_user
    
    def _create_password_input(self):
        self.text_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
        return self.text_password
    
    def _create_signin_button(self):
        return ft.ElevatedButton(text="Sign in", color=ft.colors.WHITE, width=150, height=50, on_click=self._btn_signin)
    
    def _create_signup_link(self):
        return ft.Row(
            controls=[
                ft.Text(value="Don't have an account?"),
                ft.TextButton(text="Sign Up Here", on_click=self.btn_signup),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
