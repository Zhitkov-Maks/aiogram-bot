from aiogram import F
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.utils import markdown

from config import menu
from currency.currency import get_valute

valute_router = Router()


@valute_router.callback_query(F.data == "get_valute")
async def begin_work(callback: CallbackQuery):
    """Обработчик для команд get_valute"""
    get_val: tuple = await get_valute()
    text = ""
    for val in get_val:
        text = text + f"{val[1]}: {val[0]}₽\n"
    await callback.message.answer(
        text=f"{markdown.hbold(text)}",
        parse_mode=ParseMode.HTML
    )
    await callback.message.answer("Меню.", reply_markup=menu)
