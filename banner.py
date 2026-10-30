#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Disposable welcome banner CLI')
parser.add_argument('name')
args = parser.parse_args()
print(f'WELCOME, {args.name.upper()}!')
