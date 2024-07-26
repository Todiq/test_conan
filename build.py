import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")


# remove things and define editables
run("conan remove 'test*' -c")

run('conan editable add alpha')
run('conan build --profile:all ./profiles/msvc alpha --build=missing')
run('conan build --profile:all ./profiles/msvc beta --no-remote')
run('cmake --install ./beta/build/windows-msvc/ --prefix Release/')
# run('conan build --profile:all ./profiles/clang-windows alpha --build=missing')
# run('conan build --profile:all ./profiles/clang-windows beta --build=missing')