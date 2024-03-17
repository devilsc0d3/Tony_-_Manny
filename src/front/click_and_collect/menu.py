import sqlite3
from kivy.graphics import RoundedRectangle, Color
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.checkbox_dict = {}  # Initialisez le dictionnaire ici
        self.checked_items = []  # Initialisez la liste des éléments cochés

        self.active = None
        self.spacing = None
        layout = ScrollView()  # Utilisez un ScrollView pour gérer le défilement si nécessaire
        self.add_widget(layout)

        self.inner_layout = BoxLayout(orientation='vertical', spacing=10, padding=[50, 50])
        layout.add_widget(self.inner_layout)

        with self.canvas.before:
            Color(1, 0.6, 0.8, 1)  # Couleur de fond
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])
        self.bind(size=self._update_background, pos=self._update_background)

        self.back = Button(text="Back", size_hint=(None, None), size=(100, 50),
                           pos_hint={'center_x': 0.1, 'center_y': 0.9})
        self.back.bind(on_press=self.on_back_press)
        self.add_widget(self.back)

        self.title_label = Label(text='Menu', color=(1, 1, 1, 1), font_size='30sp',
                                 size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(self.title_label)

        self.load_menu_from_database()

        self.validate_button = Button(text="Valider", size_hint=(None, None), size=(100, 50))
        self.validate_button.bind(on_press=self.on_validate_button_press)
        self.add_widget(self.validate_button)

    def on_back_press(self, instance):
        self.manager.current = 'test'

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def load_menu_from_database(self):
        connection = sqlite3.connect('./database/sql.db')
        cursor = connection.cursor()

        # Récupérer les éléments du menu depuis la base de données
        cursor.execute('SELECT * FROM dishes')
        menu_items = cursor.fetchall()

        # Fermer le curseur et la connexion
        cursor.close()
        connection.close()

        # Initialiser inner_layout
        inner_layout = self.inner_layout
        inner_layout.clear_widgets()  # Effacer les widgets existants avant d'en ajouter de nouveaux

        # Ajouter les éléments du menu à inner_layout avec des cases à cocher
        i = 0.5
        for item in menu_items:
            checkbox = CheckBox()
            checkbox.size_hint = (None, None)
            checkbox.size = (dp(30), dp(30))
            checkbox.pos_hint = {'center_x': 0.5, 'center_y': i}
            checkbox.bind(active=self.on_checkbox_active)
            inner_layout.add_widget(checkbox)
            self.checkbox_dict[item[0]] = checkbox  # Associer l'id de l'élément à la case à cocher
            label = Label(text=str(item[2]), size_hint=(None, None), size=(300, 50))
            inner_layout.add_widget(label)
            i += 0.1

    def on_validate_button_press(self, instance):
        print("Items cochés :", self.checked_items)

    def on_checkbox_active(self, checkbox, value):
        for item_id, chkbox in self.checkbox_dict.items():
            if chkbox == checkbox:
                item_id = int(item_id)
                if value:
                    print(f'Checkbox with id {item_id} is active')
                    self.checked_items.append(item_id)  # Ajoutez l'id de l'élément à la liste des éléments cochés
                    # Faites ce que vous avez à faire avec l'id de l'élément ici
                else:
                    print(f'Checkbox with id {item_id} is inactive')
                    self.checked_items.remove(item_id)  # Retirez l'id de l'élément de la liste des éléments cochés
                    # Faites ce que vous avez à faire avec l'id de l'élément ici
                break
