from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    print ("D:")
    pprint (D)
    R = A - diagflat(D)
    print ("R:")
    pprint (R)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([[6.0,3.0,1.0],[4.0,9.0,-3.0],[1.0,-1.0,3.0]])
b = array([10.0,16.0,14.0])
guess = array([1.0,1.0,1.0])

sol = jacobi(A,b,N=25,x=guess)

print ("A:")
pprint(A)

print ("b:")
pprint(b)

print ("x:")
pprint(sol)