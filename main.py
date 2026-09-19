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
      height=60,
            halign="center",
        )
        root.add_widget(self.time_input)

        set_btn = Button(text="Set Alarm", size_hint_y=None, height=60)
        set_btn.bind(on_press=self.set_alarm)
        root.add_widget(set_btn)

        self.status_label = Label(text="No alarm set", font_size=18)
        root.add_widget(self.status_label)

        cancel_btn = Button(text="Cancel Alarm", size_hint_y=None, height=60)
        cancel_btn.bind(on_press=self.cancel_alarm)
        root.add_widget(cancel_btn)

        Clock.schedule_interval(self.update_clock, 1)
        return root

    def update_clock(self, dt):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.text = now
        if self.alarm_time and not self.alarm_triggered:
            current_hm = datetime.now().strftime("%H:%M")
            if current_hm == self.alarm_time:
                self.alarm_triggered = True
                self.trigger_alarm()

    def set_alarm(self, instance):
        text = self.time_input.text.strip()
        try:
            datetime.strptime(text, "%H:%M")
            self.alarm_time = text
            self.alarm_triggered = False
            self.status_label.text = f"Alarm set for {text}"
        except ValueError:
            self.status_label.text = "Invalid time format! Use HH:MM"

    def cancel_alarm(self, instance):
        self.alarm_time = None
        self.alarm_triggered = False
        self.status_label.text = "No alarm set"

    def trigger_alarm(self):
        self.status_label.text = f"⏰ ALARM! It's {self.alarm_time}"
        popup = Popup(
            title="Alarm",
            content=Label(text=f"Wake up! It's {self.alarm_time}"),
            size_hint=(0.7, 0.4),
        )
        popup.open()


if __name__ == "__main__":
    AlarmApp().run()
  
