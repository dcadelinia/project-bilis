from setuptools import setup, find_packages

setup(
    name="the-tinikling-method",
    version="1.2.0",
    author="The Tinikling Method Project Contributors",
    description="An AI-ready multi-sport rhythm agility and biomechanical analytics framework.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(where="."),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux", # Critical target for NVIDIA Jetson architectures
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.22.0",
        "pyyaml>=6.0",
        "opencv-python>=4.6.0.66"
    ],
)
