import webbrowser
import time
import pyautogui as py
import pandas as pd
from datetime import datetime

class Whatsapp():
    def __init__(self,data='data.xlsx'):
        self.data=data 
        
    def read_data(self):
        """
        Reads the data and returns DataFrame
        """
        try:
            if '.xlsx' in self.data :
                df = pd.read_excel(self.data)
            elif '.csv' in self.data :
                df = pd.read_csv(self.data)
            elif '.json' in self.data :
                df = pd.read_json(self.data)
            
            return df 
        
        except Exception as e :
            print(f'An error occured while reading data . Error is :{e}')

    def prepare_data(self,df) :
            
        df = df.dropna(how= 'all') #if all columns is empty in a row , we remove it from df
            
        df = df.dropna(axis=0, subset=[df.columns[0]]) #if phone number is empty , deletes the row
            
        df = df.dropna(subset=[df.columns[1] , df.columns[2] ], thresh=1) #path of pic , or text must be.
                    
        df = df[df[df.columns[0]].str.contains("0123456789")!=False].reset_index(drop=True) 
        #if phone number is invalid , deletes the row
            
        df = df[df[df.columns[2]].str.contains(r'\\')!=False].reset_index(drop=True)
        #if path is invalid , deletes the row
        
        return df
              
    def send_text(self,phone_number,text) :
        """
        Sends text to a specific number .
        """
        try:
            url = f'https://api.whatsapp.com/send/?phone={phone_number}&text={text}&app_absent=0'
            
            webbrowser.open_new_tab(url)

            time.sleep(5)
            
            py.moveTo(700, 380)
            py.click() 

            time.sleep(2)

            py.moveTo(700, 430)
            py.click()

            time.sleep(10)

            py.press('enter') 
            
            time.sleep(3)
            
            py.hotkey('ctrl', 'w')   
        
        except Exception as e :
            print(f'An error occured while sending text at phone {phone_number} . Error is {e} . ')  
            py.hotkey('ctrl', 'w')
    
    def send_picture(self,phone_number,path_pic,text=0,view_once=0) :
        """
        Sends picture to a specific number
        """
        try:
            url = f'https://api.whatsapp.com/send/?phone={phone_number}&text&app_absent=0'
            
            webbrowser.open_new_tab(url)

            time.sleep(5)
            
            py.moveTo(700, 380)
            py.click() 

            time.sleep(2)

            py.moveTo(700, 430)
            py.click()

            time.sleep(10)
            
            py.moveTo(500, 700) # choosing
            py.click()

            py.moveTo(500, 620) #choosing pic
            py.click()
            
            time.sleep(2)
            
            py.write(path_pic)  # sending path of pic

            py.moveTo(500, 550)
            py.click()
            
            time.sleep(1)

            if view_once != 0 :
                py.moveTo(1200, 600) #view once
                py.click()
                time.sleep(2)  
                
            if text != 0 :              
                py.moveTo(650, 600) #sending  with text
                py.click()
                py.write(text)
                py.press("enter")
            else :
                py.press("enter") #sending directly(without text)
                
            time.sleep(3)
            
            py.hotkey('ctrl', 'w')
        
        except Exception as e:
            print(f'An error occured while sending picture at phone {phone_number} . Error is {e} . ')  
            py.hotkey('ctrl', 'w')

    def auto_with_view_once(self,df) :
        for phone_number , text , pic , view  in zip(df[df.columns[0]] , df[df.columns[1]] , df[df.columns[2]] , df[df.columns[3]]  ) :
            print(f'Sending Message :\nPhone:{phone_number}\nText:{text}\nPath:{pic} ')
            if isinstance(pic,float) : #any picture 
                self.send_text(phone_number,text)
                    
            elif isinstance(text,float) :  
                if view == 1 : 
                    self.send_picture(phone_number,pic,view_once=1)
                else :
                    self.send_picture(phone_number,pic)
                                                
            else :
                if view == 1 : 
                    self.send_picture(phone_number,pic,text,view_once=1)
                else :
                    self.send_picture(phone_number,pic,text)          

    def auto_without_view_once(self,df) :
        for phone_number , text , pic  in zip(df[df.columns[0]] , df[df.columns[1]] , df[df.columns[2]] ) :
            print(f'Sending Message :\nPhone:{phone_number}\nText:{text}\nPath:{pic} ')
            if isinstance(pic,float) : #any picture 
                self.send_text(phone_number,text)
                    
            elif isinstance(text,float) :     
                self.send_picture(phone_number,pic)
                        
            else :
                self.send_picture(phone_number,pic,text)        

    def auto(self) :
        try:
            df_1 = self.read_data() 
            
            df = self.prepare_data(df_1)
            
            columns = df.columns
                       
            if len(columns) == 3 : #phone number , text , path
                self.auto_without_view_once(df)
            
            elif len(columns) == 4 : #phone number , text , path , view once
                self.auto_with_view_once(df)
            
            elif len(columns) == 5 : #with date
                for phone_number , text , pic , view , date_1  in zip(df[df.columns[0]] , df[df.columns[1]] , df[df.columns[2]] , df[df.columns[3]] , df[df.columns[4]]   ) :
                    try:
                        now = datetime.now()
                        date = datetime.strptime(str(date_1),'%d-%m-%Y-%H-%M-%S')
                        difference = (now - date).seconds
                        if date > now :
                            difference = (date - now).seconds
                            if difference < 60 : 
                                s= {
                                        "phone" : phone_number ,
                                        "text" : text ,
                                        "pic" : pic ,
                                        "view" : view
                                    }
                                send_df = pd.DataFrame(data=s,index=[0])
                                self.auto_with_view_once(send_df)                    
                        
                    except Exception as e:
                        print(f'An error occurred. Please check date in data . Error is:{e} ')
                   

        except Exception as e :
            print(f'An error occurred . Error is {e}')            
  
