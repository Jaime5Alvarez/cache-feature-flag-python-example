# Cache Feature Flag Python Example

This project is an example implementation of feature flags with Redis caching using Python, with Ruff for code quality control and uv for package management.

## Description

This project demonstrates how to implement a feature flag system with PostHog as a provider, adding a Redis caching layer to improve performance and reduce calls to the external API.

## Requirements

- Python 3.12 or higher
- Redis
- PostHog account with an API key
- Ruff (for linting and formatting)
- uv (for package management)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Jaime5Alvarez/cache-feature-flag-python-example.git
cd cache-feature-flag-python-example
```

2. Install uv if you don't have it yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Install dependencies with uv and create a virtual environment:

```bash
uv sync
```

4. Copy the .env.example file to .env and configure your credentials:

```bash
cp .env.example .env
```

5. Edit the .env file with your PostHog API key and Redis configuration.

6. Run the example:

```bash
uv run main.py
```