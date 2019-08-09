# Elections #

n, m = map(int, input().split())
votes = [0] * m
candidate = 0
for i in range(n):
    vote = int(input()) - 1
    votes[vote] += 1
    if votes[vote] > votes[candidate]:
        candidate = vote

print(candidate)
