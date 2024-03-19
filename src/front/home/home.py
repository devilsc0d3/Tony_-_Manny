import json

from kivy.app import App
from kivy.graphics import RoundedRectangle, Color
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from src.user.User import User


class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

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

        self.place_button = Button(text='choice a place', size_hint=(None, None), size=(150, 50),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.place_button.bind(on_press=self.move_place)
        self.add_widget(self.place_button)

        self.c_and_c_button = Button(text='click and collect', size_hint=(None, None), size=(150, 50),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.c_and_c_button.bind(on_press=self.move_c_c)
        self.add_widget(self.c_and_c_button)

        session = JsonStore('session.json')
        user_info = session.get('user')

        first_name = user_info.get('first_name')
        first_name_label = Label(text=f'First Name: {first_name}', color=(0, 0, 0, 1), font_size='20sp',
                                 size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
        self.add_widget(first_name_label)
        last_name = user_info.get('last_name')
        last_name_label = Label(text=f'Last Name: {last_name}', color=(0, 0, 0, 1), font_size='20sp',
                                size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
        self.add_widget(last_name_label)
        phone_number = user_info.get('phone_number')
        phone_label = Label(text=f'Phone Number: {phone_number}', color=(0, 0, 0, 1), font_size='20sp',
                            size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
        self.add_widget(phone_label)
        print("first_name:", first_name)
        print("last", last_name)
        print("phon", phone_number)
        print("AAAA", self.get_json())


    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def move_place(self, instance):
        self.manager.current = 'place'  # Transition to home screen

    def move_c_c(self, instance):
        self.manager.current = 'c_c'  # Transition to home screen

    def initialize_user(self, user_info):
        if user_info:
            first_name = user_info.get('first_name')
            first_name_label = Label(text=f'First Name: {first_name}', color=(1, 1, 1, 1), font_size='20sp',
                                size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
            self.add_widget(first_name_label)
            last_name = user_info.get('last_name')
            last_name_label = Label(text=f'Last Name: {last_name}', color=(1, 1, 1, 1), font_size='20sp',
                                size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
            self.add_widget(last_name_label)
            phone_number = user_info.get('phone_number')
            phone_label = Label(text=f'Phone Number: {phone_number}', color=(1, 1, 1, 1), font_size='20sp',
                                size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
            self.add_widget(phone_label)
        else:
            print("User information not available.")

    def get_json(self):
        session = JsonStore('session.json')
        data = session.get('user')
        user = User(data['user']['first_name'], data['user']['last_name'], data['user']['phone_number'])
        print(data[user]['first_name'])
