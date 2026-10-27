# IVV Agent

A small AI coding agent built while learning about LLMs and function calling through Boot.dev.

The agent takes a prompt, communicates with an LLM through OpenRouter, and can use tools to interact with a local Python project.

## What it does

- Lists files and directories.
- Reads and writes files.
- Runs Python scripts.
- Uses LLM function calling to decide which tools to execute.
- Supports verbose output for debugging.

## Running it

Install dependencies:

    uv sync

Set your OpenRouter API key in a `.env` file:

    OPENROUTER_API_KEY=your_key_here

Run the agent:

    uv run main.py "Explain what this code does"

Add `--verbose` to see more details.

## About

A guided Boot.dev project exploring AI agents, tool calling, and Python.

This is an experimental learning project, not a production-ready coding agent. It can execute code and modify files, so it should only be used in a controlled environment.
