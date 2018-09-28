# 利用Sign4與Python來操作AWS Elasticsearch

現在大家應該都知道AWS Elasticsearch那是一個分散式搜尋引擎與分析利器，那麼想當然爾，他最重要的資產就是 - DATA，因此在這個章節會跟各位分享，如何對AWS Elasticsearch進行數據操作吧～

那麼看標題可以知道我們會以Python來作為我們的程式語言，並透過Sign4來對AWS Elasticsearch上的資料進行更動。因此首先讓我先簡單介紹一下Signature4到底是什麼吧。

## Signature 4

簡單來說，Signature Version 4是將身份驗證訊息添加到AWS request請求的過程。其工作原理如下：

1. 首先肯定的，你必須先創建出一個IAM角色，並配置他可以擁有哪些權限。當創建完畢後，你便會得到該角色獨一無二的一對密鑰對\(訪問密鑰ID和秘密訪問密鑰\)。
2. 創建出一個AWS request。
3. 使用該AWS request和其他訊息來創建要簽署的字符串。
4. 使用IAM腳四的秘密訪問密鑰來生成一個簽名密鑰，並使用該密鑰和要簽署的字符串來產生簽名。
5. 當AWS收到請求後，便會和你剛剛執行的相同步驟來計算簽名，若計算出的簽名和你所產生的簽名是匹配的，則處理請求，反之則拒絕。

## 產生密鑰對

有了上述的了解後，我們知道我們一定必須要有可以對AWS Elasticsearch數據更動權限的IAM User，奉上教學傳送門：[AWS IAM 建置教學](aws-iam-jian-zhi-jiao-xue.md)

------------------------------------------------------------------------------------------------------------------------------
## 資料上傳
我們在這邊有提供一個基於Python Elasticsearch Client和aws-requests-auth的Python資料上傳接口，連結如下：
* [基於Python Elasticsearch Client 與 aws-requests-auth，以Sign4簽署協議進行AWS Elasticsearch數據操作](https://github.com/TIS-JOEY/AWS_Elasticsearch_Python_Interface/blob/master/README.md)

## 前置作業：
```text
$ pip install aws-requests-auth
$ pip install elasticsearch
```

## 批次上傳
### 上傳資料格式
| _index | _type | _id | 欄名1 | 欄名2 | 欄名3 | 欄名... |
| --- | --- | --- | --- | --- | --- | --- |
| Taiwan | Tutorial | 1 | abc | def | ghi | jkl |
| Taiwan | Tutorial | 2 | mno | pqr | stu | vwx |

前三欄為固定格式，Elasticsearch中的_index等同於RDBMS的Database，_type等同於RDBMS的Table，而_id就等於id，其餘則依你的需求進行欄位上傳。
Elasticsearch的分散式儲存系統也是採Nosql格式儲存(以JSON格式)，因此每筆資料的欄位可彈性調整，並不用像RDBMS需先預定義好欄位且不得更動。
> AWS_Elasticsearch_bulkUpload.py所能讀取的資料格式為xlsx檔。



### 批次資料上傳說明
首先，須先import所下載來的AWS_Elasticsearch_bulkUpload.py檔

IAM user的access key id與IAM user的secret access key的取得教學，可至下方傳送門查看
* [AWS IAM 建置教學](aws-iam-jian-zhi-jiao-xue.md)

欲寫入id之起始位置代表的是你希望從哪一個id號開始寫入，因為AWS Elasticsearch中若在同一個index和type時，id是獨一無二的，若AWS Elasticsearch發現id號衝突時，會直接進行覆蓋(更新)。

```text
import AWS_Elasticsearch_bulkUpload

awses = AWS_Elasticsearch_bulkUpload.AWSes(access_key = 'IAM user的 access key id',
				  secret_access_key = 'IAM user的secrect access key',
				  host = 'AWS Elasticsearch domain',
				  region = 'AWS設置地區')

awses.login()
awses.create_bulk('欲上傳原始檔目錄位置(須為xlsx檔格式)','暫存檔目錄位置(須為json檔格式)','(欲寫入id之起始位置)')
```




有關於AWS Elasticsearch與Kibana建置與連結可至以下傳送門查看
* [AWS_Elasticsearch-Kibana_建置教學](https://github.com/TIS-JOEY/AWS_Elasticsearch-Kibana_Setup_Tutorial)







資料來源：

Python Elasticsearch Client ：https://elasticsearch-py.readthedocs.io/en/master/ 

aws-requests-auth：https://github.com/DavidMuller/aws-requests-auth 

