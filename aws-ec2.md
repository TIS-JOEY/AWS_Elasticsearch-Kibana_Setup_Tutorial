# AWS EC2建置教學

AWS EC2的全名為Amazon Elastic Compute Cloud，其以Web服務的方式，可讓使用者租用AWS雲端電腦系統，彈性地運行Amazon虛擬機器映像檔，使用者可以在這個虛擬機器上自由運用該系統。其優點便是在於非常地彈性，使用者可以隨時創建、終止、執行該虛擬機器，並採用量付費。

那麼一樣話不多說，讓我們直接開始創建AWS EC2吧。

## Step1 進入AWS EC2 Service

進入Amazon Dashboard，並點選EC2進入。

![](.gitbook/assets/dashboard.png)

![](.gitbook/assets/aws-ec2.png)

## Step 2 創建EC2 Instance

首先先點選Running Instances，你會看到以下介面，接著點選Launch Instance。

![](.gitbook/assets/aws-ec2-launch-instance.png)

## Step 3 選擇虛擬機器映像檔

在這邊你可以看到有很多很多的映像檔，那麼就依你自己的喜好去做選擇吧～在這邊我們選擇的是「Amazon Linux 2 AMI \(HVM\), SSD Volume Type 」

## Step 4 選擇虛擬實例類型

一樣也是依你的需求去選，那麼在這邊我們當然也一樣選擇免費的XD。

![](.gitbook/assets/aws-ec2-instance-type.png)

## Step 5 進階設定

#### Sub-step 1 進階配置

選擇完虛擬實例類型後點選「Next：Configure Instance Details」，你會看到以下介面，選擇所建立的IAM role，並選擇「Next:Add Storage」。

![](.gitbook/assets/aws-ec2-instance-detail.png)

#### Sub-step 2 容量配置

接著選擇你要賦予該虛擬機器多少容量與其他相關配置，這個一樣是依照個人的需求去定，當訂定好了後點選「Next：Add Tags」。

![](.gitbook/assets/aws-ec2-add-storage.png)

#### Sub-step 3 標籤配置

接著便是為你的虛擬機器加上Tags，方便識別，Name的位置請填寫Name，Value則填寫你要對該虛擬機命名的名字。配置完後，點選「Next：Configure Security Group」。

#### Sub-step 4 安全組配置

這步很重要，會取決於有哪些IP可以對此EC2虛擬機進行訪問，且除此之外亦要能夠讓我們可以透過該虛擬機器所建立的反向代理伺服器來訪問Kibana。

那麼在這邊我們所配置的有

* SSH ： 你希望可以連上此EC2 Instance的IP網段，你可以透過mask來讓同一網域的人皆可連上。
* All HTTP
* All HTTPS



