# object命名管理类
class UniqueNameManager:
    def __init__(self):
        self.name_set = set()

    def set_unique_object_name(self, widget, name):
        if name in self.name_set:
            raise ValueError(f"objectName '{name}' 已被占用")
        widget.setObjectName(name)
        self.name_set.add(name)
