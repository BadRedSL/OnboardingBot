from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class JobTitleKeyboard:
    buttons = {"btn_admin": "Администратор", "btn_employee": "Сотрудник"}
    __btn_admin = KeyboardButton(buttons["btn_admin"])
    __btn_employee = KeyboardButton(buttons["btn_employee"])
    job_title_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_employee)


class MainKeyboard:
    buttons = {"btn_about_office": "Об офисе", "btn_employees": "Сотрудники", "btn_about_company": "О компании",
               "btn_company_products": "Продукты компании", "btn_official_duties": "Должностные обязанности",
               "btn_test_knowledge": "Проверить свои знания", "btn_question": "Задать вопрос"}
    __btn_about_office = KeyboardButton(buttons["btn_about_office"])
    __btn_employees = KeyboardButton(buttons["btn_employees"])
    __btn_about_company = KeyboardButton(buttons["btn_about_company"])
    __btn_company_products = KeyboardButton(buttons["btn_company_products"])
    __btn_official_duties = KeyboardButton(buttons["btn_official_duties"])
    __btn_test_knowledge = KeyboardButton(buttons["btn_test_knowledge"])
    __btn_question = KeyboardButton(buttons["btn_question"])
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_about_office,
                                                            __btn_employees,
                                                            __btn_about_company,
                                                            __btn_company_products,
                                                            __btn_official_duties,
                                                            __btn_test_knowledge,
                                                            __btn_question)


class AboutOfficeKeyboard:
    buttons = {"btn_office_video": "Видео об офисе", "btn_floor_plan": "План офиса"}
    __btn_office_video = KeyboardButton(buttons["btn_office_video"])
    __btn_floor_plan = KeyboardButton(buttons["btn_floor_plan"])
    about_office_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_office_video,
                                                                    __btn_floor_plan)


class EmployeesKeyboard:
    buttons = {"btn_all_employees": "Все сотрудники", "btn_my_department": "Мой отдел"}
    __btn_all_employees = KeyboardButton(buttons["btn_all_employees"])
    __btn_my_department = KeyboardButton(buttons["btn_my_department"])
    employees_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_all_employees,
                                                                 __btn_my_department)


class CommonEmployeesKeyboard:
    buttons = {"btn_detail": "Подробнее о сотруднике", "btn_to_main": "В главное меню"}
    __btn_detail = KeyboardButton(buttons["btn_detail"])
    __btn_to_main = KeyboardButton(buttons["btn_to_main"])
    common_employees_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_detail,
                                                                        __btn_to_main)


class CompanyProductsKeyboard:
    buttons = {"btn_kids": "Kids", "btn_junior": "Junior", "btn_middle": "Middle",
               "btn_senior": "Senior", "btn_to_main": "В главное меню"}
    __btn_kids = KeyboardButton(buttons["btn_kids"])
    __btn_junior = KeyboardButton(buttons["btn_junior"])
    __btn_middle = KeyboardButton(buttons["btn_middle"])
    __btn_senior = KeyboardButton(buttons["btn_senior"])
    __btn_to_main = KeyboardButton(buttons["btn_to_main"])
    company_products_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_kids,
                                                                        __btn_junior,
                                                                        __btn_middle,
                                                                        __btn_to_main)


class CommonProductKeyboard:
    buttons = {"btn_program": "Программа", "btn_teachers": "Преподаватели", "btn_price": "Стоимость",
               "btn_back": "Назад"}
    __btn_program = KeyboardButton(buttons["btn_program"])
    __btn_teachers = KeyboardButton(buttons["btn_teachers"])
    __btn_price = KeyboardButton(buttons["btn_price"])
    __btn_back = KeyboardButton(buttons["btn_back"])
    common_product_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_program,
                                                                      __btn_teachers,
                                                                      __btn_price,
                                                                      __btn_back)


class KnowledgeTestKeyboard:
    buttons = {"btn_people_test": "Тема: сотрудники", "btn_duties_test": "Тема: обязанности"}
    __btn_people_test = KeyboardButton(buttons["btn_people_test"])
    __btn_duties_test = KeyboardButton(buttons["btn_duties_test"])
    knowledge_test_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(__btn_people_test)
