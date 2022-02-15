#!/usr/bin/env python
# coding: utf-8

# In[6]:


import PySimpleGUI as sg
   
      
sg.theme('Black')
   
layout = [[sg.Text('Enter your HexaDecimal Value'),sg.Text(size=(15,1), key='enter your hexadecimal number')],
          [sg.Input(key='enter_your_hexadecimal_number')],
      
         
          [sg.Button('convert'), sg.Button('Exit')],
          
         [sg.Text('Decimal Value:'),sg.Text(size=(40,1), key='Decimal_value')],
         [sg.Text('Binary Value:'),sg.Text(size=(40,1), key='Binary_value')],
         [sg.Text(''),sg.Text(size=(40,1), key='Error_msg',text_color='red',justification='center')]],
         
  
window = sg.Window('HexaDecimal to Decimal and Binary Converter', layout)
while True:
    event, values = window.read()
    print(event, values)
      
    if event in  (None, 'Exit'):
        break
      
    if event == 'convert':
        errorchar = ["G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        hex = values["enter_your_hexadecimal_number"]
        hex = hex.upper()
        matched_list = [characters in errorchar for characters in hex]
        string_contains_chars = any(matched_list)
        if string_contains_chars == True:
            window['Error_msg'].update("You have entered an Incorrect Hex")
        else:
            window['Error_msg'].update("")
            Decimal_value=  int(values["enter_your_hexadecimal_number"],16)
            Binary_value= bin(int(values["enter_your_hexadecimal_number"],16))[2:].zfill(8)
            




            window['Decimal_value'].update(Decimal_value)
            window['Binary_value'].update(Binary_value)
       
        
  

window.close()


# In[ ]:





# In[ ]:





# In[ ]:




