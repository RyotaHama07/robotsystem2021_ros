# 掛け算ROSパッケージ

2021年度のロボットシステム学で作成したROSのパッケージです。表示される掛け算の答えを入力すると正解か不正解かを判別してくれます。レベルは３つあり、それぞれ選択できます。

## 製作
このROSパッケージはロボットシステム学第10回の講義内に作成したパッケージ[mypkg](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)を参考に作成しています。
### 製作者
Ryota Hama and Ryuichi Ueda 
___


## 環境

- 本体 : Raspberry Pi 4 
- OS  :  ubuntu 20.04 
- ROS1

___

## 実装内容

- ノードを起動しスタートすると掛け算が表示されます。その掛け算の答えが正解か不正解かを判別します。
- 間違った答えを入力すると正しい答えを表示します。
- Lv1 (1桁×1桁) Lv2 (2桁×1桁) Lv3 (2桁×2桁)の３つのレベルがあります。
___
## 環境
### ワークスペース
以下のロボットシステム第10回の資料を参考にワークスペースを構築しています。

https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md

___
## インストール
パッケージを使用するために以下のコマンドを実行してください。
```
cd catkin_ws/src
git clone https://github.com/RyotaHama07/robotsystem2021_ros.git
cd ..
catkin_make 
source ~/.bashrc
```
___

## 実行
すべてノードを起動するために以下のコマンドを上から順に実行してください。

- 端末1　ROSを起動する
```
roscore
```

- 端末2　ノード1(random_genration.py)を起動する

```
rosrun robotsystem2021_ros random_generation.py
```

- 端末3　ノード2(mult.py)を起動する

```
cd catkin_ws
rosrun robotsystem2021_ros mult.py
```
ノード起動したら、表示される指示に従ってレベルを入力しスタート
___

## 終了
終了する場合は Ctrl + C を押してください。
___

## デモ動画

下のリンクよりデモ動画を見れます。

https://youtu.be/2ASoFRfOEMk
___

## ライセンス

[BSD 3-Clause License]
