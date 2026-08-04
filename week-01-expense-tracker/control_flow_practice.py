# control_flow_practice.py
# 1. Given a list of 5 expense amounts, loop through and print
#    "OVER BUDGET" for any expense above 100, else print the amount
# 2. Use a while loop to keep adding numbers from a list until
#    the running total exceeds 300, then stop and print how many items it took
# 3. Bonus: use a for loop with an if/else to count how many expenses
#    were "small" (<50) vs "large" (>=50)



expenses = [10, 30, 50, 100, 120]

# 1 & 3 combined: budget check + small/large count in one pass
small_count = 0
large_count = 0

for amount in expenses:
    print("OVER BUDGET" if amount > 100 else f"amount: {amount}")
    if amount < 50:
        small_count += 1
    else:
        large_count += 1

print(f"Small count: {small_count}")
print(f"Large count: {large_count}")

# 2: running total until it exceeds 300
total = 0
count = 0
for amount in expenses:
    if total > 300:
        break
    total += amount
    count += 1

print(f"It took {count} items to exceed 300 (total = {total})")