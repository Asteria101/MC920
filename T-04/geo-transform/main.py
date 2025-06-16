from interpolation import *

def main():
    args = read()
    src = ski.io.imread(args.i)

    if len(src.shape) == 2:
        src = src[:, :, np.newaxis]
    h, w = src.shape[:2]

    sw, sh, = args.s, args.s
    if args.d:
        sw = args.d[0] / w
        sh = args.d[1] / h

    angle = args.a * np.pi / 180 

    cos = np.cos(angle)
    sin = np.sin(angle)

    rot_m = [[cos, sin, (1 - cos) * w / 2 - sin * h / 2],
             [-sin, cos, sin * w / 2 + (1 - cos) * h / 2]]
    
    # transformed image
    T = np.zeros_like(src, np.uint8)

    if args.m == "n":
        for r in range(h):
            for c in range(w):
                for ch in range(src.shape[2]):
                    if args.a != 0:
                        x = round(c * rot_m[0][0] + r * rot_m[0][1] + rot_m[0][2])
                        y = round(c * rot_m[1][0] + r * rot_m[1][1] + rot_m[1][2])
                    elif args.s != 1.0 or args.d:
                        x = round(c / sw)
                        y = round(r / sh)

                    if (0 <= x < w) and (0 <= y < h):
                        T[r, c, ch] = src[y, x, ch]
                    else:
                        T[r, c, ch] = 255

    elif args.m == "b":
        for r in range(h):
            for c in range(w):
                for ch in range(src.shape[2]):
                    if args.a != 0:
                        x = c * rot_m[0][0] + r * rot_m[0][1] + rot_m[0][2]
                        y = c * rot_m[1][0] + r * rot_m[1][1] + rot_m[1][2]
                    elif args.s != 1.0 or args.d:
                        x = c / sw
                        y = r / sh

                    if (0 <= x < w) and (0 <= y < h):
                        T[r, c, ch] = bilinear(src, x, y, ch)
                    else:
                        T[r, c, ch] = 255

    elif args.m == "bi":
        for r in range(h):
            for c in range(w):
                for ch in range(src.shape[2]):
                    if args.a != 0:
                        x = c * rot_m[0][0] + r * rot_m[0][1] + rot_m[0][2]
                        y = c * rot_m[1][0] + r * rot_m[1][1] + rot_m[1][2]
                    elif args.s != 1.0 or args.d:
                        x = c / sw
                        y = r / sh

                    if (0 <= x < w) and (0 <= y < h):
                        T[r, c, ch] = bicubic(src, x, y, ch)
                    else:
                        T[r, c, ch] = 255
                    
    elif args.m == "l":
        for r in range(h):
            for c in range(w):
                for ch in range(src.shape[2]):
                    if args.a != 0:
                        x = c * rot_m[0][0] + r * rot_m[0][1] + rot_m[0][2]
                        y = c * rot_m[1][0] + r * rot_m[1][1] + rot_m[1][2]
                    elif args.s != 1.0 or args.d:
                        x = c / sw
                        y = r / sh

                    if (0 <= x < w) and (0 <= y < h):
                        T[r, c, ch] = lagrange(src, x, y, ch)
                    else:
                        T[r, c, ch] = 255


    else:
        raise ValueError("Invalid interpolation method. Use 'n', 'b', 'bi', or 'l'.")

    save(T[:args.d[1], :args.d[0]], f"out-images/res_{args.d[0]}x{args.d[1]}_{args.m}_{args.i.split("/")[-1]}")

if __name__ == "__main__":
    main()
