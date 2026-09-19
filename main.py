from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock


class AlarmApp(App):
    def build(self):
        self.title = "ABK - by Top1fnan"
        self.alarm_time = None
        self.alarm_triggered = False

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # اسمك هنا فوق الساعة
        root.add_widget(Label(text="Top1fnan", font_size=14))

        self.clock_label = Label(text="00:00:00", font_size=48)
        root.add_widget(self.clock_label)

        root.add_widget(Label(text="Set alarm time (HH:MM):"))

        self.time_input = TextInput(
            hint_text="e.g. 07:30",
            multiline=False,
            font_size=24,
            size_hint_y=None,
