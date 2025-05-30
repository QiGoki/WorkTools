item_to_set = ["w.noSpaceInterface.tp.historyListArea",
               "w.noSpaceInterface.tp.historyListArea.listBox",
               "w.noSpaceInterface.tp.historyListArea.list"]


def get_obj_from_path(root, path):
    obj = root
    for child_path in path.split('.')[1:]:
        obj = getattr(obj, child_path)
        print(obj)
    return obj


class A:
    pass


w = A()
w.noSpaceInterface = A()
w.noSpaceInterface.tp = A()
w.noSpaceInterface.tp.historyListArea = "目标对象"

# 配置文件中有路径字符串
path_test = "w.noSpaceInterface.tp.historyListArea"

# 用getattr链式递归获取
result = get_obj_from_path(w, path_test)
print(result)  # 输出：目标对象
