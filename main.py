#!/usr/bin/env python

import os
import shutil

from json_reading import get_dirs_of_responses_list_format_from_json

def delete_everything_in_path(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

def create_files_andor_dirs_in_path(list, path):
    copy_list = list.copy()

    # split file (.json) from dir
    for index, dir in enumerate(copy_list):
        dir = dir.rsplit('/', 1)
        copy_list[index]=dir

    '''eg:
        copy_list = [['file1.json'], ['folder2', 'file2.json'], ['folder4/folder5', 'file3.json']]
        group = ['file1.json']
        group = ['folder2', 'file2.json']
        group = ['folder4/folder5', 'file3.json']'''
    for group in copy_list:
        # eg: group = "file1.json"
        if len(group)==1:
            # create file in path
            os.chdir(path)
            try:
                open(group[0],"x")
                print("len 1")
            except FileExistsError:
                print(f"{path}\{group[0]} existing file. Didn't overwrite it")

        '''eg: group = [["folder2"],["file2.json"]]
            or 
            group = [["folder4/folder5"],["file3.json"]]'''
        if len(group)>1:
            # create dirs, source : group[0]
            # split group[0] by "/"
            group[0] = group[0].split("/")
            # foreach element create folder
            subpath = path
            for index, subgroup in enumerate(group[0]):
                os.chdir(subpath)
                try:
                    os.makedirs(subgroup)
                except FileExistsError:
                    print(f"{subgroup} existing folder. Didn't override it. Continuing to subfolder/next folder")
                subpath = f'{subpath}\\{subgroup}'
            # create file, source : group[-1]
            os.chdir(subpath)
            try:
                open(group[1], "x")
                print(f"just created {subpath}/{group[1]}")
            except FileExistsError:
                print(f"{subpath}\{group[1]} existing file. Didn't overwrite it")
            subpath = ""
            pass

json_file_path = "C:\\Users\\aymane.dassouli\\Desktop\\mission\\PCE\\client\\cypress\\fixtures\\url-apiCalls.json"
list = get_dirs_of_responses_list_format_from_json(json_file_path)
path = 'C:\\Users\\aymane.dassouli\\Desktop\\mission\\PCE\\client\\cypress\\fixtures\\responses'

create = int(input("create : 1 \n or\ndelete : 0\n or\nredo : 2\n"))
delete = not create
redo = 2 if create == 2 else 0

if delete == 1 or redo == 2:
    delete_everything_in_path(path)

if create == 1 or redo == 2:
    create_files_andor_dirs_in_path(list, path)

# refactor create... function
    # print(copy_list)
    # files = []
    # dirs = []
    # for group in copy_list:
    #     files.append(group[-1])
    #     if len(group) == 1 :
    #         dirs.append('')
    #     if len(group) == 2 :
    #         print(group[0])
    #         group[0] = group[0].split('/')
    #         dirs.append(group[0])

# print(dirs)
# print(files)
# print("\n")
# for i in range(len(dirs)):
#     print(f'"{dirs[i]}" : {files[i]}')
