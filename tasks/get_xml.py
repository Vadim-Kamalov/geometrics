# скрипт получает ggbBase64 и выдаёт в текущую директорию файл geogebra.xml
import base64
import os
from zipfile import ZipFile

# получение ggbBase64
with open("data.txt", "r") as file:
    ggbBase64 = file.read()

# декодирование base64
decoded = base64.b64decode(ggbBase64)

# сохраняем декодированную строку как zip-архив
with open("temp.zip", "wb") as file:
    file.write(decoded)

# получаем xml-файл и сохраняем его в текущей директории
with ZipFile("temp.zip", "r") as zipped_file:
    zipped_file.extract("geogebra.xml")
os.remove("temp.zip")