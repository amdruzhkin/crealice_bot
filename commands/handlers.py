from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def start_handler(message: Message):

    # user = await get_user_by_id(message.from_user.id)
    # if user is None:
    #     user = User()
    #     user.tg_id = message.from_user.id
    #     user.tg_username = message.from_user.username
    #     user.campaign = str(command.args)
    #     user.language = 'EN'
    #     await create_user(user)
    #
    # keyboard = get_start_menu_kb(user.language)

    await message.answer(text='Добро пожаловать в CREALICE! Мы предоставляем услуги 3D-Печати на территории черноморского побережья.')