
import numpy as np
import sympy as sp

# ---------- Check diagonalizability + eigenvalues/eigenvectors ----------
def analyse(A, name="A"):
    A = sp.Matrix(A)
    n = A.shape[0]
    print(f"Matrix {name}:", A)

    # Characteristic polynomial det(A - lambda*I)
    lam = sp.symbols('lambda')
    char_poly = A.charpoly(lam).as_expr()
    print("Characteristic polynomial:", sp.factor(char_poly))

    # Eigenvalues with algebraic multiplicity, and eigenvectors
    eigen = A.eigenvects()                   # (eigenvalue, algebraic mult., [eigenvectors])
    total_vectors = 0
    for val, alg_mult, vecs in eigen:
        geo_mult = len(vecs)
        total_vectors += geo_mult
        print(f"Eigenvalue {val}: algebraic mult = {alg_mult}, geometric mult = {geo_mult}")
        for v in vecs:
            print("   Eigenvector:", v.T)

    # Diagonalizable iff total independent eigenvectors = n
    if total_vectors == n:
        print("Result: A is DIAGONALIZABLE")
        P, D = A.diagonalize()               # A = P D P^-1
        print("P (eigenvectors as columns):", P)
        print("D (diagonal matrix of eigenvalues):", D)
        print("P^-1 * A * P = D ?", sp.simplify(P.inv() * A * P) == D)
    else:
        print("Result: A is NOT diagonalizable (not enough independent eigenvectors)")
    return char_poly, lam


# ---------- Verify Cayley-Hamilton: p(A) = 0 ----------
def cayley_hamilton(A):
    A = sp.Matrix(A)
    n = A.shape[0]
    lam = sp.symbols('lambda')
    p = sp.Poly(A.charpoly(lam).as_expr(), lam)
    coeffs = p.all_coeffs()                  # highest power first
    print("Characteristic equation: ", sp.Eq(p.as_expr(), 0))

    # Substitute A into the polynomial: c_n A^n + ... + c_1 A + c_0 I
    result = sp.zeros(n, n)
    for k, c in enumerate(reversed(coeffs)):
        result += c * A**k
    print("p(A) =", result)
    print("Cayley-Hamilton verified (p(A) = 0)?:", result == sp.zeros(n, n))

    # Use it to find the inverse: A^-1 = -(1/c0)(A^(n-1) + ... + c1 I)
    c0 = coeffs[-1]
    if c0 != 0:
        inv = sp.zeros(n, n)
        for k in range(1, n + 1):
            inv += coeffs[n - k] * A**(k - 1)
        inv = -inv / c0
        print("Inverse via Cayley-Hamilton:", inv)
        print("Matches A.inv()?:", inv == A.inv())


# ---------- 1. Diagonalizable matrix (distinct eigenvalues) ----------
print("=== 1. Diagonalizable matrix ===")
A1 = [[2, 0, 0],
      [1, 3, 0],
      [2, 1, 4]]
analyse(A1, "A1")
print()
cayley_hamilton(A1)

# ---------- 2. Diagonalizable matrix (repeated eigenvalue) ----------
print("\n=== 2. Diagonalizable with repeated eigenvalue ===")
A2 = [[2, 1, 1],
      [1, 2, 1],
      [1, 1, 2]]
analyse(A2, "A2")
print()
cayley_hamilton(A2)

# ---------- 3. Non-diagonalizable matrix ----------
print("\n=== 3. Non-diagonalizable matrix ===")
A3 = [[1, 1],
      [0, 1]]
analyse(A3, "A3")
print()
cayley_hamilton(A3)

# ---------- 4. Numerical check using NumPy ----------
print("\n=== 4. NumPy check for A2 ===")
vals, vecs = np.linalg.eig(np.array(A2, dtype=float))
print("Eigenvalues:", np.round(vals, 6))
print("Eigenvectors (columns):\n", np.round(vecs, 6))