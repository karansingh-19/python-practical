
import numpy as np

# ---------- Encoding scheme: space = 0, A = 1, B = 2, ..., Z = 26 ----------
def text_to_numbers(text):
    return [0 if ch == " " else ord(ch) - 64 for ch in text.upper()]

def numbers_to_text(nums):
    return "".join(" " if n == 0 else chr(int(n) + 64) for n in nums)

# ---------- Encoding matrix (must be non-singular with det = +-1) ----------
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])
n = A.shape[0]

det_A = round(np.linalg.det(A))
print("Encoding matrix A:\n", A)
print("det(A) =", det_A)
assert det_A in (1, -1), "A must have det = +-1 so that the inverse has integer entries"

A_inv = np.round(np.linalg.inv(A)).astype(int)
print("Decoding matrix A^-1:\n", A_inv)
print("A x A^-1 = I ?", np.array_equal(A @ A_inv, np.eye(n, dtype=int)))

# ---------- Encoding ----------
message = "LINEAR ALGEBRA IS FUN"
print("\nOriginal message:", message)

nums = text_to_numbers(message)
print("Numeric form:", nums)

pad = (-len(nums)) % n                       # pad with spaces (0) to fill the last column
nums += [0] * pad

M = np.array(nums).reshape(-1, n).T          # each column = n consecutive characters
print("Message matrix M:\n", M)

E = A @ M                                    # encoded matrix
print("Encoded matrix E = A.M:\n", E)

coded = E.T.flatten()                        # read column by column
print("Coded message to send:", list(coded))

# ---------- Decoding ----------
received = np.array(coded).reshape(-1, n).T  # rebuild the matrix from the received numbers
D = A_inv @ received                         # decoded matrix = A^-1 . E
print("\nDecoded matrix A^-1.E:\n", D)

decoded_nums = D.T.flatten()
decoded_text = numbers_to_text(decoded_nums).rstrip()
print("Decoded numbers:", list(decoded_nums))
print("Decoded message:", decoded_text)
print("Decoded = Original ?", decoded_text == message)