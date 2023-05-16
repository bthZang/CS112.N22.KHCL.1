n = int(input())
num = list(map(int,input().split()))
deadline = list(map(int,input().split()))

res = []
tmp = []
tmp_opt_sol = 0
on_time_job = 0
flag = []
current = 0

for i in range(n):
  flag.append(0)

def update(n):
  global res, tmp, tmp_opt_sol, on_time_job
  if(on_time_job > tmp_opt_sol):
    res = tmp.copy()
    tmp_opt_sol = on_time_job

def bound(current):
  global n, deadline, num, flag
  cnt = 0
  for i in range(n):
    if(flag[i] == 0 and deadline[i] >= (current + num[i])):
      cnt+=1
  return cnt;

def BnB(i):
  global res, tmp, tmp_opt_sol, current, on_time_job, deadline, num
  for j in range(n):
    if(flag[j] == 0):
      current += num[j]
      tmp.append(j+1)
      flag[j] = 1
      if(current <= deadline[j]):
        on_time_job += 1
      if(i == n):
        update(n)
      if(on_time_job + bound(current) > tmp_opt_sol):
        BnB(i+1)
      # else:
      #   print(j, current, bound(current))
      if(current <= deadline[j]):
        on_time_job -= 1
      current -= num[j]
      tmp.pop()
      flag[j] = 0

BnB(1)

print(*list(res))
print(tmp_opt_sol)
