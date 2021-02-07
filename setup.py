from setuptools import setup

try:
    import pypandoc
    description = pypandoc.convert(source='README.md', format='markdown_github', to='rst', outputfile='README.rst')
except (IOError, ImportError):
    description = open('README.md').read()


version = '0.1'

setup(
    name='shader',
    packages=['shader'],
    version=version,
    description='Shade nighttime of time-series',
    long_description=description,
    author='Justin Shenk',
    author_email='shenkjustin@gmail.com',
    url='https://github.com/justinshenk/shader',
    download_url='https://github.com/justinshenk/shader/archive/{}.tar.gz'.format(version),
    keywords=['plot', 'shade', 'nighttime', 'dark', 'time series'],
    license='MIT',
    classifiers=[ # look here https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',        
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'matplotlib', 'pandas'
    ],
    zip_safe=False,
)