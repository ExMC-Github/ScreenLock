import tkinter as tk
import os
from tkinter import messagebox
import threading
import sys
b = ""
result_ready = False
def create_input_window(txt,parent):
    root = tk.Tk()
    root.parent=parent
    """创建输入窗口并返回用户输入的内容"""
    global b, result_ready

    user_input = ""  # 存储用户输入的内容
    result_ready = False  # 重置标志
    def on_confirm():
        """确认按钮的回调函数"""
        txt[0] = True
        global b, result_ready
        user_input = entry.get()  # 获取输入框内容
        b = user_input
        result_ready = True
        root.quit()  # 退出主循环
        root.destroy()  # 关闭窗口

    def on_cancel():
        """取消按钮的回调函数"""
        txt[0] = True
        global b, result_ready
        user_input = ""  # 设置为空
        b = ""
        result_ready = True
        root.quit()  # 退出主循环
        root.destroy()  # 关闭窗口

    def on_closing():
        """窗口关闭事件处理"""
        on_cancel()  # 点击关闭按钮视为取消

    def on_focus_out(event):
        if txt[0] == False:
            global b, result_ready
            user_input = ""  # 设置为空
            b = ""
            result_ready = True
            root.quit()  # 退出主循环
            root.destroy()  # 关闭窗口


    root.title("输入窗口")
    root.geometry("300x120")
    root.resizable(False, False)  # 禁止调整窗口大小
    if os.path.exists('icon.ico'):
        root.iconbitmap('icon.ico')
    elif os.path.exists(sys._MEIPASS + '\\icon.ico'):
        root.iconbitmap(sys._MEIPASS + '\\icon.ico')
    elif os.path.exists('_INTERNAL\\icon.ico'):
        root.iconbitmap('_INTERNAL\\icon.ico')

    # 绑定窗口关闭事件
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # 创建输入标签
    label = tk.Label(root, text="请输入文本:", font=("Arial", 12))
    label.pack(pady=10)

    # 创建输入框
    entry = tk.Entry(root, width=40, font=("Arial", 12))
    entry.config(show="*")
    entry.pack(pady=5, padx=10)
    entry.focus_set()  # 设置焦点到输入框

    # 绑定回车键到确认按钮
    entry.bind("<Return>", lambda event: on_confirm())

    # 创建按钮框架
    button_frame = tk.Frame(root)
    button_frame.pack()

    # 创建确认按钮
    confirm_button = tk.Button(
        button_frame,
        text="确认",
        command=on_confirm,
        width=10,
        font=("Arial", 10)
    )
    confirm_button.pack(side=tk.LEFT, padx=10)

    # 创建取消按钮
    cancel_button = tk.Button(
        button_frame,
        text="取消",
        command=on_cancel,
        width=10,
        font=("Arial", 10)
    )
    cancel_button.pack(side=tk.LEFT, padx=10)


    root.grab_set()  # 设置为模态窗口
    root.attributes('-topmost', True)
    entry.bind("<FocusOut>", on_focus_out)
    root.attributes('-toolwindow', True)
    entry.focus_force()
    root.mainloop()

    return b


