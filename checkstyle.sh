#!/bin/sh

# Scripts to enforce certain code style rules.

# DoubleQuotesOnly; forbid usage of single-quoted Strings throughout the project
if grep -n \'.*\' ./timeless/*/*.py; then
    echo "Single-quotes are forbidden in .py files!"
    grep -n \'.*\' ./timeless/*/*.py
    exit 2;
fi