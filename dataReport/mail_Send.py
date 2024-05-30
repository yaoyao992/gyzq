import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 邮件发送者和接收者
sender_email = "yaoyao@gyzq.com.cn"
receiver_email = "yaoyao992@foxmail.com"
password = input("Type your password and press enter:")

# 创建 MIMEText 对象，用于构建邮件内容
message = MIMEMultipart("alternative")
message["Subject"] = Header("Python SMTP Email Test")
message["From"] = sender_email
message["To"] = receiver_email

# 创建邮件正文
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="https://www.python.org">Python</a> 
       <a href="https://docs.python.org/3/library/email.html">email</a> 
       <a href="https://docs.python.org/3/library/email.mime.html">mime</a> 
    </p>
  </body>
</html>
"""

# 创建一个MIMEText对象，用于创建一个HTML格式的邮件正文
part2 = MIMEText(html, "html")

# 将MIMEText对象添加到MIMEMultipart对象中
message.attach(part2)

# 创建一个SMTP对象
with smtplib.SMTP("mail.gyzq.com.cn", 465) as server:
    server.starttls()  # 启用安全模式
    server.login(sender_email, password)  # 登录验证
    server.sendmail(sender_email, receiver_email, message.as_string())  # 发送邮件
