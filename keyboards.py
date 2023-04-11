from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class JobTitleKeyboard:
    __btn_admin = KeyboardButton("Администратор")
    __btn_employee = KeyboardButton("Сотрудник")
    job_title_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_admin,
                                                                 __btn_employee)


class MainKeyboard:
    __btn_about_office = KeyboardButton("Об офисе")
    __btn_employees = KeyboardButton("Сотрудники")
    __btn_about_company = KeyboardButton("О компании")
    __btn_company_products = KeyboardButton("Продукты компании")
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_about_office,
                                                            __btn_employees,
                                                            __btn_about_company,
                                                            __btn_company_products)


class AboutOfficeKeyboard:
    __btn_office_video = KeyboardButton("Об офисе")
    __btn_floor_plan = KeyboardButton("План офиса")
    about_office_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_office_video,
                                                                    __btn_floor_plan)


class EmployeesKeyboard:
    __btn_all_employees = KeyboardButton("Все сотрудники")
    __btn_my_department = KeyboardButton("Мой отдел")
    employees_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_all_employees,
                                                                 __btn_my_department)


class CommonEmployeesKeyboard:
    __btn_detail = KeyboardButton("Подробнее о сотруднике")
    __btn_to_main = KeyboardButton("В главное меню")
    common_employees_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_detail,
                                                                        __btn_to_main)


class CompanyProductsKeyboard:
    __btn_kids = KeyboardButton("kids")
    __btn_junior = KeyboardButton("junior")
    __btn_middle = KeyboardButton("middle")
    __btn_senior = KeyboardButton("senior")
    __btn_to_main = KeyboardButton("В главное меню")
    company_products_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_kids,
                                                                        __btn_junior,
                                                                        __btn_middle,
                                                                        __btn_senior,
                                                                        __btn_to_main)


class CommonProductKeyboard:
    __btn_program = KeyboardButton("Программа")
    __btn_teachers = KeyboardButton("Преподаватели")
    __btn_price = KeyboardButton("Стоимость")
    __btn_back = KeyboardButton("Назад")
    common_product_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_program,
                                                                      __btn_teachers,
                                                                      __btn_price,
                                                                      __btn_back)
