import os

import dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import BotCommand

from form_classes import *
from keyboards import *

dotenv.load_dotenv(dotenv.find_dotenv())


class OnboardBot:
    __bot: Bot = Bot(token=os.getenv('TOKEN'))
    __storage: MemoryStorage = MemoryStorage()
    __dp: Dispatcher = Dispatcher(__bot, storage=__storage)

    __product_category: str = CompanyProductsKeyboard.buttons["btn_kids"]

    @classmethod
    def get_dp(cls) -> Dispatcher:
        return cls.__dp

    """
    Блок стартового диалога
    """

    @staticmethod
    @__dp.message_handler(commands=["start"])
    async def cmd_start(message: types.Message):
        # Что-то происходит
        if True:
            await StartDialogForm.employee.set()
            await message.reply("Укажите свое ФИО")
        elif False:
            await StartDialogForm.admin.set()
            await message.reply("Введите пароль")

    @staticmethod
    @__dp.message_handler(Text, state=StartDialogForm.employee)
    async def process_full_name(message: types.Message, state: FSMContext):
        # Что-то происходит
        if True:
            await state.finish()
            await MainDialogForm.main.set()
            await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)
        elif False:
            await message.reply("Повторите ввод")

    """
    Блок "Об офисе"
    """

    @staticmethod
    @__dp.message_handler(Text(equals=MainKeyboard.buttons["btn_about_office"], ignore_case=True),
                          state=MainDialogForm.main)
    async def process_about_office(message: types.Message, state: FSMContext):
        await message.answer("Выберите раздел", reply_markup=AboutOfficeKeyboard.about_office_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=AboutOfficeKeyboard.buttons["btn_office_video"], ignore_case=True),
                          state=MainDialogForm.main)
    async def process_office_video(message: types.Message, state: FSMContext):
        # выводим видео офиса
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=AboutOfficeKeyboard.buttons["btn_floor_plan"], ignore_case=True),
                          state=MainDialogForm.main)
    async def process_floor_plan(message: types.Message, state: FSMContext):
        # выводим план офиса
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    """
    Блок "Сотрудники"
    """

    @staticmethod
    @__dp.message_handler(Text(equals=MainKeyboard.buttons["btn_employees"], ignore_case=True),
                          state=MainDialogForm.main)
    async def process_employees(message: types.Message, state: FSMContext):
        await state.finish()
        await EmployeesDialogForm.employees.set()
        await message.answer("Выберите раздел", reply_markup=EmployeesKeyboard.employees_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=EmployeesKeyboard.buttons["btn_all_employees"], ignore_case=True),
                          state=EmployeesDialogForm.employees)
    async def process_employees_all(message: types.Message, state: FSMContext):
        # выводим список всех сотрудников
        await message.answer("Выберите раздел", reply_markup=CommonEmployeesKeyboard.common_employees_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=EmployeesKeyboard.buttons["btn_my_department"], ignore_case=True),
                          state=EmployeesDialogForm.employees)
    async def process_employees_all(message: types.Message, state: FSMContext):
        # выводим список сотрудников конкретного отдела
        await message.answer("Выберите раздел", reply_markup=CommonEmployeesKeyboard.common_employees_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=CommonEmployeesKeyboard.buttons["btn_detail"], ignore_case=True),
                          state=EmployeesDialogForm.employees)
    async def process_employees_detail(message: types.Message, state: FSMContext):
        await EmployeesDialogForm.detail.set()
        await message.answer("Введите имя интересующего сотрудника")

    @staticmethod
    @__dp.message_handler(Text, state=EmployeesDialogForm.detail)
    async def process_employees_detail_info(message: types.Message, state: FSMContext):
        # обрабатываем запрос, выводим информацию
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=CommonEmployeesKeyboard.buttons["btn_to_main"], ignore_case=True),
                          state=EmployeesDialogForm.employees)
    async def process_employees_to_main(message: types.Message, state: FSMContext):
        # обрабатываем запрос, выводим информацию
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    """
    Блок "О компании"
    """

    @staticmethod
    @__dp.message_handler(Text(equals=MainKeyboard.buttons["btn_about_company"], ignore_case=True),
                          state=MainDialogForm.main)
    async def process_about_company(message: types.Message, state: FSMContext):
        # информация о компании
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    """
    Блок "Продукты компании"
    """

    @staticmethod
    @__dp.message_handler(Text(equals=MainKeyboard.buttons["btn_company_products"], ignore_case=True),
                          state=MainDialogForm.main)
    async def process_products(message: types.Message, state: FSMContext):
        await state.finish()
        await ProductsDialogForm.products.set()
        await message.answer("Выберите раздел", reply_markup=CompanyProductsKeyboard.company_products_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=CompanyProductsKeyboard.buttons["btn_to_main"], ignore_case=True),
                          state=ProductsDialogForm.products)
    async def process_products_to_main(message: types.Message, state: FSMContext):
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=(CompanyProductsKeyboard.buttons["btn_kids"],
                                       CompanyProductsKeyboard.buttons["btn_junior"],
                                       CompanyProductsKeyboard.buttons["btn_middle"],
                                       CompanyProductsKeyboard.buttons["btn_senior"]), ignore_case=True),
                          state=ProductsDialogForm.products)
    async def process_products_category(message: types.Message, state: FSMContext):
        OnboardBot.__product_category = message.text.lower()
        await message.answer("Выберите раздел", reply_markup=CommonProductKeyboard.common_product_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=CommonProductKeyboard.buttons["btn_program"], ignore_case=True),
                          state=ProductsDialogForm.products)
    async def process_products_kids_program(message: types.Message, state: FSMContext):
        # выводим информацию о программе
        if OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_kids"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_junior"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_middle"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_senior"].lower():
            pass
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=CommonProductKeyboard.buttons["btn_teachers"], ignore_case=True),
                          state=ProductsDialogForm.products)
    async def process_products_kids_teachers(message: types.Message, state: FSMContext):
        # выводим информацию о преподавателях
        if OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_kids"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_junior"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_middle"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_senior"].lower():
            pass
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=CommonProductKeyboard.buttons["btn_price"], ignore_case=True),
                          state=ProductsDialogForm.products)
    async def process_products_kids_price(message: types.Message, state: FSMContext):
        # выводим информацию о ценах
        if OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_kids"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_junior"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_middle"].lower():
            pass
        elif OnboardBot.__product_category == CompanyProductsKeyboard.buttons["btn_senior"].lower():
            pass
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)

    @staticmethod
    @__dp.message_handler(Text(equals=CommonProductKeyboard.buttons["btn_back"], ignore_case=True),
                          state=ProductsDialogForm.products)
    async def process_products_kids_back(message: types.Message, state: FSMContext):
        # выводим информацию о ценах
        await ProductsDialogForm.products.set()
        await message.answer("Выберите раздел", reply_markup=CompanyProductsKeyboard.company_products_kb)

    """
    Блок "Продукты компании"
    """

    @staticmethod
    @__dp.message_handler(Text(equals=MainKeyboard.buttons["btn_official_duties"], ignore_case=True),
                          state=MainDialogForm.main)
    async def process_official_duties(message: types.Message, state: FSMContext):
        # выводим должностные обязанности
        await state.finish()
        await MainDialogForm.main.set()
        await message.answer("Что хотите узнать?", reply_markup=MainKeyboard.main_kb)