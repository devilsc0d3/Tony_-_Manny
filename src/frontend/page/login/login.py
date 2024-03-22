from kivy.graphics import RoundedRectangle, Color
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from src.backend.user.user_controllers import *


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

        self.phone_number_input = TextInput(hint_text='Phone number', multiline=False, size_hint=(None, None),
                                            size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.phone_number_input)

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
        hashed_phone_number = hashlib.sha256(self.phone_number_input.text.encode('utf-8')).hexdigest()
        try:
            result = user_login_controller(hashed_phone_number, self.password_input.text, self.phone_number_input.text)
        except Exception as err:
            print("exception user login controller: ", err)
        else:
            if result != "":
                print("result: ", result)
            else:
                # load datas from the session
                session = JsonStore('session.json')

                user = user_get_by_phone_number_controller(hashed_phone_number, self.phone_number_input.text)
                user_id = user[0][0]
                first_name = user[0][1]
                last_name = user[0][2]
                # add user into session.json
                session.put("user", id=user_id, first_name=first_name, last_name=last_name,
                            phone_number=self.phone_number_input.text)

                self.manager.current = 'home'

                print("User logged successfully")

    def move_to_registration_page(self, instance):
        self.manager.current = 'registration'  # Transition to registration screen