import numpy as np
import time
N = 1_000_000

# -- Benchmark: somar dois vetores de 1M psoições --

#Forma Python puro

lista_a = [1.0] * N
lista_b = [2.0] * N
t0 = time.time()
resultado = [a+b for a,b in zip(lista_a, lista_b)]
t1 = time.time()
print(f"Python lista: {(t1-t0)*1000:.1f} ms")

#Forma Numpy

arr_a = np.ones(N, dtype = np.float64)
arr_b = np.full(N, 2.0, dtype = np.float64)
t0 = time.time()
resultado = arr_a + arr_b
t1 =time.time()

print(f"NumPy array: {(t1-t0)*1000:.1f} ms")