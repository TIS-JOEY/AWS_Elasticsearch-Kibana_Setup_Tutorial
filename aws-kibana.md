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

### 透過npm安裝aws-es-kibana套件進行Sign4簽署協議訪問...

要對AWS資源進行Sign4簽名協議訪問，首先必須要創建一個擁有對Elasticsearch訪問權限的IAM角色。  
以下為教學傳送門

{% page-ref page="aws-iam.md" %}

當你創建好IAM角色時，會得到屬於該角色的ACCESS\_KEY和ACCESS\_SECRET\_KEY，而接下來我們就要使用這兩個密鑰來進行SIGN4協議簽署以訪問AWS Kibana。

以下分兩種作業系統來介紹安裝流程

#### Unix-like

1. 安裝npm
2. 開啟終端機，輸入

```text
$ npm install -g aws-es-kibana
```

    3. 透過終端機cd至user目錄，於終端機輸入以下指令來建立.aws的檔案夾並進入

```text
$ mkdir ~/.aws 
$ cd .aws
```

    4. cd進入.aws資料夾後vim 一個名為credentials的檔案，使用INSERT模式\(輸入i\)  
        並開始編寫以下內容: 

```text
[default] 
aws_access_key_id = ****************
aws_secret_access_key = ****************
```

         完成編寫後，再按ESC，並輸入:wq來儲存寫入並跳出。

    5. 回到終端機後中輸入：

```text
$ export AWS_ACCESS_KEY_ID = ****************
$ export AWS_SECRET_ACCESS_KEY = ****************
```

    6. 完成建置後，即可於任意時候在終端機透過以下指令來與AWS Kibana連接

```text
$ aws-es-kibana <cluster-endpoint>
# cluster-endpoint可在AWS elasticsearch中找到
```

AWS Kibana的連線網址應為127.0.0.1:9200/\_plugin/kibana

#### Windows

1. 安裝npm
2. 於終端輸入以下指令

```text
npm install -g aws-es-kibana
```

    3. 透過終端機cd至C://Users/使用者名稱/，於終端機輸入以下指令來建立.aws的  
         檔案夾並進入.aws資料夾

```text
$ mkdir ~/.aws 
$ cd .aws
```

    4. cd進入.aws資料夾後一樣也是vim出一個名為credentials的檔案，使用INSERT  
        模式\(輸入i\)，並開始編寫以下內容: 

```text
[default] 
aws_access_key_id = ****************
aws_secret_access_key = ****************
```

         完成編寫後，再按ESC，並輸入:wq來儲存寫入並跳出。  
  
     5. 回到終端機後中輸入：

```text
$ SET AWS_ACCESS_KEY_ID = ****************
$ SET AWS_SECRET_ACCESS_KEY = ****************
```

     6. 完成建置後，即可於任意時候在終端機透過以下指令來與AWS Kibana連接

```text
$ aws-es-kibana <cluster-endpoint>
# cluster-endpoint可在AWS elasticsearch中找到
```

AWS Kibana的連線網址應為127.0.0.1:9200/\_plugin/kibana

### 透過AWS EC2與Nginx創建反向代理伺服器進行訪問...

由上面這個小標題可以很明顯看出我們需要使用到AWS EC2的服務資源，所以我們當然也要先創建一個我們的AWS EC2虛擬機，以下為教學傳送門。 

{% page-ref page="aws-ec2.md" %}

我們的目標應為在該虛擬機中，透過Nginx來創建反向代理伺服器，並一樣透過SIGN 4簽署協議來對AWS Elasticsearch進行訪問。

## Signature 4

簡單來說，Signature Version 4是將身份驗證訊息添加到AWS request請求的過程。其工作原理如下：

1. 首先肯定的，你必須先創建出一個IAM角色，並配置他可以擁有哪些權限。當創建完畢後，你便會得到該角色獨一無二的一對密鑰對\(訪問密鑰ID和秘密訪問密鑰\)。
2. 創建出一個AWS request。
3. 使用該AWS request和其他訊息來創建要簽署的字符串。
4. 使用IAM腳四的秘密訪問密鑰來生成一個簽名密鑰，並使用該密鑰和要簽署的字符串來產生簽名。
5. 當AWS收到請求後，便會和你剛剛執行的相同步驟來計算簽名，若計算出的簽名和你所產生的簽名是匹配的，則處理請求，反之則拒絕。

除了上述我們可以用Sign 4來訪問AWS Kibana外，我們亦可透過Sign 4搭配其他程式語言來操作AWS Elasticsearch數據，教學傳送門如下。

{% page-ref page="li-yong-sign4python-cao-zuo-aws-elasticsearch.md" %}

