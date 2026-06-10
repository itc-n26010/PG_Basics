zenkai = {"1": "169",
        "2": "blue"
        }

n = input("数字を入力してください:")
if n in zenkai:
    G_zenkai = zenkai[n]
    print(G_zenkai)
else:
    print("見つかりません")

