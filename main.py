from playsound import playsound
import os
from pathlib import Path

music = Path("./mymusic")

if not music.exists():
    print('No music folder found, Make a new folder titled "mymusic" in the same directory as main.py. Press Ctrl + C to exit.')
else:
    print("Available songs:\n")
    
    songs = [file for file in os.listdir("./mymusic") if file.endswith(".mp3")]
    
    for file in songs:
        print(f"- {file}")
    
    print("\n")
    chosen_song = input("Enter song name or number: ").strip().lower()
    
    matched_song = None
    for file in songs:
        if chosen_song in file.lower():
            matched_song = file
            break
            
    if matched_song:
        song_path = music / matched_song
        print(f"Playing: {matched_song}...")
        playsound(str(song_path))
    else:
        print("No matching song found. Make sure the spelling or number is correct!")
