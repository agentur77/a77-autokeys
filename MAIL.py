from datetime import datetime
current_date = datetime.now().strftime("%d.%m.%y")
keyboard.send_keys("<ctrl>+<shift>+u+1f4e7 ")
time.sleep(0.1)
keyboard.send_keys(f' {current_date} | ')