from setuptools import setup, find_packages


setup(
    name="task-tracker",
    version="0.1.0",
    author="Sam Rho",
    author_email="seungnam2@gmail.com",
    description="A simple task tracker for personal use.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'task-cli = main:main',
        ],
    },
)
