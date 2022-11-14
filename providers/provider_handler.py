from abc import ABC, abstractmethod
from typing import List, Set


class ProviderHandler(ABC):

    def __init__(self, token):
        self.token = token

    @abstractmethod
    def release_branch_protection(self, organization_name, repository_name, branch, contexts: List[str]):
        pass
