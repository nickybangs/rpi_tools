from setuptools import find_packages, setup

version = "0.0.2"

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = ['rpi_tools']

setup(
    name='rpi_tools',
    version=version,
    description=(
        'Various tools for r-pi setup'
    ),
    long_description=readme,
    long_description_content_type='text/markdown',
    author='nicky bangs',
    author_email='nicky.bangs@gmail.com',
    data_files=[('', ['ftp.json'])],
    packages=find_packages(include=["rpi_tools", "rpi_tools.*"]),
    scripts=[
        'bin/send_note',
        'bin/send_file',
        'bin/get_notes',
        'bin/get_file',
    ],
    entry_points={
        'console_scripts': [
            'ftp_handler = rpi_tools.ftp_handler.__main__:main'
            ]
        },
    python_requires='>=3.9',
    install_requires=requirements,
)
