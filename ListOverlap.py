def list_overlap():
    common_list = []
    item = " "
    a_list = []
    while item != "":
        item = input("Add something to the first list. Enter nothing to end list: ")
        if item != "":
            a_list.append(item)

    item = " "
    b_list = []
    while item != "":
        item = input("Add something to the second list. Enter nothing to end list: ")
        if item != "":
            b_list.append(item)

    print("Here are the final lists:\n" + str(a_list) + "\n" + str(b_list))
    if len(a_list) == 0 or len(b_list) == 0:
        return

    for i in a_list:
        for j in b_list:
            if i == j:
                if i in common_list:
                    continue
                else:
                    common_list.append(i)

    print(common_list)


def list_overlap_comprehension():
    common_list = []
    item = " "
    a_list = []
    while item != "":
        item = input("Add something to the first list. Enter nothing to end list: ")
        if item != "":
            a_list.append(item)

    item = " "
    b_list = []
    while item != "":
        item = input("Add something to the second list. Enter nothing to end list: ")
        if item != "":
            b_list.append(item)

    print("Here are the final lists:\n" + str(a_list) + "\n" + str(b_list))
    if len(a_list) == 0 or len(b_list) == 0:
        return

    [common_list.append(i) for i in a_list for j in b_list if i == j if i not in common_list]
    print(common_list)


list_overlap()
list_overlap_comprehension()
