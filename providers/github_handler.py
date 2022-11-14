import logging
from typing import List

from providers.provider_handler import ProviderHandler

logger = logging.getLogger(__name__)


class GithubHandler(ProviderHandler):
    def release_branch_protection(self, token, organization_name, repository_name, branch, contexts: List[str]):
        logger.info(f"Releasing branch protection on repository {repository_name}")
