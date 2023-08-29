import os
from typing import List, Dict, Type

import pydantic

from consts import github, config_file
from logger import logger
from menus.menu_base import MenuBase
from providers.github_handler import GithubHandler
from release_block_pr_config import ReleaseBlockPrConfig, RepositoryConfig

release_block = "Release Blocked Pull Requests"


class ReleaseBlockPrMenu(MenuBase):
    handlers: Dict[str, Type[GithubHandler]] = {
        github: GithubHandler
    }

    def handle(self, answers):
        if answers.get("provider") in self.handlers:
            handler_class = self.handlers[answers["provider"]]
            release_block_pr_configs: List[ReleaseBlockPrConfig] = pydantic.parse_file_as(List[ReleaseBlockPrConfig],
                                                                                          config_file)
            for release_block_pr_config in release_block_pr_configs:
                handler = handler_class(release_block_pr_config.token)
                repositories: List[RepositoryConfig] = []
                if release_block_pr_config.repositories is not None:
                    repositories.extend(release_block_pr_config.repositories)

                # Get all organizations repositories
                organization_names = [organization.organization_name for organization
                                      in release_block_pr_config.organizations]
                repositories.extend(handler.get_organizations_repositories(organization_names))

                # Release branch protection from all repositories
                for repository in repositories:
                    handler.release_branch_protection(repository.organization_name, repository.repository_name,
                                                      repository.branch, answers["contexts"])
        else:
            logger.error(f"Invalid provider selected: {answers.get('provider')}")

    def get_menu(self):
        return release_block
