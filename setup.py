import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quick-viz",
    version="0.3.5",
    install_requires=["pandas>=1.3.0", "pygwalker==0.1.4.8"],
    author="t.ibi, y.yuji, y.wada",
    author_email="t.ibi@estyle-inc.jp",
    description="Vizualize CSV quickly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Taichi-Ibi/quick-viz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["qviz = qviz.qviz:main"]},
    python_requires=">=3.8",
)
