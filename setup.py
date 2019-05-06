from setuptools import setup
from setuptools import find_packages

setup(
        name='ivis_animate',
        version='0.0.1',
        description='ivis animation package',
        url='http://github.com/beringresearch.com/ivis-animate',
        author='Ignat Drozdov',
        author_email='idrozdov@beringresearch.com',
        license='Creative Commons Attribution-NonCommercial-NoDerivs 3.0',
        packages=find_packages(),
        install_requires=[
            'ivis',
            'numpy',
            'celluloid',
            'matplotlib'],
        zip_safe=False)
