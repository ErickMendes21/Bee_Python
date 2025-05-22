# X = list(map(int, input().split()))
# for i in range(len(X)):
#     if X[i] <= 0:
#         X[i] = 1
#     print(f"X[{i}] = {X[i]}")

# for j, i in enumerate(X):
#     if i <= 0:
#         i = 1
#     print(f"X[{j}] = {i}")

X = []
for j, i in enumerate(X):
    valor = int(input())
    if valor <= 0:
        valor = 1
    X.append(valor)
    print(f"X[{j}] = X[{i}]")
