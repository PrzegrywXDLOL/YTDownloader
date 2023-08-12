from pytube import YouTube

print("""

██╗   ██╗████████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
╚██╗ ██╔╝╚══██╔══╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝    ██║   ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
  ╚██╔╝     ██║   ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
   ██║      ██║   ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
   ╚═╝      ╚═╝   ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                        """)

link = input("Podaj link do filmu: ")
yt = YouTube(link)
print("Tytuł: ",yt.title)
print("Liczba wyświetleń: ",yt.views)
print("Długość: ",yt.length,"seconds")
czyok = input("Czy wszystko się zgadza?(T/N): ")

if czyok == "T" or czyok == "t":
    ys = yt.streams.get_highest_resolution()
    print("Pobieranie...")
    ys.download("Pobrane filmy")
    print("Pobieranie zakończone!!")
    i = input()

elif czyok == "N" or czyok == "n":
    print("Zamykam program")
    i = input()
