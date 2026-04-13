def win (b , p):

    return any(all(b[i]==p for i in line)for line in 
               [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])

def nmb(b , p):

    w=win(b , "0"),win(b , "X")
    if w[0]: return 1, None
    if w[1]: return -1, None
    if " " not in b: return 0, None 

    best=(-2, None) if p=="0" else (2, None) 

    for i in [j for j,v in enumerate(b) if v==" "]: 
        b[i]=p
        score, _=nmb(b , "0" if p=="X" else "X")
        b[i]=" "
        if (p=="0" and score>best[0]) or (p=="X" and score<best[0]):
            best=score, i
    return best
b=[" "]*9
while True:
    print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}")
    if win(b,"X")or win(b,"0") or " " not in b:
        print("Game over!")
        break
    if b.count("X")<=b.count("0"):
        move=int(input("Enter your move (0-8): "))
        if b[move]==" ":
            b[move]="X"
    else: 
        b[nmb(b,"0")[1]]="0"