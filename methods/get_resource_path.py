import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller打包后的临时文件目录
        base_path = sys._MEIPASS
    else:
        # main.py 所在目录
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(base_path, relative_path)
