#!/usr/bin/python2.7

class Disk: 
    def __init__(self, color): 
        self.color = color 

class HanoiTower: 
    
    def __init__(self, diskCount): 
        self.diskCount = diskCount
        self.peg_one = [Disk('black')] * diskCount
        self.peg_two = []
        self.peg_three = []

    def move_disk(self, start, dest):
        disk = start.pop(0)
        dest.insert(0, disk)

    def hanoi(self, diskCount, start, dest, temp): 
        if diskCount > 0: 
            self.hanoi(diskCount-1, start,temp,dest)
            self.move_disk(start,dest)
            self.hanoi(diskCount-1, temp,dest,start)







tower = HanoiTower(10); 

peg_one = tower.peg_one 
peg_two = tower.peg_two 
peg_three = tower.peg_three 
diskNum = tower.diskCount 
tower.hanoi(diskNum,peg_one,peg_two,peg_three) 

    