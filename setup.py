import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
__version__="0.0.0"
REPO_NAME="Pythonpackage"
AUTHOR_USER_NAME="harinaru"
SRC_REPO="IPYNBrenderer"
AUTHOR_EMAIL="harinainyarpillai@gmail.com"

setuptools.setup(
name=SRC_REPO,
version=__version__,
author=AUTHOR_USER_NAME,
author_email=AUTHOR_EMAIL,
description="A Small Python Package ",
long_description=long_description,
long_description_content="text/markdown",
url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
project_urls={
    "BUG TRACKER":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
},
package_dir={"":"src"},
packages=setuptools.setuptools.find_packages(where="src")




)