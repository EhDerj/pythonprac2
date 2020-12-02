import sys
sys.stdout.write(sys.stdin.read().encode("latin", errors="replace").decode("CP1251", errors="replace"))