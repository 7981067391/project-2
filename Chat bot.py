from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
import random
import datetime


class ChatBotApp(App):
    def build(self):
        self.title = "ChatBot Interface"

        self.root = BoxLayout(orientation='vertical', spacing=10)

        self.chat_history = ScrollView()
        self.chat_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.chat_history.add_widget(self.chat_layout)

        self.message_input = TextInput(hint_text="Type your message...", multiline=False, size_hint_y=None, height=40)

        self.send_button = Button(text="Send", size_hint_y=None, height=40, on_press=self.send_message)

        self.time_label = Label(text="", color=(0.5, 0.5, 0.5, 1), size_hint_y=None, height=20)
        Clock.schedule_interval(self.update_time, 1)  # Update time every second

        self.root.add_widget(self.chat_history)
        self.root.add_widget(self.message_input)
        self.root.add_widget(self.send_button)
        self.root.add_widget(self.time_label)

        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Light gray background

        return self.root

    def send_message(self, instance):
        user_message = self.message_input.text.strip()
        if user_message:
            user_message_label = Label(text="You: " + user_message, color=(0.1, 0.5, 0.1, 1), size_hint_y=None,
                                       height=30)
            bot_response = get_response(user_message)
            bot_response_label = Label(text="Chatbot: " + bot_response, color=(0, 0.2, 0.6, 1), size_hint_y=None,
                                       height=30)

            self.chat_layout.add_widget(user_message_label)
            self.chat_layout.add_widget(bot_response_label)

            self.message_input.text = ""
            self.chat_history.scroll_to(bot_response_label)

    def update_time(self, dt):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.text = "Current Time: " + current_time


# Rest of the code (get_response function, if __name__ == '__main__', etc.)

if __name__ == '__main__':
    ChatBotApp().run()
