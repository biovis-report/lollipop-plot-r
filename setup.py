from setuptools import setup, find_packages
from lollipop_plot.version import get_version


setup(
    name='lollipop-plot-r',
    version=get_version(),
    description='An biovis plugin to draw an interactive lollipop plot.',
    long_description='The lollipop plot plugin will draw an interactive lollipop plot by using shiny and maftools library.',
    keywords='biovis-plugin, lollipop-plot, interactive',
    url='https://github.com/biovis-report/lollipop-plot-r',
    author='Jingcheng Yang',
    author_email='yjcyxky@163.com',
    license='MIT',
    python_requires='>=3.4',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'biovis.plugins': [
            'lollipop-plot-r = lollipop_plot.lollipop_plot:LollipopPlotRPlugin'
        ]
    }
)
