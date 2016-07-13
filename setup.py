
from setuptools import setup, find_packages

def long_description():
    # with codecs.open('README.rst', encoding='utf8') as f:
    #     return f.read()

setup(
    name='subtitle_joiner',
    version=joiner.__version__,
    description=joiner.__doc__.strip,
    long_description=long_description(),
    url='https://github.com/TreyCai/SubtitleJoiner/issues',
    download_url='https://github.com/TreyCai/SubtitleJoiner/issues',
    author=joiner.__author__,
    author_email='imtreywalker@gmail.com',
    license=joiner.__license__,
    packages=find_packages(),
    entry_points={
        'console_scripts': {
            'joiner = joiner.__main__.main'
        }
    },
    extras_requires=[],
    install_requires=[],
    classifiers=[
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License, Version 2.0',
        'Operating System :: MacOS :: MacOS X',
        # 'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Terminals',
        'Topic :: Image Processing',
        'Topic :: Utilities'
    ]
)
