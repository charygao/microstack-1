from setuptools import setup, find_packages

setup(
    name="microstack_wait",
    description="Wait for the snap to be initialized.",
    packages=find_packages(exclude=("tests",)),
    version="0.0.1",
    entry_points={
        'console_scripts': [
            'microstack_wait = wait.main:main',
        ],
    },
)
