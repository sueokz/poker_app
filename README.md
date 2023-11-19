# poker_app

## サービス概要
コール・ベッドしても良い手札の範囲（ハンドレンジ）が即座に見れるアプリです。<br>
他のアプリでは数が少なかったり、スマートフォンではアプリの2画面ができないため作りました。<br>
今後欲しい機能ができた際増やすために作ろうと思いました。
使用している画像は個人利用のみ可の素材を使ったため、記載していません。<br>
![poker_v2](https://github.com/sueokz/poker_app/assets/77056617/7400a924-33c4-4fe2-9011-7be907b22b6c)


空白のところには下記のような画像が表示されます。<br>
 [ポジションの優位性](https://www.google.com/search?q=%E3%83%9D%E3%83%BC%E3%82%AB%E3%83%BC%E3%80%80%E5%BC%B7%E3%81%95%E9%85%8D%E7%BD%AE&tbm=isch&ved=2ahUKEwj7mNjp9M-CAxXRePUHHSL3AvkQ2-cCegQIABAA&oq=%E3%83%9D%E3%83%BC%E3%82%AB%E3%83%BC%E3%80%80%E5%BC%B7%E3%81%95%E9%85%8D%E7%BD%AE&gs_lcp=CgNpbWcQAzoECCMQJzoLCAAQgAQQsQMQgwE6BQgAEIAEOgcIABCABBAEOgkIABCABBAEEBg6BwgAEIAEEBc6CAgAEAgQHhAXUNgYWPtEYJZLaABwAHgAgAGgAYgB8A6SAQQ2LjExmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=NOtZZfuuL9Hx1e8Pou6LyA8&bih=629&biw=1366#imgrc=nvQcW2fUsdNVqM)のようなイメージになります<br>



## ユーザー
- Pokerを始めたての初心者が対象。<br>

## 問題
- 確認のしやすさ<br>
確率の重要性やコールの回数が多いことを意識し始めてた人がいきなりパターンの暗記は難しい。<br>

- 複数パターン<br>
ポーカーはポジションによってコールしても良い手札が変わるので、複数のパターンを表示したい。<br>

- 即時性<br>
ゲーム中に先ほどのアクションは悪くなかったのかも考えたい。<br>

## 解決方法
- 確認のしやすさ<br>
ボタンと画像だけのシンプルなアプリなので画面の場所をとらない。<br>

- 複数パターン<br>
欲しいパターンの数だけ画像とボタンを用意した。<br>

- 即時性<br>
ボタンを押すだけで画像を表示させるようにした。<br>
最初は選択ボタンを用意していましたが、削除しました。ポーカー中に確認できます。
![poker_vi](https://github.com/sueokz/poker_app/assets/77056617/aedea7aa-a792-44a1-a180-4d275373a5fa)

## 今後
- サイズを揃える<br>
違いの画像を使ったため、見た目が汚いし、コードをサイズが合うように何度も書き直したので修正したい。<br>

- メモ機能<br>
ゲーム中に考えたことや戦略などを簡単にメモできる入力欄を作る<br>

- 勝率クイズ<br>
手札をランダムに生成し、勝率を当てるクイズを作る。<br>

# 使用技術
## 言語フレームワーク
- python
