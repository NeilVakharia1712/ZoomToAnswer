import keyboard
from Voice_Recognition import start_listening
keyboard.add_word_listener(word='zeus', callback = start_listening, triggers=['space'], match_suffix=False, timeout=2)
while True:
    continue




