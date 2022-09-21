import pyttsx3
import PyPDF2
import pygame

engine=pyttsx3.init()
book=open('TheMountainIsYou.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(book)

pages=pdf_reader.getNumPages()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate =165
engine.setProperty('rate',newVoiceRate)

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("out-of-time-15474.mp3")
sound.set_volume(0.1)

def start():
    for num in range(10,pages):
        page=pdf_reader.getPage(num)
        text1=page.extract_text()

        engine.say(text1)
        
        sound.play()
        engine.runAndWait()
    

start()