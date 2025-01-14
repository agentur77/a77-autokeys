from datetime import datetime
current_date = datetime.now().strftime("%d.%m.%y")
keyboard.send_keys(current_date)