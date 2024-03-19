from datetime import datetime

from kivy.metrics import dp
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from src.table.table_services import table_get_all_service, table_add_service
from src.table_reservation.reservation_services import reservation_table_add_service


class ReservationScreen(Screen):
    def __init__(self, **kwargs):
        super(ReservationScreen, self).__init__(**kwargs)
        self.checkbox_dict = {}
        self.checked_tables = []
        self.load_menu_from_database()

    def on_back_press(self):
        self.manager.current = 'home'

    def load_menu_from_database(self):
        menu_items = table_get_all_service()

        inner_layout = self.ids.inner_layout
        inner_layout.clear_widgets()

        for item in menu_items:
            menu_item_layout = (
                BoxLayout(size_hint_y=None,
                          height=dp(50),
                          spacing=10)
            )

            checkbox = CheckBox(size_hint=(None, None), group="table_select", size=(dp(30), dp(30)))
            checkbox.bind(active=self.on_checkbox_active)
            menu_item_layout.add_widget(checkbox)
            self.checkbox_dict[item[0]] = checkbox

            label = Label(text='table ' + str(item[0]) + ' - place ' + str(item[2]), color=(0, 0, 0, 1),
                          size_hint_x=None, width=dp(300))
            menu_item_layout.add_widget(label)

            inner_layout.add_widget(menu_item_layout)

    def on_checkbox_active(self, checkbox, value):
        for item_id, chkbox \
                in (self.checkbox_dict.items()):
            if chkbox == checkbox:
                item_id = int(item_id)
                if value:
                    print(f'Checkbox with id {item_id} is active')
                    self.checked_tables.append(item_id)
                else:
                    print(f'Checkbox with id {item_id} is inactive')
                    self.checked_tables.remove(item_id)
                break

    def on_validate_button_press(self):
        print("Tables check :", self.checked_tables)
        d = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self.load_data()
        reservation_table_add_service(self.checked_tables[0], d, data['id'])

    def load_data(self):
        session = JsonStore('session.json')
        if session.exists('user'):
            data = session.get('user')
        else:
            data = {
                'id': "",
                'first_name': "",
                'last_name': "",
                'phone_number': "",
            }
        return data
