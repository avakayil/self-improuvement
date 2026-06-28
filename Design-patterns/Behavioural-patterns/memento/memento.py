class Editor:
    """
    Originator
    """

    def __init__(self):
        self.text = ""
        self.cur_x = 0
        self.cur_y = 0
        self.selection_width = 0

    def set_text(self, text):
        self.text = text

    def set_cursor(self, x, y):
        self.cur_x = x
        self.cur_y = y

    def set_selection_width(self, width):
        self.selection_width = width

    def create_snapshot(self):
        return Snapshot(
            self,
            self.text,
            self.cur_x,
            self.cur_y,
            self.selection_width,
        )

    def __str__(self):
        return (
            f"Text={self.text}, "
            f"Cursor=({self.cur_x},{self.cur_y}), "
            f"Selection={self.selection_width}"
        )


class Snapshot:
    """
    Memento
    """

    def __init__(self, editor, text, x, y, width):
        self.editor = editor

        self.text = text
        self.cur_x = x
        self.cur_y = y
        self.selection_width = width

    def restore(self):

        self.editor.set_text(self.text)

        self.editor.set_cursor(
            self.cur_x,
            self.cur_y,
        )

        self.editor.set_selection_width(
            self.selection_width
        )


class Command:
    """
    Caretaker
    """

    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def make_backup(self):

        self.backup = self.editor.create_snapshot()

    def undo(self):

        if self.backup:
            self.backup.restore()


# -------------------------

editor = Editor()

editor.set_text("Hello")

editor.set_cursor(10, 20)

editor.set_selection_width(5)

print(editor)

command = Command(editor)

command.make_backup()

editor.set_text("Hello World")

editor.set_cursor(50, 60)

editor.set_selection_width(15)

print(editor)

command.undo()

print(editor)