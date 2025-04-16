from setuptools import setup, find_packages

setup(
    name="webgen",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "pynput",
        "colorama",
        "questionary"
    ],
    entry_points={
        "console_scripts": [
            "webgen=webgen:main",
        ],
    },
)
