# cycode_recovery_utils

This script will be responsible for various recovery utils. currently supports

- Release blocked pr's
    - github

## installation

`pip install -r requirements.txt`

## usage

`python3 main.py`

- choose recovery action:
- Release Block Pr: provide path for the configuration file
  ![recovery action](./docs/recovery_action.png)
- Release Block Pr: choose provider
- Release Block Pr: choose which status checks to release
  ![status_checks_release](./docs/status_checks_release.png)

## configuration file

Input is as follows:

```[
  {
    "token": "token",
    "provider": "github",
    "repositories": [
      {
        "repository_name": "ilan-repo4",
        "organization_name": "firecorp",
        "branch": "main"
      }
    ]
  }
]