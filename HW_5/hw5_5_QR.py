import numpy as np

# Polynomial COefficients
a3 = 24
a2 = 4500
a1 = 18000
a0 = 2.25e6

# Companion Matrix
C = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [-a0, -a1, -a2, -a3]
])

# Eigenvalues Calculation
roots = np.linalg.eigvals(C) # QR -> RQ -> QR -> ...

# Result
print("Eigenvalues:")
for r in sorted(roots, key=lambda z: z.real):
    print(f"w = {r.real:.4f} {'+' if r.imag >= 0 else '-'} {abs(r.imag):.4f}i")
