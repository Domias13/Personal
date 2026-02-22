# Telegram-бот: проверка подписки на канал и выдача ссылки

Этот бот делает ровно 2 вещи:
1. Проверяет, подписан ли пользователь на ваш канал.
2. Выдаёт ссылку (`ACCESS_LINK`) только подписанным.

Если пользователь не подписан, бот отправляет сообщение с просьбой подписаться и снова нажать `/start`.

---

## Что нужно заранее

- Аккаунт Telegram.
- Ваш канал в Telegram.
- Установленный Python 3.10+.
- Доступ к командной строке (Cmd / PowerShell / Terminal).

Проверка Python:

```bash
python --version
```

Если команда не сработала, попробуйте:

```bash
py --version
```

---

## Шаг 1. Создать бота через BotFather

1. Откройте Telegram и найдите `@BotFather`.
2. Отправьте команду `/newbot`.
3. Задайте имя и username бота (username должен заканчиваться на `bot`).
4. BotFather пришлёт токен, примерно такой:

```text
123456789:AAExampleToken...
```

Сохраните токен — это значение `BOT_TOKEN`.

---

## Шаг 2. Подготовить канал

1. У вашего канала должен быть username (например `@my_channel`).
   - Проверяется в настройках канала.
2. Добавьте бота в канал.
3. Назначьте боту роль администратора в канале.

Важно: без прав администратора бот обычно не сможет корректно проверять подписку.

---

## Шаг 3. Скачать/открыть проект

Если у вас уже есть папка проекта — просто перейдите в неё в командной строке.

Пример:

```bash
cd C:\Users\ВашеИмя\Desktop\Personal
```

Проверьте, что в папке есть файлы:
- `telegram_sub_check_bot.py`
- `requirements.txt`
- `.env.example`

---

## Шаг 4. Установить зависимости

Выполните в папке проекта:

```bash
pip install -r requirements.txt
```

Если `pip` не найден, попробуйте:

```bash
python -m pip install -r requirements.txt
```

---

## Шаг 5. Создать файл `.env` с настройками

Скопируйте шаблон:

### Windows (Cmd)
```bat
copy .env.example .env
```

### PowerShell / Linux / macOS
```bash
cp .env.example .env
```

Откройте `.env` в любом текстовом редакторе и заполните:

```env
BOT_TOKEN=123456789:ВАШ_ТОКЕН_ОТ_BOTFATHER
CHANNEL_USERNAME=@your_channel
ACCESS_LINK=https://example.com/private-link
```

Где:
- `BOT_TOKEN` — токен из BotFather.
- `CHANNEL_USERNAME` — username канала (с `@` или без).
- `ACCESS_LINK` — ссылка, которую хотите выдавать подписанным.

---

## Шаг 6. Запуск бота

Запуск:

```bash
python telegram_sub_check_bot.py
```

Если всё хорошо, бот начнёт работать в режиме polling (команда будет «висеть» — это нормально).

Остановка бота:
- Нажмите `Ctrl + C` в окне командной строки.

---

## Шаг 7. Проверка работы

1. Откройте вашего бота в Telegram.
2. Нажмите `/start`.
3. Сценарии:
   - **Вы подписаны** → бот отправит `ACCESS_LINK`.
   - **Не подписаны** → бот предложит подписаться на канал и повторить `/start`.

---

## Частые проблемы и решения

### 1) Ошибка «Не заданы обязательные переменные окружения ...»
Значит не заполнен `.env` или файл лежит не в той папке.

Проверьте:
- файл называется именно `.env`;
- он находится рядом с `telegram_sub_check_bot.py`;
- все 3 переменные заполнены.

### 2) Бот не проверяет подписку
Проверьте:
- бот добавлен в **тот же канал**;
- бот назначен администратором;
- `CHANNEL_USERNAME` указан верно.

### 3) `pip` / `python` не найден
Попробуйте альтернативы:

```bash
py -m pip install -r requirements.txt
py telegram_sub_check_bot.py
```

### 4) Неправильный канал в ссылке
Убедитесь, что `CHANNEL_USERNAME` совпадает с username канала в Telegram.

---


## Готовый список команд для Windows CMD (ваш путь: `d:\pcb\`)

Скопируйте и выполните команды по очереди в **Командной строке (cmd.exe)**:

```bat
D:
cd "d:\pcb\"
python --version
pip --version
pip install -r requirements.txt
copy /Y .env.example .env
notepad .env
python telegram_sub_check_bot.py
```

После команды `notepad .env` вставьте и сохраните (заменив значения на свои):

```env
BOT_TOKEN=123456789:ВАШ_ТОКЕН_ОТ_BOTFATHER
CHANNEL_USERNAME=@your_channel
ACCESS_LINK=https://example.com/private-link
```

Если хотите обойтись **без блокнота**, можно создать `.env` сразу командами:

```bat
(
  echo BOT_TOKEN=123456789:ВАШ_ТОКЕН_ОТ_BOTFATHER
  echo CHANNEL_USERNAME=@your_channel
  echo ACCESS_LINK=https://example.com/private-link
) > .env
```

Если `pip` не найден, используйте:

```bat
python -m pip install -r requirements.txt
```

Если `python` не найден, попробуйте:

```bat
py -m pip install -r requirements.txt
py telegram_sub_check_bot.py
```

## Команды бота

- `/start` — проверить подписку и получить ссылку.
- `/help` — краткая справка.
