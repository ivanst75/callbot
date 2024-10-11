from aiogram_dialog.widgets.kbd import Start, Url
from aiogram_dialog import Dialog, LaunchMode, Window
from aiogram_dialog.widgets.text import Const
from . import states

main_dialog = Dialog(
    Window(
        Const("This is aiogram-dialog demo application"),
        Const("Use buttons below to see some options."),
        Start(
            text=Const("Далее..."),
            id="layout",
            state=states.Help.MAIN,
        ),
        state=states.Main.MAIN,
    ),
    launch_mode=LaunchMode.ROOT,
)


help_dialog = Dialog(
    Window(
        Const("Добавьте меня в чат и дайте права администратора."),
        Url(
            Const("Добавить в чат"),
            Const("https://t.me/call_albot?startgroup=groupadded"),
        ),
        state=states.Help.MAIN,
    ),
)
