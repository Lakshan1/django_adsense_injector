from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='django_adsense_injector',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown'
)