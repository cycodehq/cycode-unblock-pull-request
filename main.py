import os
from typing import Dict

from PyInquirer import prompt

from consts import providers, contexts, config_file
from logger import logger
from menus.menu_base import MenuBase
from menus.release_block_pr_menu import ReleaseBlockPrMenu

release_block_pr_menu = ReleaseBlockPrMenu()
menus = [release_block_pr_menu]
menu_value_to_class: Dict[str, MenuBase] = {menu.get_menu(): menu for menu in menus}

main_menu = [
    {
        "type": "list",
        "name": "menu",
        "message": "What would you like to do?",
        "choices": [menu for menu in menu_value_to_class.keys()],

    },
    {
        "type": "list",
        "name": "provider",
        "message": "Which SCM provider?",
        "choices": providers,
        "when": release_block_pr_menu.menu_chosen,
    },
    {
        "type": "checkbox",
        "name": "contexts",
        "message": "Which status checks?",
        "choices": [{"name": context} for context in contexts],
        "when": release_block_pr_menu.menu_chosen
    }
]

if not os.path.exists(config_file):
    logger.error("Could not find 'config.json' file in the root directory")
else:
    answer = prompt(main_menu)
    menu = menu_value_to_class.get(answer.get("menu"))
    if menu:
        menu.handle(answer)
        logger.info("Completed successfully")
    else:
        logger.error(f"invalid menu {answer.get('menu')}")
