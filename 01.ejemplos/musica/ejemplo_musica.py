p1 >> keys((P*[0,1,2,3])[:8], dur=1/4, rate=P[:32], sus=1, scale=Scale.default.pentatonic)

b1 >> dbass(var([0,1,5,3]), dur=PDur(3,8), oct=6, amp=1/2) + (0,9)

b2 >> bass(var([0,1,5,[3,7]]), dur=4)

d1 >> play("o--o")

p2 >> play("M a l a g a ")

p3 >> play("rrss")
