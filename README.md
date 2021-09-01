### Features

- Automatic Send Message 
- Add Picture  to Message You Want
- Send Message at Specific Time
- Choose View Once Option if You Want

![](https://camo.githubusercontent.com/38f5db5524ba43e7262dfbca1f7d3631ba127fb1596785dfd707d5fc671821c9/687474703a2f2f466f7254686542616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667) 

Import Whatsapp 
```python
from whatsapp import Whatsapp
```

Create Whatsapp Object
```python
wp = Whatsapp(data='data.xlsx') 
```

Send text to a specific number
```python
wp.send_text(phone_number,text)
```

Send Picture and/or Text to a specific number. You can choose view once .
```python
wp.send_picture(phone_number,path_pic,text,view_once)
```

Automatic 
```python
wp.auto()
```


# Note

Prepare a data which contains 
- Phone Number(required)
- Text(if you want)
- Path of picture(if you want)
- View Once(if its not 0 , it chooses view once)
- Date(if you want, examle date is 01-09-2021-19-46-00)

# Warning 

You need to chooses at least one from  text or path of picture. If you dont choose , row deletes.

Default file name is data.xlsx but you can change. You can use csv or json too .

Pay attention to the order : Phone Numbers - Text - Path of Pic - View Once - Date

If you want , you can leave blank columns at the row .

Don't move the mouse while program working.

Phone number format is like this : 90507XXXXXXX
