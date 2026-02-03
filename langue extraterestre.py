def lange_extraterestre(lst, alphabet):
    p = 0
    while p != len(lst) - 1:
        for i in range(max(len(lst[p]), len(lst[p + 1]))):
            if i <= len(lst[p]) and i <= len(lst[p + 1]):
                if lst[p][i] != lst[p + 1][i]:
                    if str(alphabet).index(lst[p + 1][i]) < str(alphabet).index(lst[p][i]):
                        return False
                    break
            else:
                return False
        p += 1
    return True

print(lange_extraterestre(["zirqhpfscx","zrmvtxgelh","vokopzrtc","nugfyso","rzdmvyf","vhvqzkfqis","dvbkppw","ttfwryy","dodpbbkp","akycwwcdog"], "khjzlicrmunogwbpqdetasyfvx"))