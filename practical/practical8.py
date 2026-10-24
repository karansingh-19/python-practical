
import sympy as sp

# ---------- Helper: check linear dependence ----------
def check_dependence(vectors):
    M = sp.Matrix.hstack(*vectors)           # vectors as columns
    k = len(vectors)
    rank = M.rank()
    print("Matrix (vectors as columns):", M)
    print("rank =", rank, ", number of vectors =", k)
    if rank == k:
        print("Result: Linearly INDEPENDENT")
    else:
        c = M.nullspace()[0]                 # solution of c1*v1 + c2*v2 + ... = 0
        print("Result: Linearly DEPENDENT")
        print("Non-trivial coefficients (c1, c2, ...):", c.T)

# Flatten a matrix into a column vector so matrices can be treated like vectors
flat = lambda X: X.reshape(X.rows * X.cols, 1)


# ================= PART 1: Linear dependence =================
print("=== 1(a) Dependent vectors in R^3 ===")
v1 = sp.Matrix([1, 2, 3])
v2 = sp.Matrix([2, 1, 0])
v3 = sp.Matrix([4, 5, 6])                    # v3 = 2*v1 + v2
check_dependence([v1, v2, v3])

print("\n=== 1(b) Independent vectors in R^3 ===")
w1 = sp.Matrix([1, 0, 0])
w2 = sp.Matrix([1, 1, 0])
w3 = sp.Matrix([1, 1, 1])
check_dependence([w1, w2, w3])

print("\n=== 1(c) Dependent matrices of size 2x2 ===")
B1 = sp.Matrix([[1, 0], [0, 1]])
B2 = sp.Matrix([[0, 1], [1, 0]])
B3 = sp.Matrix([[1, 1], [1, 1]])             # B3 = B1 + B2
check_dependence([flat(B1), flat(B2), flat(B3)])


# ================= PART 2: Linear combinations =================
print("\n=== 2(a) Linear combination of vectors in R^3 ===")
u = sp.Matrix([1, 2, 3])
v = sp.Matrix([0, 1, 4])
w = sp.Matrix([2, -1, 1])
a, b, c = 2, -1, 3
result = a * u + b * v + c * w
print(f"{a}*u + ({b})*v + {c}*w =", result)

def is_combination(vectors, target):
    M = sp.Matrix.hstack(*vectors)
    aug = M.row_join(target)
    if M.rank() == aug.rank():
        print("Yes, target is a linear combination. Coefficients:", sp.linsolve((M, target)))
    else:
        print("No, target is NOT a linear combination of the given vectors")

print("\nIs (8, 0, 5) a combination of u, v, w?")
is_combination([u, v, w], sp.Matrix([8, 0, 5]))
print("Is (1, 0, 0) a combination of v1, v2, v3 (from 1a)?")
is_combination([v1, v2, v3], sp.Matrix([1, 0, 0]))

print("\n=== 2(b) Linear combination of 2x2 matrices ===")
A1 = sp.Matrix([[1, 2], [3, 4]])
A2 = sp.Matrix([[0, 1], [1, 0]])
A3 = sp.Matrix([[1, 0], [0, 1]])
comb = 2 * A1 - 1 * A2 + 3 * A3
print("2*A1 - A2 + 3*A3 =", comb)


# ================= PART 3: Transition matrix (matrix space M2(R)) =================
print("\n=== 3. Transition matrix in the space of 2x2 matrices ===")
# Basis B
basis_B = [sp.Matrix([[1, 0], [0, 0]]),
           sp.Matrix([[1, 1], [0, 0]]),
           sp.Matrix([[1, 1], [1, 0]]),
           sp.Matrix([[1, 1], [1, 1]])]
# Basis C
basis_C = [sp.Matrix([[1, 0], [0, 1]]),
           sp.Matrix([[0, 1], [1, 0]]),
           sp.Matrix([[1, 0], [0, -1]]),
           sp.Matrix([[0, 1], [-1, 0]])]

B_mat = sp.Matrix.hstack(*[flat(X) for X in basis_B])   # columns = basis B (in standard coordinates)
C_mat = sp.Matrix.hstack(*[flat(X) for X in basis_C])

print("Both are bases (invertible)?:", B_mat.det() != 0 and C_mat.det() != 0)

P_S_to_B = B_mat.inv()                    # standard basis -> B
P_B_to_C = C_mat.inv() * B_mat            # B -> C
P_C_to_B = P_B_to_C.inv()                 # C -> B

print("B matrix (standard coordinates):", B_mat)
print("Transition matrix P (Standard -> B):", P_S_to_B)
print("Transition matrix P (B -> C):", P_B_to_C)
print("P(B->C) * P(C->B) = I ?", P_B_to_C * P_C_to_B == sp.eye(4))

# Coordinates of a matrix X in each basis
X = sp.Matrix([[2, 3], [4, 5]])
X_B = P_S_to_B * flat(X)
X_C = P_B_to_C * X_B
print("\nMatrix X =", X)
print("Coordinates [X]_B =", X_B)
print("Coordinates [X]_C = P(B->C) * [X]_B =", X_C)

recon = sum((X_B[i] * basis_B[i] for i in range(4)), sp.zeros(2, 2))
print("Reconstruct X from B-coordinates:", recon == X)