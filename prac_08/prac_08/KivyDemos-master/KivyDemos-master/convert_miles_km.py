"""
CP1404 prac_08
Converting miles to km program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesToKmApp(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKmApp().run()
