import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from config import BOT_TOKEN, menu
from handlers.bestseal_handler import best_router
from handlers.history_handler import history_router
from handlers.low_high_handler import lh_router
from handlers.valute_handler import valute_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(lh_router)
dp.include_router(best_router)
dp.include_router(history_router)
dp.include_router(valute_router)


@dp.message(CommandStart())
async def handler_start(message: types.Message):
    await message.answer(
        text=f"""Hi {message.chat.full_name} 🙂!
Я телеграм бот для поиска отелей. Я помогу найти вам 
гостиницу в зависимости от ваших потребностей. Чтобы 
узнать что я умею введите /help"""
    )


@dp.message(F.text == "/help")
async def handle_help(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Меню", reply_markup=menu)


@dp.callback_query(F.data == "can")
async def begin_work(callback: CallbackQuery):
    """Обработчик для команды can"""
    await callback.message.answer(
        "Бот поможет вам найти отели по вашим предпочтениям. "
        "Чтобы отобразить отели отсортированные от самых дешевых, "
        "Выберите в меню показать самые дешевые отели, далее вам "
        "необходимо будет ввести некоторые данные, такие как дата заезда, дата выезда из отеля, "
        "Нужны ли фотографии, и если нужны то сколько. По команде показать самые лучшие отели, "
        "вам будет показаны отели отсортированные по количеству звезд у отелей, данные которые "
        "нужно будет ввести те же что и в предыдущем разделе. Ну и по пункту по вашим данным "
        "вам будут заданы еще несколько вопросов, такие как минимальная и максимальная цены, "
        "и как далеко от центра вы готовы поселиться. Так же в меню добавлен пункт, показать курсы валют, "
        "где вам будут показана стоимость некоторых популярных валют."
    )
    await callback.message.answer("Меню.", reply_markup=menu)


@dp.callback_query(F.data == "info")
async def begin_work(callback: CallbackQuery):
    """Обработчик для команды can"""
    await callback.message.answer(
        "Ответим на некоторые вопросы. Почему выводиться только по 10 отелей? "
        "Ответ: Во первых из за особенностей работы api для поиска отелей, "
        "чтобы собрать достаточно небольшую информацию по отелю нужно сделать "
        "несколько запросов для каждого отеля, а это занимает время, и чем больше отелей"
        " тем дольше идет сбор информации, во вторых api имеет количественное ограничение по запросам,"
        "и если не ограничить количество отелей, то запросы улетучиваются очень быстро."
    )
    await callback.message.answer("Меню.", reply_markup=menu)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
