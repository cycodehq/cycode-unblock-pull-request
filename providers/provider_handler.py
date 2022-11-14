from abc import ABC, abstractmethod
from typing import List


class ProviderHandler(ABC):
    @abstractmethod
    def release_branch_protection(self, token, organization_name, repository_name, branch, contexts: List[str]):
        pass
