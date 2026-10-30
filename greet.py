#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Disposable greeting CLI')
parser.add_argument('name')
args = parser.parse_args()
print(f'Hello, {args.name}!')
