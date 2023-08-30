import os
from typing import Dict, List

import pydantic
from PyInquirer import prompt

from consts import providers, contexts, config_file
from logger import logger
from menus.menu_base import MenuBase
from menus.release_block_pr_menu import ReleaseBlockPrMenu
from release_block_pr_config import ReleaseBlockPrConfig

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


def validate_config_file():
    if not os.path.isfile(config_file):
        return f"Could not find '{config_file}' file in the directory {os.getcwd()}"
    try:
        parsed_configs = pydantic.parse_file_as(List[ReleaseBlockPrConfig], config_file)
        for parsed_config in parsed_configs:
            if len(parsed_config.organizations) == 0 and len(parsed_config.repositories) == 0:
                return f"Invalid input, need at least one repository or organization"
    except Exception as e:
        return f"Invalid input, not in the expected format {e}"
    return True


if __name__ == "__main__":
    validation_result = validate_config_file()
    if validation_result is not True:
        logger.error(validation_result)
    else:
        answer = prompt(main_menu)
        menu = menu_value_to_class.get(answer.get("menu"))
        if menu:
            menu.handle(answer)
            logger.info("Completed successfully")
        else:
            logger.error(f"Invalid menu {answer.get('menu')}")
