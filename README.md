# VK-бот на vkbottle

Пример бота на [vkbottle](https://github.com/vkbottle/vkbottle) (Python), которого можно развернуть в **Timeweb Cloud Apps**.

Бот работает через long polling и отвечает на простые команды:

| Команда | Ответ |
| --- | --- |
| `/start` | приветствие |
| `/help` | список команд |
| `/ping` | `pong` |
| любой текст | повторяет сообщение |

:rocket: [Создать свой Apps](https://timeweb.cloud/my/apps/create)

:books: [Документация Timeweb Cloud Apps](https://timeweb.cloud/docs/apps)

## Параметры деплоя

Выберите язык **Python**, фреймворк **vkbottle** и тип приложения **backend**.

| Параметр | Значение |
| --- | --- |
| Фреймворк | vkbottle |
| Версия Python | 3.13 |
| Тип приложения | `backend` |
| Команда сборки | `pip install --upgrade -r requirements.txt` |
| Команда запуска | `python3 main.py` |

## Переменные окружения

| Переменная | Описание |
| --- | --- |
| `BOT_TOKEN` | ключ доступа сообщества ВКонтакте (Управление → Работа с API) с правом на сообщения; в настройках Long Poll API включите событие «Входящее сообщение» |

## <a name="dev"></a>Локальный запуск проекта

```bash
# установка зависимостей
pip3 install -r requirements.txt

# запуск бота
BOT_TOKEN=<токен> python3 main.py
```
