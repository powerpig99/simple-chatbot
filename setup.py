from setuptools import setup, find_packages

setup(
    name="simple_chatbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["nltk"],
    entry_points={
        "console_scripts": [
            "chatbot = chatbot.cli:run_chatbot"
        ]
    },
    author="Powerpig",
    description="A simple rule-based chatbot"
)