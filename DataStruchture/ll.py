class Llist:

    def __init__(self, name, link=None):
        self.name = name
        self.link = link


list = Llist('a')
temp = Llist("b")
list.link = temp


for i in range(2):
    if list.link != None:
        print("node : " + list.name + " >>", end=" ")
    else:
        print("node : " + list.name)

    list = list.link