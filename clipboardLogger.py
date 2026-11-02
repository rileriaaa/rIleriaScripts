import pyperclip, time

print("recording clipboard. (ctrl + c to stop)")
previous_content = ""
try:
    while True:
        content = pyperclip.paste()

        if content != previous_content:
            print(previous_content)
            previous_content = content

        time.sleep(0.01)
except KeyboardInterrupt:
    print(content)
    pass
