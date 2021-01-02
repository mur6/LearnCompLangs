# I referenced:
# https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/

using LinearAlgebra

A = [1 2 3; 4 1 6; 7 8 1]
B = [1 2 3; 4 1 6; 7 8 1]
C = A ⋅ B
println("C=$(C)")
