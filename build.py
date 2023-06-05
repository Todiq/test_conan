import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")

run("conan build .")
run("conan build . --conf tools.build:skip_test=False")
