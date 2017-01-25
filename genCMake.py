import os


cwd = os.getcwd()
cmakePath = os.path.join(cwd, 'CMakeLists.txt')
cmake = open(cmakePath, 'w')
cmake.write('cmake_minimum_required (VERSION 2.6)\n')
cmake.write('project (DaHuaDS)\n')


# 遍历根目录
dirs = os.listdir(cwd)
for dir in dirs:
    path = os.path.join(cwd, dir)

    if os.path.isdir(path) and 'c0' in path:
        codeFolderName = os.path.basename(path)

        cmake.write('\n')
        cmake.write('# %s\n' % (codeFolderName))

        # 遍历 c0x_xxxx 代码目录
        files = os.listdir(path)
        for file in files:
            filePath = os.path.join(path, file)

            ext = os.path.splitext(filePath)[1]
            if ext == '.c':
                codeFileName = os.path.splitext(os.path.basename(filePath))[0]
                cmake.write('add_executable(%s_%s %s/%s.c)\n' % (codeFolderName, codeFileName, codeFolderName, codeFileName))

cmake.close()
