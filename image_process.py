import os
import numpy as np
import matplotlib.pylab as plt

        
def show_image(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('on')
    #input('press <ENTER> to continue')
# %matplotlib inline

def pick_image():
    img_name = []
    fld = []
    root_dir = '.\photos'
    try: 
        for dirName, subdirList, fileList in os.walk(root_dir):
            img_name.append(fileList)
        return img_name, dirName
    except:
        print(f"{root_dir} directory is not found")

def np_array(data):
     ar = np.zeros([len(data),200,200,3], dtype='int16')
     return ar

def convert_npa(data, dir, npa):
    for c,fname in enumerate(data):
        im = plt.imread(f'{dir}\{fname}')
        im = im[:200,:200,:3]
        npa[c] = im
    return npa

def main():
    img_name, dir = pick_image()
    array = np_array(img_name[0])
    np_img_array = convert_npa(img_name[0], dir, array)
    return np_img_array

# print(main())
# # for view image on screen
# arr = main()
# for a in arr:
#     show_image(a)

# for main function calling
# if __name__=="__main__":
#     ar = main()
#     for a in ar:
#         show_image(a)