from setuptools import setup, find_packages

setup(
    name='computer',
    version='1.0.0',
    description='Perform calculations and comparisons from user input',
    url='https://github.com/despawnerer/computer',
    author='Aleksei Voronov',
    author_email='despawn@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
