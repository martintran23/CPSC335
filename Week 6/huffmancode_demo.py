# Huffman coding with user input text
import heapq
from collections import Counter

def build_huffman_codes(text: str):
    if not text:
        return {}
    
    frequency = Counter(text)
    
    heap = [[freq, [char, ""]] for char, freq in frequency.items()]
    heapq.heapify(heap)\
    
    if len(heap) == 1:
        char = heap[0][1][0]
        return {char: "0"}
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
            
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
            
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
        huffman_codes_list = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1], p)))
        
        huffman_dict = {char: code for char, code in huffman_codes_list}
        
        for k, v in list(huffman_dict.items()):
            if v == "":
                huffman_dict[k] = "0"
                
        return huffman_dict