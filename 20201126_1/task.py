import sys

N = sys.stdin.buffer.read(1)
sys.stdout.buffer.write(N)
N = N[0]
text = sys.stdin.buffer.read()
L = len(text)
sys.stdout.buffer.write(b"".join(sorted((text[i*L//N:(i+1)*L//N] for i in range(N)))))