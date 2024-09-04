import os
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

def main():
    # 从环境变量中获取微信公众号的 AppID、AppSecret 和用户的 OpenID
    appid = os.getenv('WECHAT_APPID')
    appsecret = os.getenv('WECHAT_APPSECRET')
    openid = os.getenv('WECHAT_OPENID')

    # 从环境变量中获取 GitHub Issue 的信息
    issue_title = os.getenv('ISSUE_TITLE')
    issue_body = os.getenv('ISSUE_BODY')
    issue_url = os.getenv('ISSUE_URL')

    # 构建要发送的消息内容
    message = f"新的 GitHub Issue:\n标题: {issue_title}\n\n内容: {issue_body}\n\n链接: {issue_url}"

    # 创建 WeChat 客户端
    client = WeChatClient(appid, appsecret)

    # 使用 WeChatMessage 发送文本消息
    wm = WeChatMessage(client)
    response = wm.send_text(openid, message)
    
    # 打印微信返回的响应结果
    print("WeChat Response:", response)

if __name__ == "__main__":
    main()

