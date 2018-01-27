import PIL.Image as Image
import os, sys

class Array:
	def __init__(self, n, init = 0):
		self.data = [init for i in range(n)]
		return

	def __getitem__(self, index):
		return self.data[index]


MH = 3000 
M = 8
N = 8


fpre = "x" #图片前缀
# toImage = Image.new('RGBA', (3000, Hize))

matrix = [
	[0 for i in range(N)] for j in range(M)
]

aw = [0 for i in range(N)]


for y in range(1, N + 1):  ## 先试一下 拼一个5*5 的图片
    sw = 0
    # lastImage = Image.new('RGBA', (0, MH * (y-1)))
    for x in range(1, M + 1):
        # 之前保存的图片是顺序命名的，x_1.jpg, x_2.jpg ...
        #fname = "/Users/zhangdengke/Desktop/拼图0/x_%s.jpg" % (N*(y-1)+x)
        fname = "/Users/zhangdengke/Desktop/拼图0/x_%s.jpg" % (N*(y-1)+x)

        fromImage = Image.open(fname)
        w, h = fromImage.size
        
        # resizeImage = fromImage.resize( (int(MH * w / h), MH ), Image.ANTIALIAS ) # 先拼的图片不多，不用缩小
        matrix[x - 1][y - 1] = MH / h
        rw, rh = (w * matrix[x - 1][y - 1], h * matrix[x - 1][y - 1])
        # lw, lh = lastImage.size
        # toImage.paste(resizeImage, (sw, MH * (y-1)) ) 
        # lastImage = resizeImage
        sw += rw
    aw[y - 1] = sw
    print(aw[y - 1])

    # toImage.resize(( 1920 , MH * sw // 1920 ), Image.ANTIALIAS)


ah = 0
for y in range(1, N + 1):
	ah += MH * 19200 / aw[y - 1]
toImage = Image.new('RGBA', (19200, int(ah)))
sph = 0
for y in range(1, N + 1):
	sw = 0
	tmp = 19200 / aw[y - 1]
	lastImage = Image.new('RGBA', (0, int(sph)))
	for x in range(1, M + 1):
		matrix[x - 1][y - 1] *= tmp
		fname = "/Users/zhangdengke/Desktop/拼图0/x_%s.jpg" % (N*(y-1)+x)
		fromImage = Image.open(fname)
		w, h = fromImage.size
		resizeImage = fromImage.resize((int(w * matrix[x - 1][y - 1]), int(h * matrix[x - 1][y - 1])), Image.ANTIALIAS)
		lw, lh = lastImage.size
		sw += lw
		toImage.paste(resizeImage, (int(sw), int(sph)))
		lastImage = resizeImage

	sph += MH * tmp

toImage.save('/Users/zhangdengke/Desktop/拼图0/toImage_6.jpg')
