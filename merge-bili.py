"""
合并 Neat Download Manager 下载文件
需要安装 ffmpeg ，设置环境变量

指定合并目录，默认当前目录

fix:
名字中含有空格引起输出错误,增加双引号
"""

import os
from datetime import datetime


# 生成合并文件夹名
def get_merged_folder():
    merged_dir_name = "merged-bili-" + datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
    return merged_dir_name


def create_folder(dirName):
    if not os.path.exists(dirName):
        os.mkdir(dirName)


def ffmpeg_cmd(file_name: str, file_path: str, merged_dir: str):
    # eg: D:\DownloadNeat\a/b/c/d
    # print(file_path)

    # 严格匹配，减少错误概率
    match_str = "_哔哩哔哩_bilibili(1)"
    anthor_str = "_哔哩哔哩_bilibili"

    # 对另外一种格式进行处理
    if "_哔哩哔哩bilibili(1)" in file_name:
        match_str = "_哔哩哔哩bilibili(1)"
        anthor_str = "_哔哩哔哩bilibili"

    if match_str in file_name:
        create_folder(merged_dir)
        merged_file_name = file_name.replace(match_str, "")
        anthor_file_name = file_name.replace(match_str, anthor_str)
        video_absolute_path_one = os.path.join(file_path, file_name)
        video_absolute_path_anthor = os.path.join(file_path, anthor_file_name)
        # ffmpeg -i video.m4s -i audio.m4s -codec copy Output.mp4
        # ffmpeg -i "D:\DownloadNeat\a/b/c/d\测试_哔哩哔哩_bilibili(1).mp4" -i "D:\DownloadNeat\a/b/c/d\测试_哔哩哔哩_bilibili.mp4" -codec copy "./merged-bili-2023-05-12-14-36-14/测试.mp4"
        cmd = "ffmpeg -i \"" + video_absolute_path_one + "\" -i \"" + video_absolute_path_anthor + "\" -codec copy \"./" + merged_dir + "/" + merged_file_name + "\""
        # print("----------------------- cmd alpha -----------------------")
        # print(cmd)
        # print("----------------------- cmd omega -----------------------")
        print("----------------------- alpha -----------------------")
        os.system(cmd)
        print("----------------------- omega -----------------------")


# 通过在目录树中游走输出在目录中的文件名，向上或者向下。
def merge_video_depth_all(need_merge_dir=os.getcwd()):
    merged_dir = get_merged_folder()
    for current_dir, current_sub_dir, current_file_list in os.walk(need_merge_dir):
        # print("current_file_list", current_file_list)
        for name in current_file_list:
            # print("current_dir", current_dir)
            # print("current_sub_dir", current_sub_dir)
            # print("name", name)
            ffmpeg_cmd(name, current_dir, merged_dir)


# merge_video_depth_all()


# 指定的文件夹包含的文件或文件夹的名字的列表
# eg: merge_video_depth_one(os.path.join(os.getcwd(), "a/b/c/d"))
def merge_video_depth_one(need_merge_dir=os.getcwd()):
    merged_dir = get_merged_folder()
    for name in os.listdir(need_merge_dir):
        absolute_file_path = os.path.join(need_merge_dir, name)
        if os.path.isfile(absolute_file_path):
            ffmpeg_cmd(name, need_merge_dir, merged_dir)


merge_video_depth_one()
