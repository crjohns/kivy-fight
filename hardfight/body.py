class Body:
    def __init__(self, root):
        self.root = root

    def printMe(self):
        self.root.printMe(0)
        

class Part:

    def __init__(self, name, subparts=[]):
        self.subparts = subparts
        self.name = name

    def printMe(self, level):
        print "  "*level,
        print self.name
        for part in self.subparts:
            part.printMe(level+1)




human = Body(
            Part("body",
                [ Part("l. upper arm",
                        [Part("l. lower arm", [Part("l. hand")])]
                      ),
                  Part("r. upper arm",
                        [Part("r. lower arm", [Part("r. hand")])]
                      ),
                  Part("l. upper leg",
                        [Part("l. lower leg", [Part("l. foot")])]
                      ),
                  Part("r. upper leg",
                        [Part("r. lower leg", [Part("r. foot")])]
                      ),
                  Part("neck",
                          [Part("head", [])]
                      )
                 ]
                 )
            )

human.printMe()


