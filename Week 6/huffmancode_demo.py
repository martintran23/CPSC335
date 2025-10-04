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
        
        huffman_codes_list = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
        
        huffman_dict = {char: code for char, code in huffman_codes_list}
        
        for k, v in list(huffman_dict.items()):
            if v == "":
                huffman_dict[k] = "0"
                
        return huffman_dict
    
    
# Define Encode
def encode(text: str, codes: dict) -> str:
    return ''.join(codes[ch] for ch in text)
    
# Define Decode
def decode(encoded_bits: str, codes: dict) -> str:
    reverse = {code: ch for ch, code in codes.items()}
    
    cur, out = "", []
    for b in encoded_bits:
        cur += b
        if cur in reverse:
            out.append(reverse[cur])
            cur = ""
    return "".join(out)

#  Report Generation
def report_bits(text: str, encoded_bits: str):
    ascii_bits = len(text) * 8
    huff_bits = len(encoded_bits)
    if ascii_bits == 0:
        savings_pct = 0.0
        ratio = "N/A"
    else:
        savings_pct = (ascii_bits - huff_bits) / ascii_bits * 100.0
        ratio = f"{ascii_bits / max(1, huff_bits):.2f}:1" if huff_bits > 0 else "infinity"
        
    return ascii_bits, huff_bits, savings_pct, ratio


# User Interface
text = input("Enter the text you want to compress using Huffman Coding: ").upper()

if not text:
    print("\nNo encodable characters found.")
    
else:
    codes = build_huffman_codes(text)
    print("\nHuffman Codes Generated: ")
    for ch in sorted(codes.keys()):
        printable = ch if ch != " " else "<Space>"
        print(f"{printable}: {codes[ch]}")
    
    encoded_str = encode(text, codes)
    
    decoded_text = decode(encoded_str, codes)
    
    print(f"\nEncoded '{text}':")
    print(encoded_str)
    
    print(f"\nDecoded text: {decoded_text}")
    
    if text == decoded_text:
        print("Decoding successful! Original text matches the decoded text.")
    else:
        print("Decoding unsccessful! Original text does not match the decoded text")
        
        
# Get Statistics (ASCII vs Huffman Bits)
    ascii_bits, huff_bits, savings_pct, ratio = report_bits(text, encoded_str)
    
    print("\n--- Bit Usage & Savings ---")
    print(f"ASCII bits (8 bits/char): {ascii_bits}")
    print(f"Huffman Bits:               {huff_bits}")
    if ascii_bits > 0:
        print(f"Savings:                    {savings_pct:.2f}%")
        print(f"COmpression Ratio:                  {ratio}")