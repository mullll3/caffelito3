import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keep_alive import keep_alive
# Инициализация бота
bot = Bot(token='6672188160:AAHL3sAEhzgJc2nIHISmv6aasqzsU8vuZMA')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

# Создаем общую кнопку "Назад ↩️"
back_button = types.KeyboardButton("Назад ↩️")
back_button2 = types.KeyboardButton("Назад")

# Создаем словарь для отслеживания текущей категории для каждого пользователя
@dp.message_handler(lambda message: message.text == "Назад ↩️", state="*")
async def handle_back(message: types.Message, state: FSMContext):
    # Отправляем главное меню
    await handle_menu(message)

@dp.message_handler(lambda message: message.text == "Назад", state="*")
async def handle_back2(message: types.Message, state: FSMContext):
    await state.finish()  # Reset the state to None
    await start(message, state)
# Список chat_id администраторов
admin_chat_ids = [6778318047, 5773503802, 141839443, 6715652826, 1692177453]

# Функция для проверки, имеет ли отправитель доступ к боту
def has_access(message: types.Message):
    return message.from_user.id in admin_chat_ids

# Обработчик команды /start
@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()  # Завершаем текущее состояние при старте
    if has_access(message):
        # Если есть доступ, отправляем приветственное сообщение и кнопки
        with open('assets/images/start/start.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="""<b>Привет !\nУ тебя возникли вопросы по работе ? Я БОТ-ПОМОЩНИК. Помогу найти нужный рецепт напитка и другие полезные видео.</b>🙌""",
                                 parse_mode='HTML', reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[
                    [types.KeyboardButton("Меню")],
                    [types.KeyboardButton("Свежеобжаренный кофе"), types.KeyboardButton("Рецепты сэндвичей")],
                    [types.KeyboardButton("Я бариста")]
                ],
                resize_keyboard=True
            ))
    else:
        # Если нет доступа, отправляем сообщение об отсутствии доступа
        await bot.send_message(chat_id=message.chat.id, text="<b>У вас нет доступа к этому боту. Обратитесь к администратору.</b>",parse_mode='HTML')

@dp.message_handler(lambda message: message.text == "Я бариста")
async def handle_barista_menu(message: types.Message):
   await message.answer('https://disk.yandex.ru/d/ayyLe_-Z04b6hw')



@dp.message_handler(lambda message: message.text == "Меню")
async def handle_menu(message: types.Message):
    with open('assets/images/start/start.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Выбери нужную тебе категорию !",
                             parse_mode='HTML', reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton("Кофе 🥤"), types.KeyboardButton("Напитки 🧋"), types.KeyboardButton("Чай 🍵")],
                [types.KeyboardButton("Заготовки 🔪"), types.KeyboardButton("Сезонное меню 🔥")],
                [back_button2]
            ],
            resize_keyboard=True
        ))

@dp.message_handler(lambda message: message.text == "Сезонное меню 🔥")
async def handle_sezon_menu(message: types.Message):
    await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("Мокко-Минт"),types.KeyboardButton("Латте Халва")],
            [types.KeyboardButton("Лавандовый Раф"),types.KeyboardButton("Латте Фисташка")],
            [back_button]
        ],
        resize_keyboard=True
    ))

@dp.message_handler(lambda message: message.text == "Мокко-Минт")
async def handle_moko_mint_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/q_myW75MyQM"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/mint.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text == "Латте Халва")
async def handle_xalva_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/egBGKZq9Y-s"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/xalva.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text == "Лавандовый Раф")
async def handle_lavanda_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/HbS9ERu0rfY"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/lavanda.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text == "Латте Фисташка")
async def handle_fistash_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/q6e2BPQ8h94"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/fistash.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# https://disk.yandex.ru/d/ayyLe_-Z04b6hw
@dp.message_handler(lambda message: message.text == "Заготовки 🔪")
async def handle_brew(message: types.Message):
    await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("Батч-Брю")], 
            [back_button]
        ],
        resize_keyboard=True
    ))

@dp.message_handler(lambda message: message.text == "Батч-Брю")
async def handle_brew_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/u7oLAs4ZAUU"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/brew.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

#...........................................................................................................
@dp.message_handler(lambda message: message.text == "Чай 🍵")
async def handle_tea(message: types.Message):
    await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("Матча🍵"),types.KeyboardButton('Чай с облепихой🍵')],
            [types.KeyboardButton("Чай с имбирём🍵"),types.KeyboardButton('Ягодный чай 🍵')],
            [back_button]
        ],
        resize_keyboard=True
    ))

@dp.message_handler(lambda message: message.text == "Матча🍵")
async def handle_matcha_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/JC7F-Q6JD3k"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/matcha.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text == "Чай с имбирём🍵")
async def handle_imbir_button(message: types.Message, state: FSMContext):
    youtube_link = "https://www.youtube.com/shorts/7Q7gi1zXUOI"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/imbir.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text == "Чай с облепихой🍵")
async def handle_oblepixa_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtube.com/shorts/rvIZ7n1rAR8?feature=share"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/oblipixa.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text == "Ягодный чай 🍵")
async def handle_yagoda_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtube.com/shorts/xrebdZZalcg"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/yagoda.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "Напитки 🧋")
async def handle_drink(message: types.Message):
    await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("Милк-Шейк🥤")],
            [types.KeyboardButton("Какао🥤"), types.KeyboardButton("Горячий шоколад🥤")],
            [back_button]
        ],
        resize_keyboard=True
    ))

@dp.message_handler(lambda message: message.text == "Милк-Шейк🥤")
async def handle_milk_sheyk_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtube.com/shorts/KVeAO3e___8?feature=share"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/mill_sheyk.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "Какао🥤")
async def handle_kakao_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/PexPz8E8hDY"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/kakao.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "Горячий шоколад🥤")
async def handle_hot_ch_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/n2WhuzwKQ5o"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/hot_ch.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# Обработчик команды /coffee
@dp.message_handler(lambda message: message.text == "Кофе 🥤")
async def handle_coffee(message: types.Message):
    await message.answer("Выберите категорию кофе:", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("☕️ Классический кофе")],
            [types.KeyboardButton("🍭 Сладкий кофе"), types.KeyboardButton("❄️ Холодный кофе")],
            [back_button]
        ],
        resize_keyboard=True
    ))

#...........................................................................................................
@dp.message_handler(lambda message: message.text == "❄️ Холодный кофе")
async def handle_winter_coffee(message: types.Message):
    await message.answer('Выберите вид Холодного кофе 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton('❄️Айс американо'), types.KeyboardButton('❄️Айс капучино')],
            [types.KeyboardButton('❄️Фрапетто'), types.KeyboardButton('❄️Бамбл')],
            [back_button]    
        ],
        resize_keyboard=True
    ))

@dp.message_handler(lambda message: message.text == "❄️Айс американо")
async def handle_w_amer_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/xtCYsZxckg8"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/w_amer.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "❄️Айс капучино")
async def handle_w_cap_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/CozXgD-qW-kC"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/w_cap.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "❄️Фрапетто")
async def handle_babl_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtube.com/shorts/NQaV7OdwDAw?feature=share"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/frapp.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "❄️Бамбл")
async def handle_frapp_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/ppuR8dzrLh4"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/babl.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)
#...........................................................................................................
@dp.message_handler(lambda message: message.text == "🍭 Сладкий кофе")
async def handle_coffee(message: types.Message):
    await message.answer("Выберите категорию кофе:", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("Раф Кофе ☕️"),types.KeyboardButton("Caffelito Coffee ☕️")],
            [back_button]
        ],
        resize_keyboard=True
    ))

@dp.message_handler(lambda message: message.text == "Раф Кофе ☕️")
async def handle_raf_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/20g32gpy-0Y?si=N7-bvqKX8lgFK9eX"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/raf.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "Caffelito Coffee ☕️")
async def handle_caffelito_coffee_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/vATxA08UDS4"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/caffelito.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

        
@dp.message_handler(lambda message: message.text == "☕️ Классический кофе")
async def handle_classic_coffee(message: types.Message):
    await message.answer("Выберите вид классического кофе:", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("☕️ Эспрессо"),  types.KeyboardButton("☕️ Американо")],
            [types.KeyboardButton("☕️ Латте"), types.KeyboardButton("☕️ Капучино")],
            [types.KeyboardButton("☕️ Флэт Уайт")],
            [back_button]
        ],
        resize_keyboard=True
    ))

@dp.message_handler(lambda message: message.text == "☕️ Эспрессо")
async def handle_espresso_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/px-REaMkO_s"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/espresso.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)
@dp.message_handler(lambda message: message.text == "☕️ Американо")
async def handle_amer_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/mvuG4avwINUK"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/amer.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "☕️ Латте")
async def handle_lat_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/2Y3vzCQ24VI"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/lat.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "☕️ Капучино")
async def handle_cap_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/adeaYdMmBUw?si=a3zP_jhpu4QHJXpm"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/cap.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == "☕️ Флэт Уайт")
async def handle_flet_button(message: types.Message, state: FSMContext):
    youtube_link = "https://youtu.be/F68bKcfT2Ig"
    inline_keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
    )
    with open('assets/images/start/photo/flet.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

keep_alive()
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

# import logging
# from aiogram.dispatcher import FSMContext
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

# # Инициализация бота
# bot = Bot(token='6563314132:AAHTY0d7bfk-FmR2aj9dnOGi9Dpt-iwE3Gg')
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
# logging.basicConfig(level=logging.INFO)

# # Создаем общую кнопку "Назад ↩️"
# back_button = types.KeyboardButton("Назад ↩️")
# back_button2 = types.KeyboardButton("Назад")


# # @dp.message_handler(lambda message: message.text in ["Назад ↩️"], state="*")
# # async def handle_back(message: types.Message, state: FSMContext):
# #     await state.finish()  # Reset the state to None
# #     await start(message, state)

# # Создаем словарь для отслеживания текущей категории для каждого пользователя
# @dp.message_handler(lambda message: message.text == "Назад ↩️", state="*")
# async def handle_back(message: types.Message, state: FSMContext):
#     # Отправляем главное меню
#     await state.finish()  # Reset the state to None
#     await handle_menu(message)

# @dp.message_handler(lambda message: message.text == "Назад", state="*")
# async def handle_back2(message: types.Message, state: FSMContext):
#     await state.finish()  # Reset the state to None
#     await start(message)
# # Список chat_id администраторов
# admin_chat_ids = [5378126237, 5773503802, 141839443, 6715652826, 1692177453]

# # Функция для проверки, имеет ли отправитель доступ к боту
# def has_access(message: types.Message):
#     return message.from_user.id in admin_chat_ids

# # Обработчик команды /start
# @dp.message_handler(commands=['start'], state='*')
# async def start(message: types.Message, state: FSMContext):
#     # await state.finish()  # Завершаем текущее состояние при старте
#     if has_access(message):
#         # Если есть доступ, отправляем приветственное сообщение и кнопки
#         with open('assets/images/start/start.jpg', 'rb') as photo:
#             await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="""<b>Привет !\nУ тебя возникли вопросы по работе ? Я БОТ-ПОМОЩНИК. Помогу найти нужный рецепт напитка и другие полезные видео.</b>🙌""",
#                                  parse_mode='HTML', reply_markup=types.ReplyKeyboardMarkup(
#                 keyboard=[
#                     [types.KeyboardButton("Меню")],
#                     [types.KeyboardButton("Свежеобжаренный кофе"), types.KeyboardButton("Рецепты сэндвичей")],
#                     [types.KeyboardButton("Я бариста")]
#                 ],
#                 resize_keyboard=True
#             ))
#     else:
#         # Если нет доступа, отправляем сообщение об отсутствии доступа
#         await bot.send_message(chat_id=message.chat.id, text="<b>У вас нет доступа к этому боту. Обратитесь к администратору.</b>",parse_mode='HTML')

# @dp.message_handler(lambda message: message.text == "Я бариста")
# async def handle_barista_menu(message: types.Message):
#    await message.answer('https://disk.yandex.ru/d/ayyLe_-Z04b6hw')



# @dp.message_handler(lambda message: message.text == "Меню")
# async def handle_menu(message: types.Message):
#     with open('assets/images/start/start.jpg', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Выбери нужную тебе категорию !",
#                              parse_mode='HTML', reply_markup=types.ReplyKeyboardMarkup(
#             keyboard=[
#                 [types.KeyboardButton("Кофе 🥤"), types.KeyboardButton("Напитки 🧋"), types.KeyboardButton("Чай 🍵")],
#                 [types.KeyboardButton("Заготовки 🔪"), types.KeyboardButton("Сезонное меню 🔥")],
#                 [back_button2]
#             ],
#             resize_keyboard=True
#         ))

# @dp.message_handler(lambda message: message.text == "Сезонное меню 🔥")
# async def handle_sezon_menu(message: types.Message):
#     await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton("Мокко-Минт"),types.KeyboardButton("Латте Халва")],
#             [types.KeyboardButton("Лавандовый Раф"),types.KeyboardButton("Латте Фисташка")],
#             [back_button]
#         ],
#         resize_keyboard=True
#     ))

# @dp.message_handler(lambda message: message.text == "Мокко-Минт")
# async def handle_moko_mint_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/q_myW75MyQM"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/mint.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# @dp.message_handler(lambda message: message.text == "Латте Халва")
# async def handle_xalva_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/egBGKZq9Y-s"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/xalva.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# @dp.message_handler(lambda message: message.text == "Лавандовый Раф")
# async def handle_lavanda_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/HbS9ERu0rfY"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/lavanda.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# @dp.message_handler(lambda message: message.text == "Латте Фисташка")
# async def handle_fistash_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/q6e2BPQ8h94"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/fistash.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# # https://disk.yandex.ru/d/ayyLe_-Z04b6hw
# @dp.message_handler(lambda message: message.text == "Заготовки 🔪")
# async def handle_brew(message: types.Message):
#     await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton("Батч-Брю")], 
#             [back_button]
#         ],
#         resize_keyboard=True
#     ))

# @dp.message_handler(lambda message: message.text == "Батч-Брю")
# async def handle_brew_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/u7oLAs4ZAUU"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/brew.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# #...........................................................................................................
# @dp.message_handler(lambda message: message.text == "Чай 🍵")
# async def handle_tea(message: types.Message):
#     await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton("Матча🍵"),types.KeyboardButton('Чай с облепихой🍵')],
#             [types.KeyboardButton("Чай с имбирём🍵"),types.KeyboardButton('Ягодный чай 🍵')],
#             [back_button]
#         ],
#         resize_keyboard=True
#     ))

# @dp.message_handler(lambda message: message.text == "Матча🍵")
# async def handle_matcha_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/JC7F-Q6JD3k"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/matcha.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# @dp.message_handler(lambda message: message.text == "Чай с имбирём🍵")
# async def handle_imbir_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://www.youtube.com/shorts/7Q7gi1zXUOI"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/imbir.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# @dp.message_handler(lambda message: message.text == "Чай с облепихой🍵")
# async def handle_oblepixa_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtube.com/shorts/rvIZ7n1rAR8?feature=share"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/oblipixa.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# @dp.message_handler(lambda message: message.text == "Ягодный чай 🍵")
# async def handle_yagoda_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtube.com/shorts/xrebdZZalcg"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/yagoda.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "Напитки 🧋")
# async def handle_drink(message: types.Message):
#     await message.answer('Выберите категорию Напитка 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton("Милк-Шейк🥤")],
#             [types.KeyboardButton("Какао🥤"), types.KeyboardButton("Горячий шоколад🥤")],
#             [back_button]
#         ],
#         resize_keyboard=True
#     ))

# @dp.message_handler(lambda message: message.text == "Милк-Шейк🥤")
# async def handle_milk_sheyk_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtube.com/shorts/KVeAO3e___8?feature=share"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/mill_sheyk.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "Какао🥤")
# async def handle_kakao_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/PexPz8E8hDY"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/kakao.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "Горячий шоколад🥤")
# async def handle_hot_ch_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/n2WhuzwKQ5o"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/hot_ch.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)


# # Обработчик команды /coffee
# @dp.message_handler(lambda message: message.text == "Кофе 🥤")
# async def handle_coffee(message: types.Message):
#     await message.answer("Выберите категорию кофе:", reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton("☕️ Классический кофе")],
#             [types.KeyboardButton("🍭 Сладкий кофе"), types.KeyboardButton("❄️ Холодный кофе")],
#             [back_button]
#         ],
#         resize_keyboard=True
#     ))

# #...........................................................................................................
# @dp.message_handler(lambda message: message.text == "❄️ Холодный кофе")
# async def handle_winter_coffee(message: types.Message):
#     await message.answer('Выберите вид Холодного кофе 👇🏻', reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton('❄️Айс американо'), types.KeyboardButton('❄️Айс капучино')],
#             [types.KeyboardButton('❄️Фрапетто'), types.KeyboardButton('❄️Бамбл')],
#             [back_button]    
#         ],
#         resize_keyboard=True
#     ))

# @dp.message_handler(lambda message: message.text == "❄️Айс американо")
# async def handle_w_amer_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/xtCYsZxckg8"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/w_amer.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "❄️Айс капучино")
# async def handle_w_cap_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/CozXgD-qW-kC"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/w_cap.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "❄️Фрапетто")
# async def handle_babl_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtube.com/shorts/NQaV7OdwDAw?feature=share"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/frapp.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "❄️Бамбл")
# async def handle_frapp_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/ppuR8dzrLh4"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/babl.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)
# #...........................................................................................................
# @dp.message_handler(lambda message: message.text == "🍭 Сладкий кофе")
# async def handle_coffee(message: types.Message):
#     await message.answer("Выберите категорию кофе:", reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton("Раф Кофе ☕️"),types.KeyboardButton("Caffelito Coffee ☕️")],
#             [back_button]
#         ],
#         resize_keyboard=True
#     ))

# @dp.message_handler(lambda message: message.text == "Раф Кофе ☕️")
# async def handle_raf_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/20g32gpy-0Y?si=N7-bvqKX8lgFK9eX"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/raf.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "Caffelito Coffee ☕️")
# async def handle_caffelito_coffee_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/vATxA08UDS4"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/caffelito.png', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

        
# @dp.message_handler(lambda message: message.text == "☕️ Классический кофе")
# async def handle_classic_coffee(message: types.Message):
#     await message.answer("Выберите вид классического кофе:", reply_markup=types.ReplyKeyboardMarkup(
#         keyboard=[
#             [types.KeyboardButton("☕️ Эспрессо"),  types.KeyboardButton("☕️ Американо")],
#             [types.KeyboardButton("☕️ Латте"), types.KeyboardButton("☕️ Капучино")],
#             [types.KeyboardButton("☕️ Флэт Уайт")],
#             [back_button]
#         ],
#         resize_keyboard=True
#     ))

# @dp.message_handler(lambda message: message.text == "☕️ Эспрессо")
# async def handle_espresso_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/px-REaMkO_s"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/espresso.jpg', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)
# @dp.message_handler(lambda message: message.text == "☕️ Американо")
# async def handle_amer_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/mvuG4avwINUK"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/amer.jpg', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "☕️ Латте")
# async def handle_lat_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/2Y3vzCQ24VI"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/lat.jpg', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "☕️ Капучино")
# async def handle_cap_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/adeaYdMmBUw?si=a3zP_jhpu4QHJXpm"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/cap.jpg', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# @dp.message_handler(lambda message: message.text == "☕️ Флэт Уайт")
# async def handle_flet_button(message: types.Message, state: FSMContext):
#     youtube_link = "https://youtu.be/F68bKcfT2Ig"
#     inline_keyboard = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Смотреть видео тут 👇🏻", url=youtube_link)
#     )
#     with open('assets/images/start/photo/flet.jpg', 'rb') as photo:
#         await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=inline_keyboard)

# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)





