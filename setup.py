from setuptools import setup

setup(
    name='strat_tools',
    version='0.1',
    python_requires='>=2.7',
    package_dir={'strat_tools': 'strat_tools'},
    entry_points = {
        "console_scripts": ['stack-section = strat_tools.__main__:cli']
    },
    install_requires=['click','pillow', 'wand']
)
