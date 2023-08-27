from typing import List, Optional

import pydantic


class OrganizationConfig(pydantic.BaseModel):
    organization_name: str


class RepositoryConfig(pydantic.BaseModel):
    repository_name: str
    organization_name: str
    branch: str


class ReleaseBlockPrConfig(pydantic.BaseModel):
    token: str
    provider: str
    repositories: Optional[List[RepositoryConfig]]
    organizations: Optional[List[OrganizationConfig]]
