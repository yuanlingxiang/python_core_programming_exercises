#! usr/bin/env/python
# -*- coding:utf-8 -*-


from urllib import urlretrieve


def first_nonblank(lines):
    for each_line in lines:
        if not each_line.strip():
            continue
        else:
            return each_line


def first_last(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print first_nonblank(lines),
    lines.reverse()
    print first_nonblank(lines)


def download(url='http://www.baidu.com', process=first_last):
    try:
        retval = urlretrieve(url)
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)


if __name__ == '__main__':
    download()


