# 透過AWS EC2與Nginx創建反向代理伺服器進行訪問...

### 透過AWS EC2與Nginx創建反向代理伺服器進行訪問...

由上面這個小標題可以很明顯看出我們需要使用到AWS EC2的服務資源，所以我們當然也要先創建一個我們的AWS EC2虛擬機，以下為教學傳送門。 

{% page-ref page="aws-ec2.md" %}

我們的目標應為在該虛擬機中，透過Nginx來創建反向代理伺服器，並一樣透過SIGN 4簽署協議來對AWS Elasticsearch進行訪問。

