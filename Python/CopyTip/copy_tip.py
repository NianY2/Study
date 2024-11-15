"""
复制成功发出提示音
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyperclip
"""
import pyperclip
import time
def tip():
    """提示"""
    import winsound
    duration = 500  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)


def check_clipboard():
    """监听剪贴板"""
    previous_text = pyperclip.paste()
    while True:
        time.sleep(0.2)
        current_text = pyperclip.paste()
        if current_text != previous_text:
            print(previous_text,current_text)
            tip()
            previous_text = current_text


if __name__ == "__main__":
    check_clipboard()