import yaml
import sys
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox, QInputDialog, QFileDialog


class YamlEditor(QMainWindow):

    def __init__(self, yaml_file):
        super().__init__()
        self.yaml_file = yaml_file
        self.yaml_data = self.load_yaml()

        # Create widgets
        self.prompt_label = QLabel("Prompt:")
        self.prompt_edit = QLineEdit(self.yaml_data["imageArgs"]["prompt"])
        self.tags_label = QLabel("Tags:")
        self.tags_edit = QLineEdit(", ".join(self.yaml_data["frontMatter"]["tags"]))
        self.title_label = QLabel("Title:")
        self.title_edit = QLineEdit(self.yaml_data["frontMatter"]["title"])
        self.description_label = QLabel("Description:")
        self.description_edit = QTextEdit(self.yaml_data["frontMatter"]["description"])
        self.sections_label = QLabel("Sections:")
        self.sections_list = QListWidget()
        # self.sections_list.addItems(self.yaml_data.get("sections", []))
        self.add_section_button = QPushButton("Add Section")
        self.remove_section_button = QPushButton("Remove Section")
        self.save_button = QPushButton("Save")

        self.load_button = QPushButton("Load YAML")

        # Connect signals
        self.add_section_button.clicked.connect(self.add_section)
        self.remove_section_button.clicked.connect(self.remove_section)
        self.save_button.clicked.connect(self.save_yaml)

        self.load_button.clicked.connect(self.external_yaml)

        # Set layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.prompt_label, 0, 0)
        grid_layout.addWidget(self.prompt_edit, 0, 1)
        grid_layout.addWidget(self.tags_label, 1, 0)
        grid_layout.addWidget(self.tags_edit, 1, 1)
        grid_layout.addWidget(self.title_label, 2, 0)
        grid_layout.addWidget(self.title_edit, 2, 1)
        grid_layout.addWidget(self.description_label, 3, 0)
        grid_layout.addWidget(self.description_edit, 3, 1)
        main_layout.addLayout(grid_layout)
        main_layout.addWidget(self.sections_label)
        main_layout.addWidget(self.sections_list)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_section_button)
        buttons_layout.addWidget(self.remove_section_button)
        main_layout.addLayout(buttons_layout)
        central_widget.setLayout(main_layout)
        # add another section for save button and load button
        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.addWidget(self.save_button)
        bottom_buttons_layout.addWidget(self.load_button)
        main_layout.addLayout(bottom_buttons_layout)
        self.setCentralWidget(central_widget)

    def set_values_from_yaml():
        # when the yaml file is loaded, set the values in the editor
        pass
    def external_yaml(self):
        # file_dialog.setNameFilter()
        file_dialog = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter="YAML files (*.yaml *.yml)",
        )
        filename, filter_name = file_dialog
        print("filename", filename)
        print("filter_name", filter_name)

        self.yaml_file = filename
        self.yaml_data = self.load_yaml()

    def load_yaml(self):
        try:
            with open(self.yaml_file, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return {"imageArgs": {"prompt": ""}, "frontMatter": {"tags": [], "title": "", "description": ""}}

    def add_section(self):
        section, ok = QInputDialog.getText(self, "Add Section", "Enter section title:")
        if ok and section:
            self.sections_list.addItem(section)

    def remove_section(self):
        current_row = self.sections_list.currentRow()
        if current_row != -1:
            self.sections_list.takeItem(current_row)

    def save_yaml(self):
        self.yaml_data["imageArgs"]["prompt"] = self.prompt_edit.text()
        self.yaml_data["frontMatter"]["tags"] = [tag.strip() for tag in self.tags_edit.text().split(",")]
        self.yaml_data["frontMatter"]["title"] = self.title_edit.text()
        self.yaml_data["frontMatter"]["description"] = self.description_edit.toPlainText()
        # save sections if they exist
        if self.sections_list.count() > 0:
            self.yaml_data["sections"] = [self.sections_list.item(i).text() for i in range(self.sections_list.count())]
        with open("data.yaml", "w") as f:
            yaml.dump(self.yaml_data, f)

        # Show a message box to indicate that the data has been saved
        msg_box = QMessageBox()
        msg_box.setText("Data has been saved.")
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = YamlEditor("posts/chatgpt_chrome_extension.yml")
    editor.show()
    sys.exit(app.exec())