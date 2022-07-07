# Spring time

Clustering and triggering code for the
[spring](https://github.com/mmalenta/spring) post-processing pipeline.
In July 2022, this project has been completely restarted as it
became apparent that the old codebase can no longer meet all the
requirements of the MeerTRAP project. The old version of the code
has been renamed to
[spring_time_legacy](https://github.com/mmalenta/spring_time_legacy).
It will be always available on GitHub, so feel free to use it, but it
will be no longer maintained. It is therefore important to use this
new repository for all the newest features, upgrades and bug fixes.

This repository will result in a completely overhauled
clustering and triggering code. It will also adhere to strict development
and coding standards (this README file being one of few examples)
to make the development and use of this software easier and more efficient.

## Installation

This pipeline is intended to be run on a Linux and is tested with this OS
in mind only. There is therefore no guarantee it will work on other operating
systems.

### Requirements

This requirements list if for an additional (human-readable) reference only.
It should always be up to date, but there is always a chance a new package
was missed. For a complete requirements list, please refer to the
[setup.cfg](setup.cfg) file.

Python 3.10 (and higher) is a critical requirement. This project is/will be
relying on features and packages available with this version of python only.
As is usually the case in Python world, it is possible to make it work with
the earlier versions, but we cannot guarantee anything or offer any help
in such a scenario.

```text
python==3.10
setuptools==61.2.0
```

## Licence

