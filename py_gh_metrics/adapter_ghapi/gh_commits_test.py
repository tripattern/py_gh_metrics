from py_gh_metrics.adapter_ghapi import gh_commits

def test_it_should_get_unique_names_in_list():
   test_gh_commits = gh_commits.GhCommits()
   list_of_names_with_dups = ['Bob Smith', 'Martin Brown','Michael Mate','Bob Smith','Michael Mate','Michael Mate','Martin Brown']
   no_dups_name_list = test_gh_commits.get_unique_names_in_list(list_of_names_with_dups)
   assert set(no_dups_name_list) == set(['Bob Smith', 'Martin Brown', 'Michael Mate'])

