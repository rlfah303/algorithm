def solution(sizes):
    answer = 0
    sizes = [sorted(size, reverse=True) for size in sizes]
    
    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    
    width, height = max(widths), max(heights)
    
    answer = width * height
    
    return answer

"""
#위에꺼 한줄로

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    
"""