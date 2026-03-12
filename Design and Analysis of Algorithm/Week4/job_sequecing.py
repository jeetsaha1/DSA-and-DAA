def job_sequencing(profit, deadline):
    n = len(profit)

    # Step 1: Combine jobs and sort by decreasing profit
    jobs = list(zip(profit, deadline))
    jobs.sort(key=lambda x: x[0], reverse=True)

    # Step 2: Find maximum deadline
    max_deadline = max(deadline)

    # Step 3: Create slot array
    slots = [-1] * (max_deadline + 1)   # 1-based indexing
    total_profit = 0
    count_jobs = 0

    # Step 4: Assign jobs
    for p, d in jobs:
        # Try to find slot from deadline to 1
        for j in range(d, 0, -1):
            if slots[j] == -1:
                slots[j] = p
                total_profit += p
                count_jobs += 1
                break

    return count_jobs, total_profit


# Example
profit = [100, 19, 27, 25, 15]
deadline = [2, 1, 2, 1, 3]

jobs_done, max_profit = job_sequencing(profit, deadline)

print("Number of Jobs Done:", jobs_done)
print("Maximum Profit:", max_profit)