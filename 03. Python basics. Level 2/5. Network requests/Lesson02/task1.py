import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)  # Выполните HTTP-запрос.

print(response.status_code)  # Напечатайте статус-код ответа.
