from tkinter import *
import ctypes
import sys
from types import ModuleType
import redirect
import os
import time
debug = False
if os.path.exists('wb.rxs'):
    wb_lib = redirect.decrypt_rxs_file(open('wb.rxs', 'rb').read())
else:
    if os.path.exists(sys._MEIPASS + '\\wb.rxs'):
        wb_lib = redirect.decrypt_rxs_file(open(sys._MEIPASS + '\\wb.rxs', 'rb').read())
    else:
        if os.path.exists('_INTERNAL\\wb.rxs'):
            wb_lib = redirect.decrypt_rxs_file(open('_INTERNAL\\wb.rxs', 'rb').read())
        else:
            sys.exit(1)

wb_module = ModuleType('wb')
exec(wb_lib, wb_module.__dict__)
sys.modules['wb'] = wb_module
import wb
import hashlib
txt = [False]
a = False
def get_screen_resolution_windows():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return width, height

def on_window_click(event):
    global debug
    global a
    global txt
    width, height = get_screen_resolution_windows()
    if debug == True:
        sys.exit(0)
    elif a == False:
        a=True
        txt[0]=False
        wb.create_input_window(txt,root)
        if txt[0] == True and wb.b:
            sha256_hash = hashlib.sha256()
            text_bytes = wb.b.encode('utf-8')
            sha256_hash.update(text_bytes)
            hash_result = sha256_hash.hexdigest()
            if (hash_result == "49ada8b20a413bd31de9289a332bf56e2bc1723d8822e20c6c4b41c1deffb591"):
                sys.exit(0)
            else:
                if (hash_result == "425ec43eb6463d01e55fecbbf03fdb120b1865140953f1a279944481ff8e5fc7"):
                    sys.exit(0)
                else:
                    if (hash_result == "9c9832acc3e41cc083ae90fb8f1b7c24a0c97e43fa520394035ead99cbfa0da8"):
                        sys.exit(0)
            a = False
        else:
            a = False
def periodic_update(root, width, height):
    # 1s 检测
    width, height = get_screen_resolution_windows()
    root.geometry(f"{width}x{height}")
    root.after(1000, periodic_update, root, width, height)

if __name__ == "__main__":
    root = Tk()
    width, height = get_screen_resolution_windows()
    root.geometry(f"+{0}+{0}")
    root.geometry(f"{width}x{height}")


    def set_window_opacity(hwnd, opacity):
        ctypes.windll.user32.SetWindowLongW(
            hwnd,
            -20,
            ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x80000  # WS_EX_LAYERED
        )

        # 设置透明度
        ctypes.windll.user32.SetLayeredWindowAttributes(
            hwnd,
            0,
            opacity,
            2
        )


    root['bg'] = 'black'
    root.overrideredirect(True)
    root.update_idletasks()
    label1 = Label(root,text="ScreenLock @ Made By ExRFy",bg='black',fg='white')
    label1.pack(anchor='nw', padx=20, pady=10)
    label2 = Label(root,text="Version: v1.2.1",bg='black',fg='white')
    label2.pack(anchor='nw', side='bottom', padx=20, pady=10)
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    set_window_opacity(hwnd, 75)
    root.bind('<Button-1>', on_window_click)
    periodic_update(root, width, height)
    root.attributes('-topmost', True)
    root.focus_force()
    root.mainloop()
