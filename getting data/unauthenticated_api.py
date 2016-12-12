import requests, json
from dateutil.parser import parse
from collections import Counter

endpoint = "https://api.github.com/users/rrosatti/repos"

repos = json.loads(requests.get(endpoint).text)

# Getting the data info we can figure out which months and days the user is most likely to create a repository
dates = [parse(repo['created_at']) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

# Getting the language of the last # repositories (in this case, the last 10 repositories)
last_repos =  sorted(repos, key=lambda r: r['created_at'], reverse=True)[:10]
last_languages = [repo['language'] for repo in last_repos]

for date in dates:
	print date

for lang in last_languages:
	print lang