from setuptools import setup, find_packages

setup(
    name='django-fakegen',
    version='1.1.1',
    description='A Django package for generating fake data for your models.',
    author='Mezo',
    author_email='motazfawzy73@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
        'Faker',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
) 