'''
Write a few lines of code to copy a le into another le using shutil.copyleobj(fsrc, fdst[, length])
and shutil.copyle(src, dst, *, follow_symlinks=True). Observe the dierence.
'''
import shutil
source = r"C:\Python\classwork\lab 24\question2.py"
destination = r"C:\Python\classwork\lab 24\question3.py"
des = shutil.copyfile(source, destination)
print(des)
