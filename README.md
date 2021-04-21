# py_gh_metrics

## Dev notes
* All test functions must start with the word 'test'

## Setup dev environment
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

## Run tests
```
pytest
pytest ./py_gh_metrics/adapter_ghapi/gh_commits_test.py::test_it_should_get_unique_names_in_list -sv # run specific tests
```

## Github API
* https://docs.github.com/en/rest

### List commits
* https://docs.github.com/en/rest/reference/repos#list-commits--parameters
```
curl  https://api.github.com/repos/tripattern/py_gh_metrics/commits
```

### Show specific commit
```
curl  https://api.github.com/repos/tripattern/py_gh_metrics/commits?sha={id}
```

### What does this parameter do?
```
&page={p}
```