import os
import pathlib
import platform

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")

profile = "./profiles/clang"

if platform.system() == "Windows":
    profile = "./profiles/msvc"

# remove things and define editables
run("conan remove 'test*' -c")

run('conan editable add alpha')

run(f"conan build --profile:all {profile} alpha --build=missing")
run(f"conan install --profile:all {profile} beta --no-remote")
# run('cmake --install ./beta/build/windows-msvc/ --prefix Release/')