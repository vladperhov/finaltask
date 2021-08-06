# -*- coding: utf-8 -*-
f = open('/home/task/info.txt')
with open('/home/task/index.html', 'w+') as output, open('home/task/info.txt', 'r') as input:
    output.write(input.read())
