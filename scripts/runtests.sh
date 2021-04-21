#!/bin/bash

(
cd ..
pytest ./py_gh_metrics/adapter_ghapi/gh_commits_test.py::test_it_should_get_unique_names_in_list -sv
)

