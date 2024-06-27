import requests
from dotenv import load_dotenv
load_dotenv()
import os
# GitHub个人访问令牌
TOKEN = os.getenv('mmTOKEN')

# 目标仓库的所有者和仓库名
## https://github.com/alibaba/fastjson
OWNER = 'alibaba'
REPO = 'fastjson'

# GitHub API的基础URL
BASE_URL = f'https://api.github.com/repos/{OWNER}/{REPO}/issues'

# 请求头，包含身份验证信息
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_issues():
    issues = []
    page = 1
    while True:
        # 发送GET请求获取issue
        response = requests.get(BASE_URL, headers=headers, params={'page': page, 'per_page': 100})
        if response.status_code != 200:
            raise Exception(f"Error fetching issues: {response.status_code}")
        
        # 解析响应的JSON数据
        data = response.json()
        if not data:
            break
        
        issues.extend(data)
        page += 1
    
    return issues

def main():
    issues = get_issues()
    for issue in issues:
        print(f"Issue #{issue['number']}: {issue['title']}")
        print(f"URL: {issue['html_url']}")
        print(f"State: {issue['state']}")
        print(f"Created at: {issue['created_at']}")
        print(f"Updated at: {issue['updated_at']}")
        # print(f"Body: {issue['body']}\n")

if __name__ == "__main__":
    main()