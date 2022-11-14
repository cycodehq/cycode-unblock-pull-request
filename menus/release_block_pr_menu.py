import os
from typing import List, Dict
import pydantic
import logging
from consts import github
from menus.menu_base import MenuBase
from providers.github_handler import GithubHandler
from providers.provider_handler import ProviderHandler
import PyInquirer
from release_block_pr_config import ReleaseBlockPrConfig

logger = logging.getLogger(__name__)

release_block = "Release Blocked PR's"


class ReleaseBlockPrMenu(MenuBase):
    handlers: Dict[str, ProviderHandler] = {
        github: GithubHandler()
    }

    def handle(self, answers):
        if answers.get("provider") in self.handlers:
            handler = self.handlers[answers["provider"]]
            repositories_to_unblock: List[ReleaseBlockPrConfig] = pydantic.parse_file_as(List[ReleaseBlockPrConfig],
                                                                                         answers["config_file"])
            for tokens_to_repositories in repositories_to_unblock:
                for repository in tokens_to_repositories.repositories:
                    handler.release_branch_protection(tokens_to_repositories.token, repository.organization_name,
                                                      repository.organization_name, repository.branch,
                                                      answers["contexts"])
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
