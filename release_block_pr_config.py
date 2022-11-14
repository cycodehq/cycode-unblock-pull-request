from typing import List

import pydantic


class RepositoryConfig(pydantic.BaseModel):
    repository_name: str
    organization_name: str
    branch: str


class ReleaseBlockPrConfig(pydantic.BaseModel):
    token: str
    provider: str
    repositories: List[RepositoryConfig]
