

def pixel_scaler(length: float):
    if length <= 50:
        scale = 10
        pixel = length * scale  # 0<pixel<=500
    elif 50 < length <= 100:
        scale = 5
        pixel = length * scale  # 250<pixel<=500
    elif 100 < length <= 150:
        scale = 10/3
        pixel = length * scale  # 333<pixel<=500
    elif 150 < length <= 200:
        scale = 5/2
        pixel = length * scale  # 375<pixel<=500
    elif 200 < length <= 250:
        scale = 2
        pixel = length * scale  # 400<pixel<=500
    else:
        scale = 1
        pixel = length * scale

    return pixel, scale