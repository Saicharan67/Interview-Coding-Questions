import sys

def sort(num_list):
    left = []
    right = []

    if len(num_list) <= 1:
        return num_list
    
    ref = num_list[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    
    left = sort(left)
    right = sort(right)

    return left + [ref] * ref_count + right

if __name__ == "__main__":
    args = sys.argv
    if args[1] == None:
        num_list = input("input list")
    else:
        f_name = args[1]
        with open(f_name) as f:
            num_list = f.read()
    
    sort(num_list)