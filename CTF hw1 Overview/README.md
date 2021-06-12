
# 網路攻防第一次程式作業

## 程式說明

&emsp;&emsp;利用`netcat`連接到`140.138.77.30:6077`後，使用迴圈循環1000次測資，將其中接收到的random number由byte型態轉為string型態

&emsp;&emsp;之後使用string 中replace function字串處理去除`b ,[,],\\,n`等字元，再利用string內建函式split
依照空格切割字串，結果放到int型態的list裡

&emsp;&emsp;將list用內建的sort作排序結果轉回string list，並利用逗號間隔依序放回string後，將結果回傳。



