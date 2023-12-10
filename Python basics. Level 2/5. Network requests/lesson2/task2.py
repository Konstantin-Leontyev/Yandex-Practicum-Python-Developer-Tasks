import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)  # Выполните HTTP-запрос.

print(response.text)  # Напечатайте текст HTTP-ответа.
