# coding = utf-8

class practice:

    def move(self, n, a, b, c):
        if n == 1 :
            print ('move', a, '-->', c)
            return
        self.move(n-1, a, c, b)
        print ('move', a, '-->', c )
        self.move(n-1, b, a, c)


d=practice()
d.move(10,'A','B','C')