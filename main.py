import os

url = input("Enter Video Url: ")

only_audio = "-x"

print('''
Select Option: \n
[1]: Both Audio And Video
[2]: Only Audio
[3]: Best Audio + Best Video (Takes more space and more internet)
[4]: Best Audio
''')

option = int(input("Enter Option 1/4: "))

def video_and_audio():
    option = None

def only_audio():
    option = "-x"
    print("Audio Will be saved in .mp3 Format")
    os.system(f"C:\\Users\\dhang\\Desktop\\Python\\youtube-dl.exe {option} {url}")

if __name__ == "__main__":
    if option == 1:
        video_and_audio()

    elif option == 2:
        only_audio()
    
    elif option == 3:
        option = "-f bestvideo+bestaudio"
        os.system(f"C:\\Users\\dhang\\Desktop\\Python\\youtube-dl.exe {option} {url}")
        print("Downloading with best audio and video")

    elif option == 4:
        option = "-x -f bestaudio"
        os.system(f"C:\\Users\\dhang\\Desktop\\Python\\youtube-dl.exe {option} {url}")
        print("Downloading with best audio")
