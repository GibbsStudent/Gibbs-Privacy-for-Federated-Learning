import subprocess
from pkg_resources import get_distribution, VersionConflict
from pip._internal import main as pip_main

packages = [
    "numpy",
    "matplotlib",
    "scipy",
    "joblib",
    "tqdm",
    "json"
]

def get_installed_version(package_name):
    try:
        return get_distribution(package_name).version
    except VersionConflict:
        return None

def install_package(package_name, version):
    pip_main(["install", f"{package_name}=={version}"])

if __name__ == "__main__":
    for package_name in packages:
        installed_version = get_installed_version(package_name)
        if installed_version is not None:
            print(f"{package_name} is already installed (Version {installed_version})")
        else:
            print(f"{package_name} is not installed.")
            desired_version = input(f"Enter the desired version for {package_name}: ")
            install_package(package_name, desired_version)
            print(f"{package_name} (Version {desired_version}) has been installed.")
