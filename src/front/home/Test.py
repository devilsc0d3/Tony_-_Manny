from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label


class TestScreen(Screen):
    place_button = ObjectProperty(None)
    c_and_c_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        self.get_json_datas()

    def move_place(self):
        self.manager.current = 'place'

    def move_c_c(self):
        self.manager.current = 'c_c'

    def move_order(self):
        self.manager.current = 'order'

    def move_setting(self):
        self.manager.current = 'setting'

    def on_back_press(self):
        session = JsonStore('session.json')
        session.clear() # delete everything in the json
        self.manager.current = 'login'

    def get_json_datas(self):
        session = JsonStore('session.json')
        data = session.get('user')

        first_name = data['first_name']
        first_name_label = Label(text=f'First Name: {first_name}', color=(0, 0, 0, 1), font_size='20sp',
                                 size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
        self.add_widget(first_name_label)

        last_name = data['last_name']
        last_name_label = Label(text=f'Last Name: {last_name}', color=(0, 0, 0, 1), font_size='20sp',
                                size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
        self.add_widget(last_name_label)
