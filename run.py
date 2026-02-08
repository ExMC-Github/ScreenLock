from tkinter import *
import ctypes
import sys
from types import ModuleType
import redirect
import os
import tkinter as tk
from tkinter import messagebox
import threading
import time

def get_meipass():
    return sys._MEIPASS
# 使用示例
if __name__ == '__main__':
    if os.path.exists('main.rxs'):
        code = redirect.decrypt_rxs_file(open('main.rxs', 'rb').read())
    else:
        if os.path.exists(get_meipass() + '\\main.rxs'):
            code = redirect.decrypt_rxs_file(open(get_meipass() + '\\main.rxs', 'rb').read())
        else:
            if os.path.exists('_INTERNAL\\main.rxs'):
                code = redirect.decrypt_rxs_file(open('_INTERNAL\\main.rxs', 'rb').read())
            else:
                sys.exit(1)

    exec(code)
