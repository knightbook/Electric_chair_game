def get_valid_input(prompt, valid_range):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_range:
                return choice
            else:
                print("無効な選択肢です。再度入力してください。")
        except ValueError:
            print("無効な入力です。数字を入力してください。")
