# AWS Kibana

## Introduction

通常我們在使用Elasticsearch服務時，亦會使用其他兩個相輔相成的服務，分別是Logstash和Kibana。Logstash是用來作為日誌分析之用，而Kibana則是用來進行可視化分析之用。  
那麼這章就讓我來帶大家來進行Kibana的配置吧～

## Problem...

當你依照第一章將我們的AWS Elasticsearch創建並配置完成後，你會發現奇怪，為什麼我可以訪問Elasticsearch但不能訪問AWS Kibana呢？

原因在於，AWS對於Kibana介面的保護措施\(AWS 沒有提供X-Pack\)，因為在Kibana介面中有一個Dev tools，若任何人都可以訪問Kibana的話，那麼任何人都可以透過Restful語句來進行資料的更動，太危險了。

所以在這裡我就要來教大家，如何來訪問AWS Kibana。

## 反向代理伺服器

相信大家都有聽過代理伺服器\(Proxy\)，其是一種可以隱藏主機的真實位址的方式，提升安全性，甚至可以將一些快取放置於Proxy中，提升搜尋的速度。

代理伺服器的工作原理是去各後方伺服器抓取資源放在伺服器上供client端進行讀取下載，而反向代理伺服器則正好相反，他會根據client端的request，從關聯的一組或多組伺服器上取得資源再返還給clietn端。clietn端只會知道反向代理伺服器的IP位址而不會知道代理伺服器後面的伺服器叢集的位址存在。後方伺服器叢集不能被用戶直接連結，而只能透過反向代理伺服器，使用這種方式除了可以提昇安全性外，亦可提供負載功能、加密、快取等。

而在這邊我們就是要建立一個反向代理伺服器，讓用戶可以透過這個反向代理伺服器來與AWS Kibana進行連接。

### 透過npm --&gt; aws-es-kibana進行Sign4訪問...

#### Unix-like

1. 安裝npm
2. 開啟終端機，輸入

```text
$ npm install -g aws-es-kibana
```

    3. 透過終端機cd至root目錄中，於終端機輸入以下指令來建立.aws的檔案夾

```text
$ cat ~/.aws 
```

    4. 進入.aws資料夾後後建立一個名為credentials的檔案  
         並編寫以下內容: 

```text
[default] 
aws_access_key_id = ****************
aws_secret_access_key = ****************
```

    5. 回到終端機中輸入：

```text
$ export AWS_ACCESS_KEY_ID = ****************
$ export AWS_SECRET_ACCESS_KEY = ****************
```

    6. 完成建置後，即可於任意時候在終端機透過以下指令來與AWS Kibana連接

```text
$ aws-es-kibana <cluster-endpoint>
# cluster-endpoint可在AWS elasticsearch中找到
```

> aws\_access\_key\_id與aws\_secret\_access\_key

#### 

