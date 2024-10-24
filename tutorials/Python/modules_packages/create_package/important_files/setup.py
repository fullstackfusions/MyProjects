# approach-1 using setup.cfg
from setuptools import setup

if __name__ == "__main__":
    setup()


# or Approach-2 without setup.cfg

from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package_name',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.2',  # Specify your project's dependencies here
        'requests>=2.24.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Change as appropriate
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Change the license as needed
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='sample setuptools development',  # Add some keywords relevant to your project
    python_requires='>=3.6',
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'your_script=your_package.module:function',
        ],
    },
)
