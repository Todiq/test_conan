import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")


# remove things and define editables
# run("conan remove * -c")

run('conan editable add alpha')
run('conan build alpha --build=missing --profile:all msvc')
run('conan build beta --build=missing --profile:all msvc')