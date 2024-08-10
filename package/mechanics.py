# 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭
# 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭
# 😭😭😭😭😭😭😭😭😭😭

MaxX=730
MinX=70
MaxY=680
MinY=10

class computer:
    def __init__(self,speed=5,acceleration=0.00001):
        self.x = 50
        self.y = 10
        self.speed = speed
        self.acceleration=acceleration
    def move(self,ball):
        # self.speed+=self.acceleration
        target_y=ball.y+ball.yspeed*ball.x/abs(ball.xspeed)
        if target_y>MaxY:
            target_y=MaxY-(target_y-MaxY)
        elif target_y<MinY:
            target_y=target_y*-1
        target_y-=50
        if not (self.y > target_y - 10 and self.y < target_y + 10) and ball.xspeed<0:
            
            if self.y < target_y:
                self.y += self.speed
            else:
                self.y -= self.speed
                
        



class pong:
        def __init__(self,x=400,y=400,xspeed=8,yspeed=4,acceleration=0.01):
            self.x=x
            self.y=y
            self.xspeed=xspeed
            self.yspeed=yspeed
            self.acceleration=acceleration
            
        def move(self):
            # self.xspeed+=self.acceleration
            # self.yspeed+=self.acceleration
            self.x+=self.xspeed
            self.y+=self.yspeed
            if(self.y>=MaxY or self.y<=MinY):
                self.yspeed*=-1

                
        def isGameOver(self,player,computer):

            if(self.x>MaxX+2):
                if(player.y<self.y-130 or player.y>self.y+30):
                    return 1
                else:
                    self.xspeed*=-1
                    return 0
            elif(self.x<MinX-2):
                if(computer.y<self.y-150 or computer.y>self.y+30):
                    return -1
                else:
                    self.xspeed*=-1
                    return 0
            return False



class player:
    def __init__(self,speed=0.15,t=0):
        self.x=750
        self.y=10
        self.speed=speed
        self.t=t
        
        
    def move(self,event):
        pass
        
            
            
            
            
            
