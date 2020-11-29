def Bisect(item, seq):
    if not seq:
        return False
    mid = (len(seq)-1)//2
    if item == seq[mid]:
        return True
    elif item < seq[mid]:
        return Bisect(item, seq[0:mid])
    else:
        return Bisect(item, seq[mid+1:])