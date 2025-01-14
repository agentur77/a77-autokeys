from datetime import datetime
current_date = datetime.now().strftime("%d.%m.%y")
keyboard.send_keys("<ctrl>+<shift>+u+2728")
time.sleep(.1)
keyboard.send_keys(f' VORSCHLAG {current_date} | X Std. |')