from setuptools import setup, find_packages

setup(
    name="cpu_scheduler_simulator",
    version="0.1",
    description="CPU scheduler simulator project",
    license="MIT",
    packages=find_packages(include=["core.common", "core.schedulers", "core"]),
    python_requires=">=3.12.2",
    install_requires=["matplotlib>=3.0", "tk-tools"],
    extras_require={
        "test": ["pytest>=7.0", "setuptools"]
    },
    test_suite="pytest",
)
