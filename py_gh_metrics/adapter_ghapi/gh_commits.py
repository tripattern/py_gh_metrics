from ghapi.all import GhApi

# api = GhApi(owner='tripattern', repo='py_gh_metrics')

class GhCommits():
    def __init__(self):
        self.gh_api = GhApi()

    def commits_pp_per_day(self):
        # repos.list_commits(owner, repo, sha, path, author, since, until, per_page, page):
        commits = self.gh_api.repos.list_commits(owner='tripattern', repo='py_gh_metrics', since='2021-01-01')
        commits_per_day = []
        for commit in commits:
            print (commit.author.login)
            commits_per_day = commits_per_day + [(commit.author.login,1)]
        print (commits_per_day)

my_gh_commits_obj = GhCommits()
my_gh_commits_obj.commits_pp_per_day()