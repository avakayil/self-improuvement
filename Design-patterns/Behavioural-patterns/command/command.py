from abc import ABC, abstractmethod


# =====================================
# Receiver
# =====================================

class Editor:

    def __init__(self):
        self.text = "Hello World"

    def get_selection(self):
        return self.text

    def delete_selection(self):
        self.text = ""

    def replace_selection(self, text):
        self.text += text


# =====================================
# Command
# =====================================

class Command(ABC):

    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
        self.backup = ""

    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    @abstractmethod
    def execute(self):
        pass


# =====================================
# Copy Command
# =====================================

class CopyCommand(Command):

    def execute(self):

        self.app.clipboard = self.editor.get_selection()

        return False


# =====================================
# Cut Command
# =====================================

class CutCommand(Command):

    def execute(self):

        self.save_backup()

        self.app.clipboard = self.editor.get_selection()

        self.editor.delete_selection()

        return True


# =====================================
# Paste Command
# =====================================

class PasteCommand(Command):

    def execute(self):

        self.save_backup()

        self.editor.replace_selection(
            self.app.clipboard
        )

        return True


# =====================================
# History
# =====================================

class CommandHistory:

    def __init__(self):
        self.history = []

    def push(self, command):
        self.history.append(command)

    def pop(self):

        if self.history:
            return self.history.pop()

        return None


# =====================================
# Application
# =====================================

class Application:

    def __init__(self):

        self.clipboard = ""

        self.editor = Editor()

        self.history = CommandHistory()

    def execute_command(self, command):

        if command.execute():

            self.history.push(command)

    def undo(self):

        command = self.history.pop()

        if command:

            command.undo()


# =====================================
# Client
# =====================================

app = Application()

print("Initial:", app.editor.text)

app.execute_command(
    CutCommand(app, app.editor)
)

print("After Cut:", app.editor.text)

app.execute_command(
    PasteCommand(app, app.editor)
)

print("After Paste:", app.editor.text)

app.undo()

print("Undo Paste:", app.editor.text)

app.undo()

print("Undo Cut:", app.editor.text)