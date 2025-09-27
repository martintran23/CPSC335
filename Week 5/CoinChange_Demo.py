from typing import List

def make_change_us(k: int) -> List[int]:
    coins = [25, 10, 5, 1]
    result: List[int] = []
    owe = k
    
    for c in coins:
        count = owe // c
        if count > 0:
            result.extend([c] * count)
            owe -= count * c
        if owe == 0:
            break
    return result

# Demo
if __name__ == "__main__":
    for k in (45, 83, 99):
        print(f"k={k}: {make_change_us(k)}")
        