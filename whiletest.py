#while True:
#    mode = input('請輸入搭配方案: ')
#    if mode == 'q':
#        break
#    elif mode == '1':
#        print('尚未啟動')
#    elif mode == '2':
#        print('好像也還沒好')
#    else:
#        print('只能輸入1 or 2 or q, 謝謝')


ans = 'a1234'
x = 3

while x > 0:
    intt = input('Please input password: ')
    if ans == intt:
        print('correct and pass')
        break
    else:
        x = x - 1
        print('Not correct')
        if x >0:
            print('You can try', x)


