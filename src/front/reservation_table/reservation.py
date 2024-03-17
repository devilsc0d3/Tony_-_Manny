import sqlite3
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox

from src.table.table_services import table_get_all_service
from src.table_reservation.reservation_services import reservation_table_get_all_service, reservation_table_add_service


class ReservationScreen(Screen):
    def __init__(self, **kwargs):
        super(ReservationScreen, self).__init__(**kwargs)
        self.checkbox_dict = {}  # Initialisez le dictionnaire ici
        self.checked_tables = []  # Initialisez la liste des tables cochées

        layout = ScrollView()  # Utilisez un ScrollView pour gérer le défilement si nécessaire
        self.add_widget(layout)

        self.inner_layout = BoxLayout(orientation='vertical', spacing=10, padding=[50, 50])
        layout.add_widget(self.inner_layout)

        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Couleur de fond
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])
        self.bind(size=self._update_background, pos=self._update_background)

        self.back = Button(text="Back", size_hint=(None, None), size=(100, 50),
                           pos_hint={'center_x': 0.1, 'center_y': 0.9})
        self.back.bind(on_press=self.on_back_press)
        self.add_widget(self.back)

        self.title_label = Label(text='Reservation', color=(1, 1, 1, 1), font_size='30sp',
                                 size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(self.title_label)

        self.reservation_button = Button(text="Réserver", size_hint=(None, None), size=(100, 50),
                                         pos_hint={'center_x': 0.9, 'center_y': 0.9})
        self.reservation_button.bind(on_press=self.on_reservation_button_press)
        self.add_widget(self.reservation_button)

        self.load_reservations_from_database()

    def on_back_press(self, instance):
        self.manager.current = 'test'

    def load_reservations_from_database(self):
        tables = table_get_all_service()

        for table in tables:
            table_id = table[0]
            rank = table[1]
            places = table[2]

            table_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            table_checkbox = CheckBox(size_hint=(None, None), size=(50, 50))
            table_label = Label(text=f"Table {rank} - {places} places", color=(1, 1, 1, 1), font_size='20sp',
                                size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.8})

            table_layout.add_widget(table_checkbox)
            table_layout.add_widget(table_label)

            self.inner_layout.add_widget(table_layout)

            self.checkbox_dict[table_id] = table_checkbox  # Associez l'id de la table à la case à cocher
            table_checkbox.bind(active=self.on_checkbox_active)  # Lier la case à cocher à la méthode on_checkbox_active

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def on_reservation_button_press(self, instance):
        print("Tables cochées :", self.checked_tables)
        d = "2021-12-31 23:59:59"  # Remplacez ceci par la date et l'heure de la réservation
        for table_id in self.checked_tables:
            reservation_table_add_service(table_id, d, 1)

    def on_checkbox_active(self, checkbox, value):
        for table_id, chkbox in self.checkbox_dict.items():
            if chkbox == checkbox:
                if value:
                    print(f'Table with id {table_id} is active')
                    self.checked_tables.append(table_id)  # Ajoutez l'id de la table à la liste des tables cochées
                else:
                    print(f'Table with id {table_id} is inactive')
                    self.checked_tables.remove(table_id)  # Retirez l'id de la table de la liste des tables cochées
                break
