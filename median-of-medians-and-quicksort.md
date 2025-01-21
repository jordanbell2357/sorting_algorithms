# Median of medians

Median-finding Algorithm. *Brilliant.org*. Retrieved 22:48, January 20, 2025, from https://brilliant.org/wiki/median-finding-algorithm/

BFPRT (Blum, Floyd, Pratt, Rivest, Tarjan)

```python3
import statistics

def median_of_medians_order_statistic(A, i):
    # Decompose A into batches each of length 5 (last batch has <= 5 elements)
    batches = [A[j:j+5] for j in range(0, len(A), 5)]
    # Find median of each batch
    medians = [statistics.median(batch) for batch in batches]
    
    # Recursively find the median of the medians
    if len(medians) <= 5: # Base case
        pivot = statistics.median(medians)
    else: # Recursive case
        pivot = median_of_medians_order_statistic(medians, len(medians) // 2)
    
    # Partition the list into elements less than, equal to, and greater than the pivot
    lt_pivot = [a for a in A if a < pivot]
    eq_pivot = [a for a in A if a == pivot]
    gt_pivot = [a for a in A if a > pivot]
    
    # Determine where the i-th element lies
    k = len(lt_pivot)
    m = len(eq_pivot)
    if i < k: # The i-th element is in the less-than-pivot group
        return median_of_medians_order_statistic(lt_pivot, i)
    elif i < k + m: # The i-th element is in the equal-to-pivot group
        return pivot  
    else: # The i-th element is in the greater-than-pivot group
        return median_of_medians_order_statistic(gt_pivot, i - k - m)
```

```python
import random

A = [3, 0, 0, 3, 2, 1, 3, 1, 3, 4]
print(median_of_medians_order_statistic(A, len(A) // 2)) # 3
print(statistics.median(A)) # 2.5

B = list(random.choices(population=range(0, 10000), k=1000))
print(median_of_medians_order_statistic(B, len(B) // 2)) # in my run 4844
print(statistics.median(B)) # in my run 4841.5
```

# Quicksort
