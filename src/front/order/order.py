from kivy.metrics import dp
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from src.table_reservation.reservation_services import *


class OrderScreen(Screen):
    def on_pre_enter(self):
        self.show_reservation()

    def on_back_press(self):
        self.manager.current = 'home'

    def show_reservation(self):
        data = self.load_data()
        reservations = reservation_table_get_service(data['id'])
        # reservations = reservation_table_get_all_service()
        inner_layout = self.ids.inner_layout
        inner_layout.clear_widgets()

        if not reservations:
            inner_layout.add_widget(Label(text="No reservations found !",
                                          padding=10,
                                          color=(0, 0, 0, 1)))
            return
        for reservation in reservations:
            menu_item_layout = BoxLayout(
                size_hint_y=None,
                height=dp(50),
                spacing=10
            )
            print(reservation[2])
            label_text = f"Table {reservation[2]} - Date {reservation[3]}"
            label = Label(text=label_text, color=(0, 0, 0, 1), size_hint_x=None, width=dp(300))

            delete_button = Button(text="remove", size_hint=(None, None), size=(dp(100), dp(50)))
            delete_button.bind(on_press=lambda instance, res=reservation: self.delete_reservation(res))

            commentary_input = TextInput(hint_text=f'{reservation[4]}',
                                         foreground_color=(0, 0, 0, 1),
                                         size_hint_x=None, width=dp(100))
            commentary_button = Button(text="add / update", size_hint=(None, None), size=(dp(100), dp(50)))
            commentary_button.bind(on_press=lambda instance, res=reservation: self.update_commentary_callback(instance, res))

            menu_item_layout.add_widget(label)
            menu_item_layout.add_widget(delete_button)
            menu_item_layout.add_widget(commentary_input)
            menu_item_layout.add_widget(commentary_button)
            inner_layout.add_widget(menu_item_layout)

    def delete_reservation(self, reservation):
        # Call your delete_reservation_service here with the appropriate parameters
        print(f"Deleting reservation {reservation[0]}")
        print(type(reservation[0]))
        reservation_table_delete_service(reservation[0])
        # Refresh reservations after deletion
        self.show_reservation()

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

    def update_commentary_callback(self, instance, reservation):
        for child in instance.parent.children:
            if isinstance(child, TextInput):
                commentary = child.text
                break

        self.update_commentary(reservation[0], commentary)

    def update_commentary(self, reservation, commentary):
        reservation_table_update_commentary(commentary, reservation)
        print(commentary)
        self.show_reservation()
