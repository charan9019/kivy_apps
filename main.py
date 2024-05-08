from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.username = "admin"
        self.password = "admin9019"
        self.login_layout = BoxLayout(orientation='vertical')

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        self.login_button = Button(text='Login', on_press=self.check_credentials)
        self.exit_button = Button(text='Exit', on_press=self.exit_app)
        self.error_label = Label(text='', color=(1, 0, 0, 1))

        self.login_layout.add_widget(self.username_input)
        self.login_layout.add_widget(self.password_input)
        self.login_layout.add_widget(self.login_button)
        self.login_layout.add_widget(self.exit_button)
        self.login_layout.add_widget(self.error_label)

        return self.login_layout

    def check_credentials(self, instance):
        if self.username_input.text == self.username and self.password_input.text == self.password:
            self.login_layout.clear_widgets()
            self.build_calculator()
        else:
            self.error_label.text = 'Incorrect username or password'

    def build_calculator(self):
        self.expression = ""
        layout = BoxLayout(orientation='vertical')

        self.display = Button(text='0', font_size=40, size_hint_y=None, height=100)
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['C'],  # Clear button
            ['Exit']  # Exit button
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        self.login_layout.add_widget(layout)

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif instance.text == 'C':  # Clear button pressed
            self.expression = ""
        elif instance.text == 'Exit':  # Exit button pressed
            App.get_running_app().stop()
        else:
            if instance.text not in ['+', '-', '*', '/']:
                self.expression += instance.text
            else:
                if self.expression and self.expression[-1] in ['+', '-', '*', '/']:
                    self.expression = self.expression[:-1]
                self.expression += instance.text

        self.display.text = self.expression

    def exit_app(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    CalculatorApp().run()