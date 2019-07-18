from bst import Bst, Node


if __name__ == "__main__":

    bst = Bst()

    bst.put(50, "수박")
    bst.put(60, "멜론")
    bst.put(30, "복숭아")
    bst.put(10, "망고")
    bst.put(40, "체리")
    # bst.put(25, "포도")
    # bst.put(15, "오렌지")
    # bst.put(35, "바나나")
    bst.put(90, "뀰")
    # bst.put(80, "레몬")
    # bst.put(5, "딸기")
    # bst.put(70, "키위")

    print("InOrder output >> ", end="")
    bst.inOrder(bst.root)


    print("\n15 ?? :", bst.get(50))

    # delnode = bst.delete_min()
    # print("\n 최소값 삭제 후 트리 >> ", end="s")
    # bst.inOrder(bst.root)
    #
    #
    # print("\n최소값 : ", end="")
    # m = bst.min()
    # print(m.key, m.value)
    #
    #
    # print("\n최댓값 삭제 후 트리 >> ", end="")
    # delnode2 = bst.delete_max()
    # bst.inOrder(bst.root)
    #
    # print("\n최댓값 : ", end="")
    # m2 = bst.max()
    # print(m2.key, m2.value)


    print("===========================================================================")
    bst.delete(50)
    bst.inOrder(bst.root)