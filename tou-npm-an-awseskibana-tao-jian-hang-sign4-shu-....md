# 透過npm安裝aws-es-kibana套件進行Sign4簽署協議訪問...

### 透過npm安裝aws-es-kibana套件進行Sign4簽署協議訪問...

要對AWS資源進行Sign4簽名協議訪問，首先必須要創建一個擁有對Elasticsearch訪問權限的IAM角色。  
以下為教學傳送門

* [AWS IAM 建置教學](aws-iam-jian-zhi-jiao-xue.md)

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

