"""
A series of three rooms are connected to each other by automatic doors.



each door is operated by a security card. once you enter a room the door automatically closes and that security card cannot be used again. a machine at the start will dispense an unlimited number of cards, but each room (including the starting room) contains scanners and if they detect that you are holding more than three security cards or if they detect an unattended security card on the floor, then all the doors will become permanently locked. however, each room contains a box where you may safely store any number of security cards for use at a later stage.

if you simply tried to travel through the rooms one at a time then as you entered room 3 you would have used all three cards and would be trapped in that room forever!

however, if you make use of the storage boxes, then escape is possible. for example, you could enter room 1 using your first card, place one card in the storage box, and use your third card to exit the room back to the start. then after collecting three more cards from the dispensing machine you could use one to enter room 1 and collect the card you placed in the box a moment ago. you now have three cards again and will be able to travel through the remaining three doors. this method allows you to travel through all three rooms using six security cards in total.

it is possible to travel through six rooms using a total of 123 security cards while carrying a maximum of 3 cards.

let c be the maximum number of cards which can be carried at any time.
let r be the number of rooms to travel through.
let m(c,r) be the minimum number of cards required from the dispensing machine to travel through r rooms carrying up to a maximum of c cards at any time.

for example, m(3,6)=123 and m(4,6)=23.and, σm(c,6)=146 for 3 c  4.


you are given that σm(c,10)=10382 for 3 c  10.

find σm(c,30) for 3 c  40.
"""