# py_gh_metrics

## Dev Notes
* All test functions must start with the word 'test'

## Setup Dev Environment
* Setup Github Access Token
  * https://github.com/settings/tokens/new
* Export in your .bashrc or .zshrc
  * Reference: https://ghapi.fast.ai/
```
export GITHUB_TOKEN=xxx
```
* Setup Python dependencies
```
pipenv install
pipenv install --dev
```

## Run Tests
```
pytest
```
