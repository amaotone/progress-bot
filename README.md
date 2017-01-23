# 進捗どうですか！

卒論を書くのが嫌なので代わりと言っては何ですが卒論の進捗をTwitterに投稿するスクリプトを書きました。

LaTeX書かれた卒論の文字数をカウントして、Twitterに投稿します。

## 依存関係

- Python3
- tweepy `pip install tweepy`

あとは`detex`と`wc`を使います。

## 使い方

setting.jsonというファイルに、twitter applicationのconsumer keyとかを書きます。

```json
{
  "consumer_key": "hoge",
  "consumer_token": "fuga",
  "token": "foo",
  "secret": "bar"
}
```

あとは

```bash
$ python progress.py <file>
```
