#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Disposable greeting CLI')
parser.add_argument('name')
parser.add_argument('--farewell', action='store_true', help='Say goodbye instead of hello')
args = parser.parse_args()
greeting = 'Goodbye' if args.farewell else 'Hello'
print(f'{greeting}, {args.name}!')
