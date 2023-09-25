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
run('conan editable add Test/alpha')
run('conan build Test/alpha --build=missing  --conf "&:tools.build:skip_test=False"')
# run('conan test Test/alpha/test_package alpha/1.0 --conf "alpha/1.0:tools.build:skip_test=False"')
# run('conan build Test/beta --settings:build "alpha/1.0:build_type=Debug" --settings:host "alpha/1.0:build_type=Debug"')
