from setuptools import setup, find_packages

setup(
    name="calculadora-pacote",
    version="1.0.0",
    author="Mauroslucios",
    author_email="mauroslucios@gmail.com",
    description="Um pacote de calculadora simples para operações básicas",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mauroslucios/pacote_python",  # Adicione o link para seu repositório
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
