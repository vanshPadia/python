'''mcq'''

def mcq(ans):
    match ans.lower():
        case 'a':
            return "you choose A "
        case 'b':
            return "you choose B"
        case "c":
            return 'you choose C'

print(mcq("cpu"))
