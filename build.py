import os
import platform
import shutil

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")

# remove things and define editables
run("conan remove test*/* -c")
run("conan editable remove --refs test*")
run("conan editable add alpha")

shutil.rmtree(os.path.join("alpha", "build"), ignore_errors=True)
shutil.rmtree(os.path.join("beta", "build"), ignore_errors=True)
try:
    os.remove(os.path.join("alpha", "CMakeUserPresets.json"))
except FileNotFoundError as e:
    pass
try:
    os.remove(os.path.join("beta", "CMakeUserPresets.json"))
except FileNotFoundError as e:
    pass

if platform.system() == "Windows":
    run(f"conan build --profile:build msvc --profile:host Windows-x86_64-msvc-194 alpha --build=missing --remote conancenter")
    run(f"conan build --profile:build msvc --profile:host Windows-x86_64-msvc-194 beta --no-remote")
else:
    run(f"conan build --profile:build clang --profile:host Linux-x86_64-clang alpha --build=missing --remote conancenter")
    run(f"conan build --profile:build clang --profile:host Linux-x86_64-clang beta --no-remote")