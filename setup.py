from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name='rect',
    packages=['rect'],
    ext_modules=cythonize(Extension(
        'Rectangle',
        sources=['rect/wrapper.pyx', 'src/Rectangle.cpp'],
        include_dirs=['inc/'],
        language='c++',
        extra_compile_args=['--std=c++11'],
        extra_link_args=['--std=c++11']
    )),
)
