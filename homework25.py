# class Test:
#     def __init__(self):
#         self.lst=[]
#     def test1(self,add):
#         self.lst.append(add)
#         print(f"Task added: {add}")
#     def test2(self,edit,newtask):
#         self.lst[edit]=newtask
#         print(f"Task edited: {newtask}")
#     def test3(self,delete):
#         self.lst.pop(delete)
#         print(f"Task deleted: {self.lst}")
#     def test4(self):
#         print(self.lst)
#     def test5(self):
#         pass
# obj1=Test()
# while True:
#     print("1. Add Task")
#     print("2. Edit Task")
#     print("3. Delete Task")
#     print("4. Show Tasks")
#     print("5. Exit")
#     a=input()
#     if a=="1":
#         b=input()
#         obj1.test1(b)
#     if a=="2":
#         obj1.test4()
#         c=int(input())-1
#         d=input()
#         obj1.test2(c,d)
#     if a=="3":
#         obj1.test4()
#         c=int(input())-1
#         obj1.test3(c)
#     if a=="4":
#         obj1.test4()
#     if a=="5":
#         print("Programm finished")
#         break
