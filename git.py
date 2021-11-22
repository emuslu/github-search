from github import Github

g = Github("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")

def search_github(keywords):
    query = '+'.join(keywords) + '+language:python+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
 
    print(f'Found {result.totalCount} repo(s)')
 
    for repo in result:
        print(f'{repo.clone_url}, {repo.stargazers_count} stars')
 
 
if __name__ == '__main__':
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    search_github(keywords)
 
