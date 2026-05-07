from collections import deque

bullet_price = int(input())
barrel_capacity = int(input())
bullets = list(map(int,input().split()))
locks = deque(map(int,input().split()))
value = int(input())

bullets_shot = 0
barrel_count = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]

    bullets_shot += 1
    barrel_count += 1

    if bullet <= lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    
    if barrel_count == barrel_capacity and bullets:
        print("Reloading!")
        barrel_count = 0

if not locks:
    spent = bullets_shot * bullet_price
    earned = value - spent
    print(f"{len(bullets)} bullets left. Earned ${earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
