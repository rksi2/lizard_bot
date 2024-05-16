import os

from hammett.core import Application, Button
from hammett.core.constants import DEFAULT_STATE, SourcesTypes, RenderConfig
from hammett.core.screen import Screen
from hammett.core.mixins import StartMixin
from hammett.core.handlers import register_typing_handler
from hammett.core.handlers import register_button_handler
from disk import get_filenames



class HelloScreen(StartMixin, Screen):
    description = "Привет, это бот который собирает расписание, выбери дату."
    files = get_filenames()


    async def add_default_keyboard(self,update,_context):
        files = get_filenames()
        file_keyboard = []
        for file in files:
            button = Button(
                f'{file["name"]}'.replace('.xlsx',''),
                GetGroup,
                source_type=SourcesTypes.JUMP_SOURCE_TYPE,
            )
            file_keyboard.append([button])
            print(file_keyboard[0])

        return file_keyboard


class GetGroup(StartMixin, Screen):
    description = "Пришлите номер группы!"

    @register_typing_handler
    async def get_number(self, update, _context):
        nmbr = update.message.text


def main():
    name = 'Start_Screen'
    app = Application(
        name,
        entry_point=HelloScreen,
        states={
            DEFAULT_STATE: [HelloScreen, GetGroup],
        },
    )
    app.run()


if __name__ == "__main__":
    main()