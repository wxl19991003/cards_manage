import cards_tools

while True:
    cards_tools.menu()
    options = input("选择您的操作：")
    if options in ("1", "2", "3", "0"):
        if options == "1":
            cards_tools.new_cards()
        elif options == "2":
            cards_tools.cards_read()
        elif options == "3":
            cards_tools.cards_search()
        else:
            break

    else:
        print("输入错误，请重新输入：")
