from ikkiuchishogi_game import ShogiCls
from datetime import datetime

if __name__ == '__main__':

    taikyoku = ShogiCls()

    # 盤面表示。
    taikyoku.shogi_display()
    # 手番表示。
    taikyoku.shogi_yourturn()
    
    # 対局終了までループ。
    while True:
        # 対局が終わったか判断する
        if taikyoku.shogi_checkendofgame() == 1:
            break
        else:
            # どこに駒を移動させるか入力。
            taikyoku.shogi_inputXY()
    
    # 対局終了後にログをresult_kifuに吐き出す
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"./result_kifu/game_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"対局結果: {taikyoku.result}\n")
        f.write("棋譜:\n")
        for move in taikyoku.moves:
            f.write(f"{move}\n")
    print(f"ログを {filename} に保存しました。")