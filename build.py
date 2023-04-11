import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")


run("conan create Test/alpha --build=missing")