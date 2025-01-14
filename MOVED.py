from datetime import datetime
current_date = datetime.now().strftime("%d.%m.%y")
keyboard.send_keys("<ctrl>+<shift>+U+1F552 ")
time.sleep(.1)
keyboard.send_keys(f' {current_date} | Verschoben, weil')