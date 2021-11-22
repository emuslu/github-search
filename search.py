import validators
from github import Github
from svn.remote import RemoteClient
from git import Repo


g = Github("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")

def search_github(keywords):
    query = '+'.join(keywords) + '+language:python+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
    print(f'Found {result.totalCount} repo(s)')
    result = result[:999]
    for repo in result:
        print(f'{repo.clone_url}, {repo.stargazers_count} stars')
 
def download_folder(url):
    Repo.clone_from(url, "C:/Users/HP-PC/Desktop/Emre/githubsearch")

if __name__ == '__main__':
    #keywords = input('Enter keyword(s)[e.g python, malware, ransomware...]: ')
    #keywords = [keyword.strip() for keyword in keywords.split(',')]
    #search_github(keywords)
    url = input('Enter folder url: ')
    if not validators.url(url):
        print('Invalid url')
    else:
        download_folder(url)
