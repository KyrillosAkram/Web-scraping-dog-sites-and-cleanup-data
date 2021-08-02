import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call(
    [sys.executable, '-m', 'pip', 'install', 'lxml','requests' ,'pyOpenSSL', 'beautifulsoup4', 'json5' ,'jsonschema'])