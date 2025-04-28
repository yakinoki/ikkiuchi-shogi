![](https://img.shields.io/github/repo-size/yakinoki/ikkiuchishogi)

# ikkiuchi-shogi

「一騎打ち将棋（ikkiuchi shogi）」は、  
**横移動→縦移動**の2ステップで盤上を移動する、シンプルながら戦略性のある将棋風ゲームです。  
横方向の移動時に相手と重なった時点で勝敗が決します。  
玉（King）はランダムに動きます。

---

## 構成

### src/

- **ikkiuchishogi_game.py**  
  ゲームロジック本体。
  - 横移動 → 縦移動のルールを実装。
  - 横移動の時点で相手に重なれば勝ち。
  - 玉はランダムに移動。

- **ikkiuchishogi_game_play.py**  
  ゲームを実行するエントリポイント。

---

## old/

過去バージョンのアーカイブです。

- **ikkiuchishogi_game_1.py**  
  初期バージョン。基本ルール（横移動→縦移動）を実装。

- **ikkiuchishogi_game_2.py**  
  コードブラッシュアップ版（リファクタリングあり）。

- **ikkiuchishogi_game_3.py**  
  玉（King）のランダム自動移動を導入。

---

## その他

- `config.yml`：設定ファイル
- `result_kifu/`：対局結果を保存するディレクトリ
