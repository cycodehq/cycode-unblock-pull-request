import os
from typing import List, Dict, Type

import pydantic

from consts import github
from logger import logger
from menus.menu_base import MenuBase
from providers.github_handler import GithubHandler
from release_block_pr_config import ReleaseBlockPrConfig

release_block = "Release Blocked PR's"


class ReleaseBlockPrMenu(MenuBase):
    handlers: Dict[str, Type[GithubHandler]] = {
        github: GithubHandler
    }

    def handle(self, answers):
        if answers.get("provider") in self.handlers:
            handler_class = self.handlers[answers["provider"]]
            repositories_to_unblock: List[ReleaseBlockPrConfig] = pydantic.parse_file_as(List[ReleaseBlockPrConfig],
                                                                                         answers["config_file"])
            for tokens_to_repositories in repositories_to_unblock:
                handler = handler_class(tokens_to_repositories.token)
                for repository in tokens_to_repositories.repositories:
                    handler.release_branch_protection(repository.organization_name, repository.repository_name,
                                                      repository.branch, answers["contexts"])
        else:
            logger.error(f"Invalid provider selected: {answers.get('provider')}")

    def get_menu(self):
        return release_block

    @staticmethod
    def validate_config_file(config_file):
        if not os.path.isfile(config_file):
            return "File does not exist"
        try:
            pydantic.parse_file_as(List[ReleaseBlockPrConfig], config_file)
        except Exception as e:
            return f"Invalid input, not in the expected format {e}"
        return True
