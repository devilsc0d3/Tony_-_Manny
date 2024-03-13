import sqlite3
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView


class ReservationScreen(Screen):
    def __init__(self, **kwargs):
        super(ReservationScreen, self).__init__(**kwargs)

        layout = ScrollView()  # Use a ScrollView to handle scrolling if needed
        self.add_widget(layout)

        self.inner_layout = BoxLayout(orientation='vertical', spacing=10, padding=[50, 50])
        layout.add_widget(self.inner_layout)

        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Background color
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])
        self.bind(size=self._update_background, pos=self._update_background)

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size
