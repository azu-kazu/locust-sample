# locust-sample
負荷試験ツール [LOCUST](https://locust.io/) のサンプル

# ローカル起動方法

## 前提  
- `pyenv`のインストール
- 試験対象のアプリを起動しておく

## 手順
Pythonのバージョン調整
```
// Python v3.6.11のインストール
$ pyenv install 3.6.11

// カレントディレクトリでv3.6.11を使用できるようにする
$ pyenv local 3.6.11
```

LOCUSTのインストール
```
$ python -m pip install locust
```

起動
```
$ locust

(下と同義)
$ locust -f ./locustfile.py
```

Web UIの表示
```
$ http://localhost:8089
```
