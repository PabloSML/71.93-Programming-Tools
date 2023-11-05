#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple Python Script with GitPython

This script demonstrates basic file manipulation and Git commands
using the GitPython library.

Usage: ./bash_like.py
"""

import os
from git import Repo

def create_directory(directory_name):
    """
    Create a new directory if it doesn't exist.
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")

def write_to_file(file_name, content):
    """
    Write content to a file.
    """
    with open(file_name, 'w') as file:
        file.write(content)
        print(f"Content written to '{file_name}'.")

def git_init():
    """
    Initialize a Git repository.
    """
    repo = Repo.init()
    print("Git repository initialized.")

def git_add_commit(file_name, commit_message):
    """
    Add a file to the Git repository and commit changes.
    """
    repo = Repo(".")
    repo.index.add([file_name])
    repo.index.commit(commit_message)
    print(f"Changes committed with message: '{commit_message}'.")

if __name__ == "__main__":
    # Example usage
    create_directory("my_project")
    os.chdir("my_project")

    write_to_file("example.txt", "Hello, this is an example file.")

    git_init()
    git_add_commit("example.txt", "Initial commit")
