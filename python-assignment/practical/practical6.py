
import sympy as sp

# ---------- Matrix ----------
A = sp.Matrix([[1, 2, 3, 4],
               [2, 4, 7, 8],
               [3, 6, 10, 12]])

m, n = A.shape
rref_A, pivots = A.rref()
rank = len(pivots)

print("Matrix A:", A)
print("Size:", m, "x", n)
print("RREF of A:", rref_A)
print("Pivot columns:", pivots)
print("Rank =", rank)

# ---------- 1. Column space C(A): pivot columns of the ORIGINAL matrix ----------
col_basis = A.columnspace()
print("\n--- Basis of Column Space C(A) ---")
for k, v in enumerate(col_basis, start=1):
    print(f"Vector {k}:", v.T)
print("Dimension =", len(col_basis))

# ---------- 2. Row space R(A): non-zero rows of the RREF ----------
row_basis = [rref_A[i, :] for i in range(rank)]
print("\n--- Basis of Row Space R(A) ---")
for k, v in enumerate(row_basis, start=1):
    print(f"Vector {k}:", v)
print("Dimension =", len(row_basis))

# ---------- 3. Null space N(A): solutions of AX = 0 ----------
null_basis = A.nullspace()
print("\n--- Basis of Null Space N(A) ---")
for k, v in enumerate(null_basis, start=1):
    print(f"Vector {k}:", v.T)
print("Dimension (nullity) =", len(null_basis))

# ---------- 4. Left null space N(A^T): solutions of A^T Y = 0 ----------
left_basis = A.T.nullspace()
print("\n--- Basis of Left Null Space N(A^T) ---")
for k, v in enumerate(left_basis, start=1):
    print(f"Vector {k}:", v.T)
print("Dimension =", len(left_basis))

# ---------- Verification ----------
print("\n--- Verification ---")
print("rank + nullity = n :", rank, "+", len(null_basis), "=", rank + len(null_basis))
print("rank + left nullity = m :", rank, "+", len(left_basis), "=", rank + len(left_basis))
print("A * (null space vectors) = 0 :", all((A * v).is_zero_matrix for v in null_basis))
print("(left null vectors)^T * A = 0 :", all((v.T * A).is_zero_matrix for v in left_basis))
print("Row space is orthogonal to null space :",
      all((r * v)[0] == 0 for r in row_basis for v in null_basis))