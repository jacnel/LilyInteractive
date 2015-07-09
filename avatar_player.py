from Tkinter import *
from PIL import Image, ImageTk
#import main

class AvatarPlayer(Label):
    def __init__(self, master):
        self.idle = "AvatarGifs/idle2.gif"
        self.talking = "AvatarGifs/talking2.gif"
        self.current_gif = self.getFrames(master, self.idle)
        self.count = 0
        self.idx = 0
        
        Label.__init__(self, master, image=self.current_gif[0])
        
        self.cancel = self.after(self.delay, self.play)

    def getFrames(self, master, filename):
        im = Image.open(filename)
        width = 560
        height = 315
        resized = im.resize((width,height),Image.ANTIALIAS)
        seq = []
        try:
            while True:
                seq.append(resized.copy())
                im.seek(len(seq))
                resized = im.resize((width,height),Image.ANTIALIAS)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        frames = [ImageTk.PhotoImage(first)]


        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            frames.append(ImageTk.PhotoImage(frame))

        return frames
    
    def checkQ(self):
        main.q
        print str(main.q.get())
        
    def play(self):
        self.config(image=self.current_gif[self.idx])
        self.idx += 1
        self.count += 1
        if self.idx == len(self.current_gif):
            self.idx = 0
        if self.count%5 == 0:
            pass
            #self.checkQ()
        self.cancel = self.after(100, self.play)
        

def avatar_player():
    root = Tk()
    root.geometry("400x600")
    anim = AvatarPlayer(root)
    anim.pack()
    root.mainloop()


