import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

API_TOKEN = '6971192609:AAHBxWItFDGsOMihFXiD51AjD0tTkfMOy6c'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Хочу задать свой вопрос')
    button2 = KeyboardButton('Как закупить? Регламент закупки?')
    button3 = KeyboardButton('Какую номенклатуру нужно купить?')
    button4 = KeyboardButton('Виды закупки')
    button5 = KeyboardButton('Правовая база')
    button6 = KeyboardButton('Организационные вопросы')
    markup.add(button1, button4)
    markup.add(button2)
    markup.add(button3)
    markup.add(button5, button6)

    # Отправка изображения и приветсвия
    with open('img/img.png', 'rb') as photo:
        await message.answer("Привет! Я Марк закупщик!\nЧем я могу вам помочь?", reply_markup=markup)
        await message.answer_photo(photo)


# Функция обработки вопроса с помощью искусственного интеллекта
async def ai(question: str):
    print('функция отработала и дает ответ!')
    answerAI = 'На данный момент я не владею такой информацией'
    answer = f"Вы задали вопрос: '{question}'.\nОтвет от искусственного интеллекта: {answerAI}"
    return answer


# Функция для отправки сообщения с новыми кнопками
async def send_message_with_buttons(message: types.Message, text: str, buttons: list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for button_text in buttons:
        markup.add(KeyboardButton(button_text))
    await message.answer(text, reply_markup=markup)


# Обработчики для каждой кнопоки
@dp.message_handler(lambda message: message.text == 'Как закупить? Регламент закупки?')
async def process_button1(message: types.Message):
    text = "Вы выбрали 'Как закупить? Регламент закупки?' Выберите следующий шаг:"
    buttons = ["Определится по типу Заказчика", "Определится по способу закупки", "По федеральному закону",
               "Хочу задать свой вопрос", "Главное меню"]
    await send_message_with_buttons(message, text, buttons)


# Обработчики для каждой кнопоки
@dp.message_handler(lambda message: message.text == 'Какую номенклатуру нужно купить?')
async def process_button2(message: types.Message):
    text = "Вы выбрали 'Какую номенклатуру нужно купить?' Выберите следующий шаг:"
    buttons = ["Товары", "Услуги", "Работы", "Хочу задать свой вопрос", "Главное меню"]
    await send_message_with_buttons(message, text, buttons)


# Обработчики для каждой кнопоки
@dp.message_handler(lambda message: message.text == 'Виды закупки')
async def process_button3(message: types.Message):
    text = "Вы выбрали Виды закупки' Выберите следующий шаг:"
    buttons = ["Конкурс", "Аукцион, редукцион", "Запрос предложений или котировок", "Хочу задать свой вопрос",
               "Главное меню"]
    await send_message_with_buttons(message, text, buttons)


# Обработчики для каждой кнопоки
@dp.message_handler(lambda message: message.text == 'Правовая база')
async def process_button4(message: types.Message):
    text = "Вы выбрали 'Правовая база' Выберите следующий шаг:"
    buttons = ["ФЗ 223", "ЕОМУ по АДД", "ЕОС3", "Хочу задать свой вопрос", "Главное меню"]
    await send_message_with_buttons(message, text, buttons)


# Обработчики для каждой кнопоки
@dp.message_handler(lambda message: message.text == 'Организационные вопросы')
async def process_button5(message: types.Message):
    text = "Вы выбрали 'Организационные вопросы' Выберите следующий шаг:"
    buttons = ["Договорная деятельность", "Закупочная комиссия", "Годовой план Закупок(ГПЗ)", "Хочу задать свой вопрос",
               "Главное меню"]
    await send_message_with_buttons(message, text, buttons)


@dp.message_handler(lambda message: message.text == 'Главное меню')
async def return_to_main_menu(message: types.Message):
    await start(message)


# Обработчик для 1-ой кнопки с вызовом функции AI
@dp.message_handler(lambda message: message.text == 'Хочу задать свой вопрос')
async def handle_other(message: types.Message):
    await message.answer('Введите ваш вопрос')


# обработчик для текстовых сообщений
@dp.message_handler(lambda message: message.text != 'Хочу задать свой вопрос')
async def handle_question(message: types.Message):
    # функция нейронки
    answer = await ai(message.text)
    await message.answer(answer)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
