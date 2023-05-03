import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")


# normal creation works
#run("conan create Test/alpha --build=missing")
#run("conan create Test/beta --build=missing")

# rmove things and define editables
#run("conan remove * -c")
run("conan editable add Test/alpha")
run("conan build Test/alpha --build=missing")
run("conan build Test/beta")
