import numpy as np

def val_px(img, x, y):
    return img[x,y][0]

def newValPixel(mat_ref, img, x, y):
    return val_px(img, x, y)*mat_ref.max()/255
    # return val_px(img, x, y)/255

def get_matrix(mat_ref, v):
    (h,w) = mat_ref.shape
    mat = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            if mat_ref[i,j] >= v:
                mat[i,j] = 1
    return mat


def px_to_matrix(mat_ref, img, x, y):
    v = newValPixel(mat_ref, img, x, y)
    return get_matrix(mat_ref, v)
