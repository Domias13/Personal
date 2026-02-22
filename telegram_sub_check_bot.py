import logging
import os
from typing import Optional

from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ChatMemberStatus
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
ACCESS_LINK = os.getenv("ACCESS_LINK")


def _validate_settings() -> None:
    missing = [
        name
        for name, value in {
            "BOT_TOKEN": BOT_TOKEN,
            "CHANNEL_USERNAME": CHANNEL_USERNAME,
            "ACCESS_LINK": ACCESS_LINK,
        }.items()
        if not value
    ]

    if missing:
        raise RuntimeError(
            "Не заданы обязательные переменные окружения: " + ", ".join(missing)
        )


async def _is_user_subscribed(
    user_id: int, context: ContextTypes.DEFAULT_TYPE
) -> Optional[bool]:
    """
    Возвращает:
      - True, если пользователь состоит в канале;
      - False, если не состоит;
      - None, если не удалось проверить (например, нет прав у бота).
    """

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in {
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        }
    except Exception as exc:  # noqa: BLE001
        logger.warning("Не удалось проверить подписку: %s", exc)
        return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not update.message:
        return

    subscribed = await _is_user_subscribed(user.id, context)

    if subscribed is True:
        await update.message.reply_text(
            f"✅ Спасибо за подписку! Вот ваша ссылка:\n{ACCESS_LINK}"
        )
        return

    channel_url = (
        f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}"
        if CHANNEL_USERNAME.startswith("@")
        else f"https://t.me/{CHANNEL_USERNAME}"
    )

    if subscribed is False:
        await update.message.reply_text(
            "❌ Чтобы получить ссылку, подпишитесь на канал и отправьте /start снова.\n"
            f"Канал: {channel_url}"
        )
        return

    await update.message.reply_text(
        "⚠️ Сейчас не удалось проверить подписку.\n"
        "Убедитесь, что бот добавлен в канал как администратор с правом просмотра участников, "
        "и попробуйте снова."
    )


async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    await update.message.reply_text(
        "Команды:\n"
        "/start — проверить подписку и получить ссылку.\n"
        "/help — показать это сообщение."
    )


def main() -> None:
    _validate_settings()

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()
