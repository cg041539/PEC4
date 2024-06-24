from setuptools import setup, find_packages

setup(
    name="PEC4",
    version="0.1.0",
    author="Cristina Garcia Fernandez",
    author_email="cristina@ayer.be",
    description="Proyecto PEC4 para procesamiento y análisis de datos de verificaciones "
                "de antecedentes de armas de fuego.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cg041539/PEC4",
    packages=find_packages(where='src'),
    package_dir={'PEC4': 'src'},
    py_modules=['main'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=open('requirements.txt').read().splitlines(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pec4=main:main',
        ],
    },
)
sde requirements.txt
    include_package_data=True,  # Incluye archivos especificados en MANIFEST.in
    entry_points={  # Si tienes scripts ejecutables
        'console_scripts': [
            'pec4=main:main',  # Define el comando `pec4` que ejecutará la función `main` en `main.py`
        ],
    },
)
