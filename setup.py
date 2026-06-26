"""
Setup configuration for AI-AGENT
Enables pip installation and terminal command usage
"""

from setuptools import setup, find_packages
import os

# Read the README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="ai-agent",
    version="1.0.0",
    author="Joydip",
    author_email="",
    description="Professional Multilingual AI Chatbot supporting 40+ languages",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joydip-hub/AI-AGENT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Chat",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Natural Language :: Spanish",
        "Natural Language :: French",
        "Natural Language :: German",
        "Natural Language :: Hindi",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Japanese",
        "Natural Language :: Arabic",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "ai-agent=src.cli:main",
            "ai-agent-simple=src.cli:simple_main",
        ],
    },
    include_package_data=True,
    package_data={
        "src": ["*.py"],
        "config": ["*.yaml", "*.yml"],
    },
    keywords=[
        "ai", "chatbot", "multilingual", "nlp", "conversation",
        "language-detection", "artificial-intelligence", "cli",
        "hindi", "spanish", "french", "arabic", "chinese", "japanese"
    ],
    project_urls={
        "Bug Reports": "https://github.com/Joydip-hub/AI-AGENT/issues",
        "Source": "https://github.com/Joydip-hub/AI-AGENT",
        "Documentation": "https://github.com/Joydip-hub/AI-AGENT#readme",
    },
)
