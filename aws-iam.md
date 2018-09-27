# AWS IAM 建置教學

AWS IAM\(Identity and Access Management\)是一種可以讓管理者輕鬆管理多個AWS使用者的服務，管控不同群集的人各自擁有哪些權限，以穩定系統與提昇安全性與結構性。

首先，請先移至到你的AWS 服務Dashboard，並點選IAM服務，然後你就會看到以下的介面。

![](.gitbook/assets/iam-dashboard.png)

AWS IAM服務最主要可以分為Users、Roles與Groups，接下來就讓我來帶大家如何創建這些東西。

## AWS Users

#### Step 1 

點選左側導覽欄的Users進入，並點選 Add users。  
接著再輸入user的名字，記得**Programmatic access**必須打勾。

![](.gitbook/assets/iam-users-access-type%20%281%29.png)

#### Step 2

接下來除非你已創建好Group，而可以直接指定此使用者屬於該Group，令所創建的角色擁有該Group的權限外。我們必須點選

