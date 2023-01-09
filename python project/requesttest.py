import requests
import re

# from ast import Param
# from io import BytesIO
# from PIL import Image


# my_data = {"Name":"himanshu","E-mail":"himanshu@gmail.com"}
# r=requests.post("https://tryphp.w3schools.com/demo/demo_form_post.php", data=my_data)

re = requests.get("https://img1.hotstarext.com/image/upload/f_auto,t_web_m_1x/sources/r1/cms/prod/6574/666574-h")

f = open("myfile.html","w+")
f.write(re.text)


########################################################################
# re = requests.get("https://img1.hotstarext.com/image/upload/f_auto,t_web_m_1x/sources/r1/cms/prod/6574/666574-h")

# re = requests.get("https://freepngimg.com/thumb/tom_and_jerry/6-2-tom-and-jerry-picture.png")

# print("status code:", re.status_code)

# image = Image.open(BytesIO(re.content))

# print(image.size, image.format,image.mode)

# path = "./image1."+image.format

# try:
#     image.save(path, image.format)
# except IOError:
#     print("cannot save image.")



#########################################################################
# Param = {"q":"pizza"}
# r = requests.get("http://www.google.com/search", params=Param )

# print("status:", r.status_code)

# print(r.url)

# f = open("./page.html", "w+")
# f.write(r.text)