from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m = PyMouse()
k = PyKeyboard()
x_dim, y_dim = m.screen_size()
print(m.screen_size())

print(x_dim)
print(y_dim)
time.sleep(2)


def main():
    try:
       for i in range(40):
           print(i)
           print("reward3")
           k.tab_key("H")
           time.sleep(4)

           print("startbattle")
           k.tab_key("I")
           time.sleep(7)

           print("begin")
           k.tab_key("o")
           time.sleep(69)



           print("reward1")
           m.click(792, 768)
           k.tab_key("p")

           print("reward2")
           k.tab_key("p")
           time.sleep(2)


    except:
        print("jieshu")



main()