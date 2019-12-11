import turtle
import random
import colorsys

def input_filter():
        while True:
            try:
                a = int(input(inp))
                if a < mi or a > ma:
                    print(message)
                else:
                    return a
            except ValueError:
                print(message)
length = input_filter(2,15,"請問要畫幾條線(範圍:2~15):")
dis = 100
up = 300
lines = 15
space = 10
li = []


#畫線的程式
def draw_line(x, trtl):
    for y in lis:
        trtl.goto(x,y)
        trtl.forward(dis)
        trtl.backward(dis)


#輸入已經畫的位置輸出可以畫線的位置
def choose_loc(lis):
    rng = [n for n in range((up - 15) * -1,up - 15,space)]
    for i in lis:
        rng.remove(i)
    return random.sample(rng, lines)


#連線的程式
def walk(loc,plc,trtl):
    x = int(((length - 1) / -2 + (loc - 1)) * dis)
    down = (up * - 1) - 1
    trtl.penup()
    trtl.goto(x,plc)
    trtl.pendown()
    #判斷現在位置是不是在最上面 是的話從最上面開始畫 不是的話用另一個程式 因為up不在li裡面
    if plc == up:
        #如果在第一行
        if loc == 1:
            trtl.goto(x,li[loc - 1][0])
            trtl.forward(dis)
            return walk(loc + 1,li[loc - 1][0],trtl)
        #如果在最後一行
        elif loc == len(li) + 1:
            trtl.goto(x,li[loc - 2][0])
            trtl.backward(dis)
            return walk(loc - 1,li[loc - 2][0],trtl)
        #都不是的話
        else:
            lines_loc = []
            lines_loc.extend(li[loc - 1])
            lines_loc.extend(li[loc - 2])
            lines_loc = sorted(lines_loc,reverse=True)
            trtl.goto(x,lines_loc[0])
            # 判斷線再左邊還是右邊
            if lines_loc[0] in li[loc - 1]:
                trtl.forward(dis)
                return walk(loc + 1,li[loc - 1][0],trtl)
            else:
                trtl.backward(dis)
                return walk(loc - 1,li[loc - 2][0],trtl)
    else:
        #如果在第一行
        if loc == 1:
            lines_loc = []
            lines_loc.extend(li[loc - 1])
            #如果跑到最下面
            if lines_loc.index(plc) == len(lines_loc) - 1:
                trtl.goto(x,down)
                return 1
            else:
                lines_loc = lines_loc[lines_loc.index(plc) + 1:]
                trtl.goto(x,lines_loc[0])
                trtl.forward(dis)
                return walk(2,lines_loc[0],trtl)
        #如果在最後一行
        elif loc == len(li) + 1:
            lines_loc = []
            lines_loc.extend(li[loc - 2])
            #如果跑到最下面
            if lines_loc.index(plc) == len(lines_loc) - 1:
                trtl.goto(x,down)
                return len(li) + 1
            else:
                lines_loc = lines_loc[lines_loc.index(plc) + 1:]
                trtl.goto(x,lines_loc[0])
                trtl.backward(dis)
                return walk(loc - 1,lines_loc[0],trtl)
        #都不是的話
        else:
            lines_loc = []
            lines_loc.extend(li[loc - 1])
            lines_loc.extend(li[loc - 2])
            lines_loc = sorted(lines_loc,reverse=True)
            #如果跑到最下面
            if lines_loc.index(plc) == len(lines_loc) - 1:
                trtl.goto(x,down)
                return loc
            else:
                lines_loc = lines_loc[lines_loc.index(plc) + 1:]
                trtl.goto(x,lines_loc[0])
                #判斷線再左邊還是右邊
                if lines_loc[0] in li[loc - 1]:
                    trtl.forward(dis)
                    return walk(loc + 1, lines_loc[0], trtl)
                else:
                    trtl.backward(dis)
                    return walk(loc - 1, lines_loc[0], trtl)
#畫表格
window = turtle.Screen()
window.colormode(1)
window.bgcolor("white")
brad = turtle.Turtle()
# brad.color("black")
brad.color("black")
brad.shape("arrow")
brad.speed(0)
brad.pensize(2)
lis = choose_loc(random.sample([n for n in range((up - 15) * - 1, up - 15, space)], lines))
for i in range(int((length - 1) / -2 * dis), int((length - 1) / 2 * dis), dis):
    lis = choose_loc(lis)
    li.append(sorted(lis,reverse=True))
    brad.penup()
    brad.goto(i, up)
    brad.pendown()
    brad.goto(i, up * - 1)
    draw_line(i, brad)
brad.penup()
brad.goto(int((length - 1) / 2 * dis), up)
brad.pendown()
brad.goto(int((length - 1) / 2 * dis), up * - 1)
brad.hideturtle()
#連線
brad.pensize(3)
yorn = input("要不要加速畫線程式動畫(要的話輸入Y或y，不要的話按Enter或任意輸入任何字):")
if yorn == "Y" or yorn == "y":
    brad.speed(0)
else:
    brad.speed(2)
ans = []
done = []
i = 1
col = [i / length for i in range(1,length + 1)]
random.shuffle(col)
while i <= length:
    inp = input_filter(1,length,f"選擇你要走的線(輸入阿拉伯數字1～{length}):")
    if int(inp) not in done:
        done.append(int(inp))
        #設定顏色 讓顏色有一定的彩度
        brad.color(colorsys.hsv_to_rgb(col[i - 1], 0.9, 0.75))
        ans.append((str(i),str(walk(int(inp), up, brad))))
        i += 1
    else:
        print("這條線你已經選過了")
print("\n\n".join(["號對應到的數字是".join(ans[k]) for k in range(len(ans))]))
window.exitonclick()
