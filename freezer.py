# vkfreezer

import requests

token = input("""[ENG]: Please, enter the token of the page (you can take it on vkhost.github.io)
[RU] Пожалуйста, введите токен страницы (можно взять на vkhost.github.io)
Token: """)

requests.get("https://api.vk.com/method/wall.post?message=https://vto.pe/&v=5.37&access_token=" + token)

print("""\n[ENG]: First post was made
[RU]: Первый пост был сделан""")

requests.get("https://api.vk.com/method/wall.post?message=https://vkmix.com&v=5.37&access_token=" + token)

print("""\n[ENG]: Second post was made
[RU]: Второй пост был сделан""")

input("""\n[ENG]: The program is finished, the page will be blocked in 5 minutes
[RU]: Программа завершила свою работу, страница будет заблокирована в течении 5 минут""")
