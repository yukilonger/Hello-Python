#!/usr/bin/env python3
# chmod +x

print(1,2,3)


def print_color(red_info, green_info):
    print(f'\033[31m{red_info}\033[0m \033[32m{green_info}\033[0m')

print_color(1,2)

def print_title(info):
    print('\033[0;36m' + info + '\033[0m') # 蓝色字体

print_title('反弹预测：')

def print_highlight(info):
    print('\033[0;33m' + info + '\033[0m') # 黄色字体

print_highlight('高亮')