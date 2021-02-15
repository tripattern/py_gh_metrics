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
pytest ./py_gh_metrics/adapter_ghapi/gh_commits_test.py::test_it_should_get_unique_names_in_list -sv # run specific tests
```
