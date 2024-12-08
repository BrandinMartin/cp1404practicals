"""
CP1404 prac_08
Converting miles to km program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesToKm(App):
    output_km = StringProperty("0.0")

    def build(self):
        """Builds the app"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handles the calculation of miles to km"""
        miles = self.convert_text_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handles incrementation (either up or down)"""
        miles = self.convert_text_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        """Updates the result"""
        self.output_km = str(miles * MILES_TO_KM)

    def convert_text_to_number(self, text):
        """Converts the text into a number if """
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesToKm().run()

