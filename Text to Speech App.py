import PySimpleGUI as pg
import pyttsx3
layout = [
    [pg.Input(key='text'),pg.Button('Speak')],
    [pg.Text('Select Voice Type'),pg.Radio('Male','RADIO',key='-male-',default=True),
     pg.Radio('Female','RADIO',key='-female-')],
    [pg.Text('Volume:'),pg.Text('Speed:',pad=(150,0))],
    [pg.Slider(range=(0,10),default_value=5,orientation='h',size=(20,15),key='-VOLUME-'),
     pg.Slider(range=(0,10),default_value=10,orientation='h',size=(20,15),key='-SPEED-')]
]

window =pg.Window('Text to Speech App',layout)

while True:
    event,values = window.read()
    speaker = pyttsx3.init()
    
    if event== pg.WIN_CLOSED:
        break
    elif event == 'Speak':
        voices = speaker.getProperty('voices') 
        speed = speaker.getProperty('rate')
        volume = speaker.getProperty('volume')   

        text = values['text']
        speed_value = (values['-SPEED-']*20)
        volume_value = (values['-VOLUME-']/10)

        speaker.setProperty('rate',speed_value)
        speaker.setProperty('volume',volume_value)

        if values['-male-']:
           speaker.setProperty('voice', voices[0].id)
        else:
           speaker.setProperty('voice', voices[1].id)
        
        speaker.say(text)
        speaker.runAndWait()
        
window.close()

