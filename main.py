from sympy import *

A = [
    [Symbol('a00'), Symbol('a01'), Symbol('a02')],
    [Symbol('a10'), Symbol('a11'), Symbol('a12')],
    [Symbol('a20'), Symbol('a21'), Symbol('a22')],
    [Symbol('a30'), Symbol('a31'), Symbol('a32')]
]

L = [
    Symbol('L0'),
    Symbol('L1'),
    Symbol('L2'),
    Symbol('L3')
]

dPhiX = [
    4 * A[1][1] * L[1] - A[1][1],
    4 * A[2][1] * L[2] - A[2][1],
    4 * A[3][1] * L[3] - A[3][1],
    4 * (A[1][1] * L[2] + A[2][1] * L[1]),
    4 * (A[2][1] * L[3] + A[3][1] * L[2]),
    4 * (A[1][1] * L[3] + A[3][1] * L[1])
]

dPhiY = [
    4 * A[1][2] * L[1] - A[1][2],
    4 * A[2][2] * L[2] - A[2][2],
    4 * A[3][2] * L[3] - A[3][2],
    4 * (A[1][2] * L[2] + A[2][2] * L[1]),
    4 * (A[2][2] * L[3] + A[3][2] * L[2]),
    4 * (A[1][2] * L[3] + A[3][2] * L[1])
]

def main():
    print('dPhiX * dPhiX:')
    for i in range(6):
        for j in range(6):
            if (j < i):
                continue
            print(f"{i+1}{j+1}: {dPhiX[i] * dPhiX[j]}")
    
    print('\n\ndPhiY * dPhiY:')
    for i in range(6):
        for j in range(6):
            if (j < i):
                continue
            print(f"{i+1}{j+1}: {dPhiY[i] * dPhiY[j]}")
    
    print('\n\ndPhiX_i * dPhiX_j + dPhiY_i * dPhiY_j:')
    for i in range(6):
        for j in range(6):
            if (j < i):
                continue
            res = dPhiX[i] * dPhiX[j] + dPhiY[i] * dPhiY[j]
            res = expand(res)
            res = simplify(res)
            print(f"{i+1}{j+1}: {res}")
            
            
if __name__ == "__main__":
    main()