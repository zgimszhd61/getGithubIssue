# getGithubIssue
## 使用方法
1. 将自己的access token填写到app.py之中.
2. 运行app.py
3. 运行结果如下截图所示.

<img width="589" alt="image" src="https://github.com/zgimszhd61/getGithubIssue/assets/114722053/474e3ab5-7860-4598-b8a9-a4e84bf043f1">



------

## 如何得到自己的personal access token
要生成GitHub个人访问令牌（Personal Access Token），请按照以下步骤操作：

### 步骤 1：登录GitHub
1. 打开GitHub网站（[github.com](https://github.com)），并使用你的GitHub账户登录。

### 步骤 2：进入设置页面
1. 在页面右上角，点击你的个人头像。
2. 从下拉菜单中选择“Settings”（设置）。

### 步骤 3：进入开发者设置
1. 在左侧边栏，向下滚动并点击“Developer settings”（开发者设置）。

### 步骤 4：生成新的个人访问令牌
1. 在左侧边栏，点击“Personal access tokens”（个人访问令牌）。
2. 点击“Generate new token”（生成新令牌）。

### 步骤 5：配置令牌
1. **Token name**：在“Token name”字段中输入令牌的名称，以便你以后识别其用途。
2. **Expiration**：选择令牌的过期时间。你可以选择默认的30天，也可以选择自定义的过期时间，甚至选择“无过期”。
3. **Scopes**：选择令牌的权限范围。根据你的需求选择适当的权限，例如：
   - `repo`：访问你的所有仓库。
   - `read:org`：读取组织信息。
   - `user`：读取用户信息。
   - 其他权限根据需要选择。

### 步骤 6：生成并保存令牌
1. 配置完成后，点击“Generate token”（生成令牌）。
2. GitHub会生成并显示你的个人访问令牌。**注意**：这个令牌只会显示一次，请务必复制并保存到安全的地方。

### 示例图示
以下是生成个人访问令牌的示意图：

生成个人访问令牌

### 使用个人访问令牌
在需要身份验证的地方（例如使用Git命令行推送代码时），使用你的GitHub用户名和生成的个人访问令牌作为密码。

### 参考资料
- [GitHub官方文档：管理个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)[1]
- [GeeksforGeeks：如何生成GitHub个人访问令牌](https://www.geeksforgeeks.org/how-to-generate-personal-access-token-in-github/)[3]

通过以上步骤，你可以成功生成并使用GitHub个人访问令牌来进行API调用或其他需要身份验证的操作。

Citations:
[1] https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[2] https://docs.catalyst.zoho.com/en/tutorials/githubbot/java/generate-personal-access-token/
[3] https://www.geeksforgeeks.org/how-to-generate-personal-access-token-in-github/
[4] https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
[5] https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
[6] https://www.youtube.com/watch?v=iLrywUfs7yU
[7] https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-create-a-GitHub-Personal-Access-Token-example
[8] https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-and-revoking-personal-access-tokens-in-your-organization
