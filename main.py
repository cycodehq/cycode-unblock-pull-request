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
        'type': 'list',
        'name': 'menu',
        'message': 'What do you want to do?',
        'choices': [menu for menu in menu_value_to_class.keys()],

    },
    {
        'type': 'input',
        'name': 'config_file',
        "message": "Please provide a configuration file",
        "default": config_file,
        'validate': release_block_pr_menu.validate_config_file,
        "when": release_block_pr_menu.menu_chosen
    },
    {
        'type': 'list',
        'name': 'provider',
        "message": "Which provider?",
        "choices": providers,
        "when": release_block_pr_menu.menu_chosen,
    },
    {
        'type': 'checkbox',
        'name': 'contexts',
        "message": "Which contexts?",
        "choices": [{"name": context} for context in contexts],
        "when": release_block_pr_menu.menu_chosen
    }
]

if __name__ == '__main__':
    answer = prompt(main_menu)
    menu = menu_value_to_class.get(answer.get('menu'))
    if menu:
        menu.handle(answer)
        logger.info("Completed successfully")
    else:
        logger.error(f"invalid menu {answer.get('menu')}")

