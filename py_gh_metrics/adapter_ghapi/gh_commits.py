from ghapi.all import GhApi

# api = GhApi(owner='tripattern', repo='py_gh_metrics')

class GhCommits():
    def __init__(self):
        self.gh_api = GhApi()

    def get_commits_list(self):
        # repos.list_commits(owner, repo, sha, path, author, since, until, per_page, page):
        # commits = self.gh_api.repos.list_commits(owner='tripattern', repo='py_gh_metrics', since='2021-01-01')
        return self.gh_api.repos.list_commits(owner='mklose', repo='intern', since='2020-01-01')
        # print(commits_list[0])
    def get_names_of_commits(self, cl):
        names_commits = []
        for i in cl:
            names_commits = names_commits + [i.commit.author.name]
        print(names_commits)
        return names_commits

    def get_unique_names_in_list(self, names):
        unique_names = set(names)
        list_unique_names = list(unique_names)
        print(list_unique_names)
        return list_unique_names

    def commits_pp_per_day(self):
        commits_list = self.get_commits_list()
        nc = self.get_names_of_commits(commits_list)
        no_dups = self.get_unique_names_in_list(nc)

        # make unique
        commits_per_day = []
        for i in no_dups:
            commits_per_day = commits_per_day + [{i: nc.count(i)}]

        print(commits_per_day)


my_gh_commits_obj = GhCommits()
my_gh_commits_obj.commits_pp_per_day()
