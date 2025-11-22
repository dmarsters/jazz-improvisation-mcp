from setuptools import setup, find_packages

setup(
    name="jazz-improvisation-mcp",
    version="0.1.0",
    description="Jazz improvisation structure MCP server - temporal revelation through established grammar",
    author="Dal",
    packages=find_packages(),
    install_requires=[
        "mcp>=0.1.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "jazz-improvisation-mcp=jazz_improvisation_mcp.server:run_server",
        ],
    },
)
