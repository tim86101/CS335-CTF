# 網路攻防第二次程式作業

## 題目講解
&emsp;&emsp; 給定一組x,y，找到一組a,b使得 ax+by(mod 10000) = 𝑔𝑐𝑑(𝑥,y)。

## 程式說明

&emsp;&emsp;利用`netcat`連接到`140.138.77.30:6077`後，使用迴圈循環1000次測資，將其中接收到的random number由byte型態轉為string型態

&emsp;&emsp;之後使用string 中replace function字串處理去除`b ,[,],\\,n`等字元，將X,Y結果傳入`euclidean function`

&emsp;&emsp;在`euclidean function`，假設a=x,b=y，使a=1,b=1存下左右兩邊的ab值，
最後執行完輾轉相除法後，可以得到ax+by=𝑔𝑐𝑑(x,y),判斷a,b是否大於0，若沒有，則加上10000，最後將𝑔𝑐𝑑,a,b回傳。


