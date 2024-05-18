from setuptools import setup, find_packages

setup(
    name='KeyboardChatteringFix-Linux',
    version='0.1.0',
    description='A tool for filtering mechanical keyboard chattering on Linux.',
    author='w2sv',
    url='https://github.com/w2sv/KeyboardChatteringFix-Linux',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'libevdev~=0.11'
    ],
    entry_points={
        'console_scripts': [
            'chattering_fix = src.__main__:main'
        ]
    }
)