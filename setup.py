from setuptools import setup, find_packages

setup(
    name='django-fakegen',
    version='3.3.3',
    description='A Django app for generating fake data using Faker.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Mezo',
    author_email='motazfawzy73@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2',
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