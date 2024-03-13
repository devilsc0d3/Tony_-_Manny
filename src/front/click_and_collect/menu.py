import sqlite3
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

        self.spacing = None
        layout = ScrollView()  # Use a ScrollView to handle scrolling if needed
        self.add_widget(layout)

        self.inner_layout = BoxLayout(orientation='vertical', spacing=10, padding=[50, 50])
        layout.add_widget(self.inner_layout)

        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Background color
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])
        self.bind(size=self._update_background, pos=self._update_background)

        self.title_label = Label(text='Menu', color=(1, 1, 1, 1), font_size='30sp',
                                 size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.load_menu_from_database()

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def load_menu_from_database(self):
        # Connect to the database
        connection = sqlite3.connect('./database/sql.db')
        cursor = connection.cursor()

        # Fetch menu items from the database
        cursor.execute('SELECT * FROM dishes')
        menu_items = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Display menu items in the MenuScreen
        for item in menu_items:
            self.inner_layout.add_widget(Label(text=item[2]))
            self.inner_layout.add_widget(Label(text=''))
        print(menu_items)
