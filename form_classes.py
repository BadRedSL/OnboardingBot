from aiogram.dispatcher.filters.state import StatesGroup, State


class StartDialogForm(StatesGroup):
    start: State = State()

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


class KnowledgeTestDialogForm(StatesGroup):
    knowledge_test: State = State()

    people_test: State = State()
