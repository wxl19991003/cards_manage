card_list = []


def menu():
    print("*" * 50)
    print("""欢迎使用名片管理系统 V1.0
            请输入：
            1.创建名片
            2.查看名片
            3.查询名片
            
            0.退出程序""")
    print("*" * 50)


def new_cards():
    print("_" * 50)
    print("创建新名片：")
    name_str = input("请输入姓名：")
    tele_str = input("请输入电话：")
    age_str = input("请输入年龄：")
    email_str = input("请输入邮箱：")
    card_dit = {"name": name_str,
                "tele": tele_str,
                "age": age_str,
                "email": email_str}
    card_list.append(card_dit)
    print("保存成功！")
    print("_" * 50)


def cards_read():
    if len(card_list) == 0:
        print("没有保存的名片")
        return
    print("_" * 50)
    print("查看所有名片：")
    print("姓名\t\t电话\t\t年龄\t\t邮箱\t\t")
    print("=" * 50)
    for card_dit in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dit["name"],
                                        card_dit["tele"],
                                        card_dit["age"],
                                        card_dit["email"]))
    print("_" * 50)


def cards_search():
    print("_" * 50)
    print("查询名片：")
    find_name = input("输入查询的姓名：")
    for dit in card_list:
        if dit["name"] == find_name:
            print("姓名\t\t电话\t\t年龄\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (dit["name"],
                                            dit["tele"],
                                            dit["age"],
                                            dit["email"]))
            card_op(dit)
            break
    else:
        print("not found")

    print("_" * 50)


def card_op(found_dic):
    option = input("请输入您要进行的操作：1.修改名片\t2.删除名片\t0.返回主菜单\n")
    if option == "1":
        found_dic["name"] = input_func(found_dic["name"], "请输入姓名：:")
        found_dic["tele"] = input_func(found_dic["tele"], "请输入电话：")
        found_dic["age"] = input_func(found_dic["age"], "请输入年龄：")
        found_dic["email"] = input_func(found_dic["email"], "请输入邮箱：")
        print("修改完成！")
    elif option == "2":
        card_list.remove(found_dic)
        print("删除成功！")


def input_func(old_dic, tip_mess):
    """

    :param old_dic:
    :param tip_mess:
    :return:
    """
    value_input = input(tip_mess)
    if len(value_input) > 0:
        return value_input
    else:
        return old_dic
