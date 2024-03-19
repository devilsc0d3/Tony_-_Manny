import sqlite3

from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.checkbox_dict = {}
        self.checked_items = []

        self.load_menu_from_database()

    def on_back_press(self):
        self.manager.current = 'test'

    def load_menu_from_database(self):
        connection = sqlite3.connect('./database/sql.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM dishes')
        menu_items = cursor.fetchall()

        cursor.close()
        connection.close()

        inner_layout = self.ids.inner_layout
        inner_layout.clear_widgets()

        for item in menu_items:
            menu_item_layout = BoxLayout(size_hint_y=None, height=dp(50), spacing=10)

            checkbox = CheckBox(size_hint=(None, None), size=(dp(30), dp(30)))
            checkbox.bind(active=self.on_checkbox_active)
            menu_item_layout.add_widget(checkbox)
            self.checkbox_dict[item[0]] = checkbox

            label = Label(text=str(item[2]), color=(0, 0, 0, 1), size_hint_x=None, width=dp(300))
            menu_item_layout.add_widget(label)

            # Ajouter le BoxLayout de l'élément du menu à inner_layout
            inner_layout.add_widget(menu_item_layout)

    def on_validate_button_press(self):
        print("Items cochés :", self.checked_items)

    def on_checkbox_active(self, checkbox, value):
        for item_id, chkbox in self.checkbox_dict.items():
            if chkbox == checkbox:
                item_id = int(item_id)
                if value:
                    print(f'Checkbox with id {item_id} is active')
                    self.checked_items.append(item_id)
                else:
                    print(f'Checkbox with id {item_id} is inactive')
                    self.checked_items.remove(item_id)
                break
