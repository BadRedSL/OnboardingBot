from aiogram.dispatcher.filters.state import StatesGroup, State


class StartDialogForm(StatesGroup):
    employee: State = State()
    full_name: State = State()

    admin: State = State()


class MainDialogForm(StatesGroup):
    main: State = State()


class EmployeesDialogForm(StatesGroup):
    employees: State = State()
    detail: State = State()


class ProductsDialogForm(StatesGroup):
    products: State = State()

    kids: State = State()

    junior: State = State()

    middle: State = State()

    senior: State = State()

    to_main: State = State()

    program: State = State()

    teachers: State = State()

    price: State = State()

    back: State = State()


class OfficialDutiesDialogForm(StatesGroup):
    official_duties: State = State()
