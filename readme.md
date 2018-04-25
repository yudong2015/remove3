# 问题：标号1-n的n个人首尾相接，1到3报数，报到3的退出，求最后一个人的标号？


## 举例（1~10）

1, 2, 3, 4, 5, 6, 7, 8, 9, 10


第一轮：1, 2, 4, 5, 7, 8, 10

第二轮：1, 4, 5, 8, 10

第三轮：4, 5, 10

第四轮：4, 10

第五轮：4 ... 最后一个人是标号为4的人


## 分析

- 第一轮报数从 0 + 1 开始, 去掉((10+0)//3)个（3、6、9 ）, 剩余 10-((10+0)//3)=7个

- 第二轮报数从 1 ((10+0)%3) + 1 开始, 去掉((7+1)//3)个（2、7），剩余 7-((7+1)//3))=5个

- 第三轮报数从 2 ((7+1)%3) + 1 开始, 去掉((5+1)//3)个（1, 8），剩余 5-((5+2)//3)=3个

- 第四轮报数从 1 ((5+2)%3) + 1 开始, 去掉((3+1)//3)个（5），剩余 3-((3+1)//3)=2

- 第五轮报数从 1 (3+1)%3) + 1 开始, 去掉((2+1)//3)个（10），剩余 2-((2+1)//3)=1 ... 剩余1个，结束



#### 分析每一轮报数过程中X号（设最后剩余人的标号为X）的位置(position)变化

第一轮：start1=0+1，position1=X, n1=n

第二轮：start2=(n1 + start1 - 1) % 3 + 1, position2 = position1-((position1 + start1 - 1)//3), n2=n1-((n1 + start1 - 1)//3

第三轮：start3=(n2 + start2 - 1)%3 + 1, position3=position2-((position2 + start2 - 1)//3), n3=n2-((n2 + start2 - 1)//3

...

第N轮：startN=(nN'1 + startN'1 - 1) % 3 + 1, positionN=positionN'1 - ((positionN'1 + startN'1 - 1) // 3), nN=nN'1 - ((nN'1 + startN'1 - 1) // 3

...


第M-1轮：startM'1=(nM'2 + startM'2 - 1) % 3 + 1, positionM'1=positionM'2 - ((positionM'2 + startM'2 - 1) // 3), n=2

第M轮：startM=(nM'1 + startM'1 -1)%3 + 1, position=1, n=1



#### 倒着推导X的位置（最初的位置也既标号）

- 由于X在每一轮的报数中都没有退出，所以对于随机轮T ((positionT + startT - 1)%3)=1或2

- X的位置position是整数，且最后一定是1（只剩他）


第N+1轮：

```
positionN - ((positionN + startN - 1) // 3 ) = positionN1
```

设 (positionN + startN - 1) % 3 = a (1或2)

则上面的伪码转换为数学表达式：


```
positionN - ((positionN + startN - 1 - a) / 3 ) = positionN1

=====>

positionN = (3positionN1 + startN - 1 - a) / 2
```


得到公式：

 __positionN = (3positionN1 + startN - 1 - a) / 2__

根据上面分析可知：从初始的start=0和已知的n以及最后只剩1个数，可以算出每一轮报数的start; 有了每一轮的start，以及下面条件：

 - 最后一轮positionpN1是1
 - a是1或者2
 - positionN是整数

 可以推出X最初的位置，也既标号。


-----------

注：% 表示除法取余数，//表示除法取商数，/ 表示数学上的除号