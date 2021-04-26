import matplotlib.image as img
import sys, os

with open('./bad', 'a') as f:

    frame_index = 0
    while os.path.isfile('./frames/'+str(frame_index)+'.jpg'):

        image = img.imread('./frames/'+str(frame_index)+'.jpg')

        t = []
        for row in image[::5]:
            for r, g, b in row[::5]:
                t.append('1' if sum(map(int, [r, g, b])) > 512 else '0')

        val = int(''.join(t[::-1]), 2)

        f.write(str(val)+'\n')

        frame_index += 1

