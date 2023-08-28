# Cycode Recovery Tool

![logo](https://e5s6t7j5.rocketcdn.me/wp-content/uploads/2020/10/Cycode_logo.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
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

1. Clone this repository
2. Build your local docker image

```

```

## Usage

1. Choose recovery action (currently only Release Block Pr) ![recovery action](./docs/recovery_action.png)
2. Provide path for the configuration file (or use our default config.json file)
3. Choose provider (currently only Github)
4. Choose which status checks to release ![status_checks_release](./docs/status_checks_release.png)

## configuration file

Input is as follows:

## License

This project is licensed under the MIT License.