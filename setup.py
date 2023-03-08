from setuptools import setup, find_packages

setup(
    name ='code-splunker',
    version ='1.0.0',
    description ='Search for code caves in a binary',
    url = 'https://github.com/Ajstroze/code-splunker',
    author = 'Ajstroze',
    author_email = "ajstroze@gmail.com",
    license = 'GNU General Public License v3 or later (GPLv3+)',

    classifiers=[
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'Topic :: System',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.11.2',
    ],

    keywords = 'Codecave',

    packages = find_packages(),

    #install_requires=[],

    #extras_require={},

    entry_points={
        'console_scripts': [
            'code_splunker=code_splunker.main:main',],
    }
)
