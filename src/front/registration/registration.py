import hashlib

from kivy.app import App
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from src.user.user_controllers import user_add_controller


class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Background color
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])
        self.bind(size=self._update_background, pos=self._update_background)

        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = [50, 50]

        self.title_label = Label(text='Tonny & Manny', color=(1, 1, 1, 1), font_size='30sp',
                                 size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.add_widget(self.title_label)

        self.subtitle_label = Label(text='Registration', color=(1, 1, 1, 1), font_size='30sp',
                                    size_hint=(None, None), size=(250, 50), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(self.subtitle_label)

        self.first_name_input = TextInput(hint_text='First name', multiline=False, size_hint=(None, None),
                                          size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(self.first_name_input)

        self.last_name_input = TextInput(hint_text='Last name', multiline=False,
                                         size_hint=(None, None), size=(300, 40),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.add_widget(self.last_name_input)

        self.phone_number_input = TextInput(hint_text='Phone number', multiline=False,
                                            size_hint=(None, None), size=(300, 40),
                                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.phone_number_input)

        self.password_input = TextInput(hint_text='Password', multiline=False, password=True,
                                        size_hint=(None, None), size=(300, 40),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.password_input)

        self.confirm_password_input = TextInput(hint_text='Confirm password', multiline=False, password=True,
                                                size_hint=(None, None), size=(300, 40),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.add_widget(self.confirm_password_input)
        """
        self.login_button = Button(text='Login', size_hint=(None, None), size=(150, 50),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.login_button.bind(on_press=self.check_login)
        self.add_widget(self.login_button)
        """
        self.registration_button = Button(text='Registration', size_hint=(None, None), size=(150, 50),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.registration_button.bind(on_press=self.check_registration)
        self.add_widget(self.registration_button)

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def check_registration(self, instance):
        # hash datas
        hashed_first_name = hashlib.sha256(self.first_name_input.text.encode('utf-8')).hexdigest()
        hashed_last_name = hashlib.sha256(self.last_name_input.text.encode('utf-8')).hexdigest()
        hashed_phone_number = hashlib.sha256(self.first_name_input.text.encode('utf-8')).hexdigest()
        hashed_password = hashlib.sha256(self.last_name_input.text.encode('utf-8')).hexdigest()
        try:
            result = user_add_controller(hashed_first_name, hashed_last_name, hashed_phone_number, hashed_password)
        except Exception as err:
            print(err)
        else:
            if result != "":
                print(result)
            else:
                "User added successfully"
