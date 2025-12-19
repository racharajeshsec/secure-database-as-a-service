# Toy OPE example (order preserved). Replace with a real library if you used one.

def ope_encrypt(weight: float) -> int:
    return int(weight * 100)

def ope_decrypt(enc: int) -> float:
    return enc / 100.0

def range_query(enc_weights, min_w: float, max_w: float):
    return [w for w in enc_weights if min_w <= ope_decrypt(w) <= max_w]
