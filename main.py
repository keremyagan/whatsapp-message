from whatsapp import Whatsapp
import pandas as pd

wp=Whatsapp()

df = pd.read_excel('data.xlsx')

text = 'This is my new phone number .'

for number in df[df.columns[0]] :
    wp.send_text(number,text)
