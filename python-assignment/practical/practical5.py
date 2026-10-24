
import numpy as np

# ---------- Gauss-Jordan elimination (reduces to RREF) ----------
def gauss_jordan(A):
    A = np.array(A, dtype=float)
    n, m = A.shape
    M = np.hstack((A, np.zeros((n, 1))))     # augmented matrix [A | 0]
    r = 0                                    # current pivot row
    pivots = []
    for c in range(m):
        if r >= n:
            break
        p = np.argmax(np.abs(M[r:, c])) + r  # partial pivoting
        if np.isclose(M[p, c], 0):
            continue                         # no pivot in this column
        M[[r, p]] = M[[p, r]]                # swap rows
        M[r] = M[r] / M[r, c]                # make pivot = 1
        for i in range(n):                   # eliminate above AND below pivot
            if i != r:
                M[i] = M[i] - M[i, c] * M[r]
        pivots.append(c)
        r += 1
    M = np.round(M, 6)
    M[np.isclose(M, 0)] = 0                  # clean tiny values / -0
    return M, pivots


def solve_homogeneous(A):
    A = np.array(A, dtype=float)
    n = A.shape[1]                           # number of unknowns
    M, pivots = gauss_jordan(A)
    rank = len(pivots)
    print("RREF of [A|0]:\n", M)
    print("rank(A) =", rank, ", number of unknowns =", n)

    if rank == n:
        print("Result: Only the trivial solution x =", np.zeros(n))
    else:
        free = [c for c in range(n) if c not in pivots]
        print("Result: Non-trivial solutions exist")
        print("Pivot variables:", [f"x{c+1}" for c in pivots])
        print("Free variables :", [f"x{c+1}" for c in free])
        for k, f in enumerate(free, start=1):
            x = np.zeros(n)
            x[f] = 1
            for i, pc in enumerate(pivots):
                x[pc] = -M[i, f] + 0.0
            print(f"Basis vector {k}:", x)
        print("General solution = linear combination of the basis vectors")


# ---------- 1. Non-trivial solution (rank < n) ----------
print("=== System 1: x+y+z=0, 2x+3y+z=0, 3x+4y+2z=0 ===")
A1 = [[1, 1, 1],
      [2, 3, 1],
      [3, 4, 2]]
solve_homogeneous(A1)

# ---------- 2. Only trivial solution (rank = n) ----------
print("\n=== System 2: x+2y+z=0, 2x+y+z=0, x+y+2z=0 ===")
A2 = [[1, 2, 1],
      [2, 1, 1],
      [1, 1, 2]]
solve_homogeneous(A2)

# ---------- 3. More unknowns than equations (two free variables) ----------
print("\n=== System 3: 3 equations, 4 unknowns ===")
A3 = [[1, 2, -1, 3],
      [2, 4, 1, 0],
      [1, 2, 2, -3]]
solve_homogeneous(A3)