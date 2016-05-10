#!/usr/local/bin/python


def fun(dirpath, numfiles):
    from os import listdir
    from os.path import isfile, join
    from mymodule import helper

    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

    print("I found %d files, and you asked for %d files" %
          (len(files), numfiles))

    print("Calling module functions:")
    helper.hfunction()


if __name__ == "__main__":
    import sys
    fun(sys.argv[1], int(sys.argv[2]))
