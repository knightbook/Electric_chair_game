#utils.py
# 有効な入力を受け付けるための関数
def get_valid_input(prompt, valid_range):
    while True:
        try:
            # ユーザーに選択を促すメッセージを表示し、入力を受け取る
            choice = int(input(prompt))
            
            # 入力された値が有効な範囲内か確認
            if choice in valid_range:
                # 有効な選択肢なら、その選択肢を返す
                return choice
            else:
                # 範囲外の選択肢の場合、再度入力を促す
                print("無効な選択肢です。再度入力してください。")
        
        # 数字以外が入力された場合のエラーハンドリング
        except ValueError:
            # 数字以外の入力があった場合、再度入力を促す
            print("無効な入力です。数字を入力してください。")
