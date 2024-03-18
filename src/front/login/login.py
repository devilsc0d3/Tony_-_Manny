import hashlib
import sqlite3

from kivy.app import App
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from src.user.user_controllers import user_login_controller


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

        self.subtitle_label = Label(text='Login', color=(1, 1, 1, 1), font_size='30sp',
                                 size_hint=(None, None), size=(250, 50), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(self.subtitle_label)

        self.username_input = TextInput(hint_text='Username', multiline=False, size_hint=(None, None),
                                        size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', multiline=False, password=True,
                                        size_hint=(None, None), size=(300, 40),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.password_input)

        self.login_button = Button(text='Login', size_hint=(None, None), size=(145, 50),
                                   pos_hint={'center_x': 0.4, 'center_y': 0.3})
        self.login_button.bind(on_press=self.check_login)
        self.add_widget(self.login_button)

        self.registration_button = Button(text='Registration', size_hint=(None, None), size=(145, 50),
                                   pos_hint={'center_x': 0.6, 'center_y': 0.3})
        self.registration_button.bind(on_press=self.move_to_registration_page)
        self.add_widget(self.registration_button)

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def check_login(self, instance):
        # hash datas
        hashed_phone_number = hashlib.sha256(self.first_name_input.text.encode('utf-8')).hexdigest()
        hashed_password = hashlib.sha256(self.last_name_input.text.encode('utf-8')).hexdigest()
        try:
            result = user_login_controller(hashed_phone_number, hashed_password)
        except Exception as err:
            print(err)
        else:
            if result != "":
                print(result)
            else:
                "User logged successfully"

    def move_to_registration_page(self, instance):
        self.manager.current = 'registration'  # Transition to registration screen