from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.utils import platform
from universal_converter import UniversalConverter
import os

class MDConverterApp(App):
    def build(self):
        self.title = "Universal MD Converter"
        
        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Status Label
        self.label = Label(
            text="Select a file to convert", 
            size_hint=(1, 0.1),
            halign="center",
            valign="middle"
        )
        self.layout.add_widget(self.label)

        # File Chooser
        # Default to Downloads folder on Android, current dir on desktop
        default_path = '/storage/emulated/0/Download' if platform == 'android' else '.'
        self.filechooser = FileChooserListView(
            path=default_path,
            filters=['*.xlsx', '*.xls', '*.csv', '*.docx', '*.pdf', '*.txt']
        )
        self.layout.add_widget(self.filechooser)

        # Convert Button
        self.btn = Button(
            text="Convert to Markdown", 
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.8, 1)
        )
        self.btn.bind(on_press=self.convert_file)
        self.layout.add_widget(self.btn)

        return self.layout

    def convert_file(self, instance):
        selection = self.filechooser.selection
        if not selection:
            self.label.text = "Error: No file selected!"
            return

        file_path = selection[0]
        filename = os.path.basename(file_path)
        self.label.text = f"Converting {filename}..."

        try:
            # Output to the same folder as the input file
            output_dir = os.path.dirname(file_path)
            converter = UniversalConverter(output_dir=output_dir)
            
            # Convert to Markdown
            out_path = converter.convert(file_path, output_format="md")
            
            self.label.text = f"Success! Saved as: {os.path.basename(out_path)}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    MDConverterApp().run()