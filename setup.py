from setuptools import setup

setup(
    name='cp-hec-api-sdk',
    version='1.0',
    author='Travis Lockman',
    license='Apache 2.0',
    description="Check Point HEC API SDK",
    url="https://github.com/travislockman/cp_hec_api_python_sdk",
    py_modules=['cphecv1'],
    install_requires=['requests']
)
