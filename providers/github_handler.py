from typing import List

from github import Github

from logger import logger
from providers.provider_handler import ProviderHandler
from release_block_pr_config import RepositoryConfig


class GithubHandler(ProviderHandler):
    def __init__(self, token):
        super().__init__(token)
        self.github: Github = Github(token)

    def release_branch_protection(self, organization_name, repository_name, branch, contexts: List[str]):
        full_repo_name = f"{organization_name}/{repository_name}"
        if len(contexts) > 0:
            try:
                repo = self.github.get_repo(full_repo_name, lazy=True)
                branch = repo.get_branch(branch)
                required_status_checks = branch.get_required_status_checks()
                current_contexts = set(required_status_checks.contexts)
                logger.info(f"Current required status checks {current_contexts}")
                contexts_to_keep = current_contexts.difference(contexts)
                if contexts_to_keep != current_contexts:
                    logger.info(
                        f"Updating required status checks repository {full_repo_name} branch {branch.name} to contexts {contexts_to_keep}")
                    branch.edit_required_status_checks(contexts=list(contexts_to_keep))
                else:
                    logger.info(f"Skipping {full_repo_name} contexts to remove are not required")
            except:
                logger.exception(f"Failed to update required status checks on repository {full_repo_name}")

    def get_organization_repositories(self, organization_name):
        repository_configs = []
        try:
            organization = self.github.get_organization(organization_name)
            repositories = organization.get_repos()
            for repository in repositories:
                repository_config = RepositoryConfig(
                    repository_name=repository.name,
                    organization_name=organization_name,
                    branch=repository.default_branch  # Replace with the desired default branch
                )
                repository_configs.append(repository_config)
            return repository_configs
        except:
            logger.exception(f"Failed to get repositories for organization {organization_name}")
