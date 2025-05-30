import os
from playsound import playsound
import time

#sounds mapping
sounds_folder = "animal sounds"

letter_to_sound = {}

# getting each letter from alphabets mapped to their respective audio file
for letter in "abcdefghijklmnopqrstuvwxyz":
  filename = f"{letter}.wav"
  filepath = os.path.join(sounds_folder , filename)
  letter_to_sound[letter] = filepath




#user input
sound_name = input("Please input a word in english:").lower()
#playing the corrosponding file to the specific alpabets or sentences
for letter in sound_name:
  if letter in letter_to_sound:
    playsound(letter_to_sound[letter])
    time.sleep(0.01)
  else:
    time.sleep(0.1)




