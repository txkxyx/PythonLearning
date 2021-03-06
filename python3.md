# Python3 Install

```
brew install pytho3
==> Summary
🍺  /usr/local/Cellar/python3/3.6.4_2: 3,593 files, 56.2MB

python3 --version3
ython 3.6.4

```

# Python文法
## 算術計算

``` python
>>> 1+2 #和
3
>>> 1-2 #差
-1
>>> 4*5 #乗算
20
>>> 7/5 #除算
1.4
>>> 3**2 #累乗
9
```

## データ型
```python
>>> type (10)
<class 'int'>
>>> type (1.21)
<class 'float'>
>>> type ("python")
<class 'str'>
```

## 変数
```python
>>> x = 10
>>> print(x)
10
>>> x = 100
>>> print(x)
100
>>> y = 2.12
>>> x * y
212.0
>>> type(x * y)
<class 'float'>
>>> z = x * y
>>> type (z)
<class 'float'>
```

## リスト
```python
>>> a = [1,2,3,4,5] #リストの作成
>>> print(a) #リストの中身を出力
[1, 2, 3, 4, 5]
>>> type(a) #データ型を出力
<class 'list'>
>>> len(a) #リストの長さを出力
5
>>> a[0] #リストの要素にアクセス
1
>>> a[4] #
5
>>> a[4] = 99 #値を代入
>>> print(a)
[1, 2, 3, 4, 99]
>>> a[0:2] #インデックスの0番目から1番目までを取得
[1, 2]
>>> a[1:] #インデックスの1番目から最後まで取得
[2, 3, 4, 99]
>>> a[:3] #最初のインデックスから２番目まで取得
[1, 2, 3]
>>> a[:-1] #最初から最後から1つ前まで取得
[1, 2, 3, 4]
>>> b = ["a","b","c","d"] #文字のリストを作成
>>> print(b)
['a', 'b', 'c', 'd']
```
