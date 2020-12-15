from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

msg_extension = Extension(
    name='msgheader',
    sources=["msgheader.pyx"],
    libraries=["msgheader", "protobuf"],
    library_dirs=["lib", "/usr/local/lib"],
    include_dirs=["lib", "/usr/local/include"],
    language="c++"
)

setup(
    name="lucid-message",
    version="0.0.1",
    packages=find_packages(),
    install_requires=['protobuf'],
    ext_modules=cythonize([msg_extension, "msg_header_pb2.py"],
                          language_level=3),
)
