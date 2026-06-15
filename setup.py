from setuptools import setup, find_packages

setup(
    name="noah-llm",
    version="1.0.0",
    description="NOAH LLM - Uncensored Local Transformer",
    author="NOAH LLM Team",
    packages=find_packages(),
    install_requires=[
        'flask>=2.0.0',
        'numpy>=1.20.0',
        'requests>=2.25.0',
        'python-dotenv>=0.19.0',
        'pillow>=8.0.0',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'noah-llm=maya_bpe:chat_with_noah',
        ]
    }
)