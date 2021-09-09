import sys
import subprocess

compiler_ver = "0.1"

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

python_ver = "3";

if len(sys.argv) < 2:
	eprint("usage: " + sys.argv[0] + " input.py outfile")
	exit()

ifile = sys.argv[1]
ofile = sys.argv[2]

if len(sys.argv) > 3:
	python_ver = sys.argv[3]

versons = {
	"3"     : "python3",
	"3.9"   : "python3.9",
	"2"     : "python2"
}

if not (python_ver in versons) :
	eprint("version : " + python_ver + " is not supported")
	exit()

command = "/bin/env " + versons[python_ver]

with open(ofile,"wb") as fdout:
	with open(ifile,"rb") as fdin:
		fdout.write(bytes("#!" + command + "\n", 'utf-8'))
		fdout.write(fdin.read())
		fdout.write(bytes("\n# compiled with " + compiler_ver + " python compiler", 'utf-8'))

subprocess.run(["chmod", "a+x", ofile])

exit()
