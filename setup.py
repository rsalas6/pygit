from setuptools import setup, find_packages

setup(
    name="pygit",
    version="0.1.0",
    description="A simplified version of Git implemented in Python",
    author="Roberto Salas Hernández",
    author_email="hi@beto.page",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pygit=pygit.main:main',
        ],
    },
    install_requires=[
        # Lista de dependencias
    ],
    tests_require=[
        'pytest',
    ],
)
