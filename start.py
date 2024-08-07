import os
import subprocess
import sys
import time
from datetime import datetime


def is_workday(date):
    """判断给定日期是否是工作日（周一到周五）"""
    return date.weekday() < 5  # 周一到周四为0到4，周五为4（但返回True），周六和周日为5和6


def is_six(date):
    if date.hour > 18:
        return True
    else:
        return False


def read_software_paths(filename):
    """从配置文件中读取软件路径并存储到列表中"""
    software_paths = []
    with open(os.getcwd() + "\\" + filename, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除行首和行尾的空白字符，并检查是否包含等号
            stripped_line = line.strip()
            if '=' in stripped_line and not stripped_line.startswith('['):
                # 分割键值对
                key, path = stripped_line.split('=', 1)
                # 假设我们只关心路径
                software_paths.append(path)
    return software_paths


def main():
    # 获取当前时间
    now = datetime.now()

    # 判断当前时间是否是工作日
    if is_workday(now):
        if is_six(now):
            print("18点了，不要再当牛马了！")
        else:
            print("今天工作，努力上班！")
            # 遍历并打印每个软件的路径，如果是工作日则尝试打开
            software_paths = read_software_paths('soft.properties')
            # 遍历并打印每个软件的路径
            for path in software_paths:
                try:
                    subprocess.Popen(path, shell=True)  # 注意：shell=True 可能会带来安全风险
                    print(path + "  程序启动成功！")
                except Exception as e:
                    print(f"Failed to open {path}: {e}")
    else:
        print("今天周末，不当牛马！")

    time.sleep(3)
    sys.exit()


if __name__ == '__main__':
    main()
