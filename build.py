import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")


# remove things and define editables
run("conan remove 'test*' -c")

# run('conan editable add alpha')
run('conan build --profile:all ./profiles/clang-linux alpha --build=missing')
run('conan export-pkg --profile:all ./profiles/clang-linux alpha --no-remote')
run('conan build --profile:all ./profiles/clang-linux beta --no-remote')
run('cmake --install ./beta/build/linux-clang/Release --prefix Release/')
# run('conan build --profile:all ./profiles/clang-windows alpha --build=missing')
# run('conan build --profile:all ./profiles/clang-windows beta --build=missing')