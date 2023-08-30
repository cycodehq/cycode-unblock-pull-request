# Cycode Recovery Tool

![logo](https://e5s6t7j5.rocketcdn.me/wp-content/uploads/2020/10/Cycode_logo.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Configuration](#configuration-file)
- [Usage](#usage)
- [License](#license)

## Overview

Introducing the Cycode Recovery Tool, an internal disaster recovery solution exclusively designed to support Cycode's
customers. This invaluable tool steps in during times of a disaster, ensuring that your software development workflows
remain resilient even when faced with adversity.

## Features

* PR Unblocking: The Cycode Recovery Tool specializes in freeing up blocked Pull Requests (PRs), currently providing
  support exclusively for GitHub repositories. If your development process hits a snag with a blocked PR, this tool
  comes to the rescue, swiftly resolving the issue and getting your workflow back on track.

## Getting Started

### Configuration File

The tool expects a configuration file with SCM information named `config.json`. You can either add this config file when you build the docker image or mount the configuration file with `docker run -v`.

Sample config file:

```
[
  {
    "token": "<GitHub token with repo scope permission>",
    "provider": "GitHub",
    "repositories": [
      {
        "repository_name": "my_repository",
        "organization_name": "my_organization",
        "branch": "main"
      }
    ],
    "organizations": [
      {
        "organization_name": "my_organization"
      },
      {
        "organization_name": "my_second_organization"
      }
    ]
  }
]
```

* The token should have `repo` scope permissions.
* You can provide either `repositories` or `organizations`. You don't need both, but you need at least one of the two.
* In case `organizations` are provided, we will update all the organization's default branch in all repositories.
* You can provide multiple SCM configurations.

There are 2 options to run the Cycode recovery tool:
* Using our docker image
* Building your own docker image

### Pulling Cycode image
```
docker pull cycodehq/cycode_recovery_utils:latest
```

### Building an image locally
```
docker build -t cycode_recovery_tool . --no-cache
```

### Running the docker image
You will need to provide your configuration file
```
docker run -v /path/to/file/config.json:/app/config.json -ti cycode_recovery_tool
```

## Usage

1. Choose recovery action (currently only Release Block Pr)
![recovery action](./docs/recovery_action.png)
2. Choose provider (currently only GitHub)
3. Choose which status checks to release
![status_checks_release](./docs/status_checks_release.png)

## License

This project is licensed under the [MIT License](LICENSE).