
class Boomerang:

    """Класс погружения и всплытия.
    Используется для того, чтобы работать с обьектами через родительский класс (экран)"""

    def __init__(self):
        self.add_list = []
        self.delete_list = []

    def add_object(self, obj):
        self.add_list.append(obj)

    def remove_object(self, obj):
        self.delete_list.append(obj)

    def is_add_list_empty(self):
        return len(self.add_list) == 0

    def is_delete_list_empty(self):
        return len(self.delete_list) == 0

    def get_add_list(self):
        return self.add_list

    def get_delete_list(self):
        return self.delete_list
