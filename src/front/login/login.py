import sqlite3

from kivy.app import App
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Background color
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])
        self.bind(size=self._update_background, pos=self._update_background)

        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = [50, 50]

        self.title_label = Label(text='Tonny & Manny', color=(1, 1, 1, 1), font_size='30sp',
                                 size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(self.title_label)

        self.username_input = TextInput(hint_text='Username', multiline=False, size_hint=(None, None),
                                        size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', multiline=False, password=True,
                                        size_hint=(None, None), size=(300, 40),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.password_input)

        self.login_button = Button(text='Login', size_hint=(None, None), size=(150, 50),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.login_button.bind(on_press=self.check_login)
        self.add_widget(self.login_button)

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def check_login(self, instance):
        # Replace this with your actual login logic
        connection = sqlite3.connect('./database/sql.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE first_name = ?', (self.username_input.text,))
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        print(rows)

        if len(rows) > 0:
            print('Login successful!')
            self.manager.current = 'test'  # Transition to home screen
        else:
            print('Invalid username or password')
