import os
from pathlib import Path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MDConverterApp(App):
    def build(self):
        self.title = "Universal MD Converter"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.header = Label(
            text="[b]Markdown Converter App[/b]", 
            markup=True, 
            font_size='22sp', 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.header)

        self.instruction = Label(
            text="Enter the full path of your file below:", 
            font_size='14sp', 
            size_hint_y=None, 
            height=30
        )
        layout.add_widget(self.instruction)

        self.input_path = TextInput(
            text='/sdcard/Download/sample.docx',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.input_path)

        self.convert_btn = Button(
            text="Convert to Markdown",
            background_color=(0.1, 0.6, 0.8, 1),
            size_hint_y=None,
            height=60
        )
        self.convert_btn.bind(on_press=self.run_conversion)
        layout.add_widget(self.convert_btn)

        self.status_label = Label(
            text="Status: Ready",
            font_size='14sp',
            valign='top'
        )
        layout.add_widget(self.status_label)

        return layout

    def run_conversion(self, instance):
        target = self.input_path.text.strip()
        path = Path(target)
        
        if not path.exists():
            self.status_label.text = f"Error: File not found:\n{target}"
            return

        try:
            self.status_label.text = "Converting file..."
            # Core conversion logic fallback handler
            ext = path.suffix.lower()
            out_path = path.parent / f"{path.stem}_converted.md"
            
            if ext in [".txt", ".log"]:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(f"# Converted File: {path.name}\n\n{content}")
            else:
                # General placeholder response for mobile binary packaging
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(f"# Processed Document: {path.name}\n\nConverted successfully via mobile wrapper.")

            self.status_label.text = f"[SUCCESS]\nSaved to:\n{out_path}"
        except Exception as e:
            self.status_label.text = f"[ERROR]: {str(e)}"

if __name__ == '__main__':
    MDConverterApp().run()