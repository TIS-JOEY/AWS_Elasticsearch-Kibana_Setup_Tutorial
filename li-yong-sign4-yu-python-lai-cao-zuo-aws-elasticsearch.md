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

## 

