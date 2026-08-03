import sys
import os

if __name__ == '__main__':
    # fallback: CI checkout may not fetch tags, then git describe fails
    version = '3.3.1'
    p = os.popen('git rev-list --tags --max-count=1')
    commit = p.read()
    p.close()

    if commit:
        p = os.popen('git describe --tags ' + commit)
        tag = p.read()
        p.close()
        if tag:
            version = str(tag[1:])

    # print('get version:', version)

    version_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../QtScrcpy/appversion"))
    file=open(version_file, 'w')
    file.write(version)
    file.close()
    sys.exit(0)