import PySimpleGUI as pg
import qrcode 
layout = [
    [pg.Input(key='data')],
    [pg.Button('Create'),pg.Button('Close')],
    [pg.Image(key='output')]

]
window = pg.Window('QRCODE',layout)

while True:
    event,values = window.read()
    if event == pg.WIN_CLOSED or event == 'Close':
       break
    elif event == 'Create':
        qc = qrcode.make(values['data'])
        qc.save('qr_code.png')
        window['output'].update('qr_code.png')
window.close()


