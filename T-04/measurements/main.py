from properties import *

def main():
    # Input format
    # python3 main.py <input_file>
    
    if len(argv) != 2:
        return
    
    # read source image and convert to grayscale
    src = ski.io.imread(f"in-images/{argv[1]}")
    mono = ski.color.rgb2gray(src)
    mono = cv2.threshold(mono, 0.8, 1, cv2.THRESH_BINARY)[1]
    mono = (mono * 255).astype(np.uint8)
    #save(mono, f"out-images/mono_{argv[1]}")

    contours = getContours(mono)

    n_regions = len(contours) - 1
    print(f"número de regiões: {n_regions}\n")

    small = 0
    medium = 0
    large = 0

    areas = list()

    # contours[0] is the background contour, so we skip it
    for i, obj in enumerate(reversed(contours[1:])):
        M = cv2.moments(obj)

        area = M['m00']
        areas.append(area)
        perimeter = cv2.arcLength(obj, True)
        eccentricity = getEccentricity(obj)
        solidity = getSolidity(obj)

        print(f"região {i:>2}: área: {area:>4.0f} perímetro: {perimeter:>10.6f} excentricidade: {eccentricity:>8.6f} solidez: {solidity:>8.6f}")

        cx, cy = (int(M['m10'] / area), int(M['m01'] / area))
        if i < 10:
            cv2.putText(src, f"{i}", (cx-5, cy+5), cv2.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0), 2)
            cv2.putText(src, f"{i}", (cx-5, cy+5), cv2.FONT_HERSHEY_COMPLEX, .5, (255, 255, 255), 1)
        else:
            cv2.putText(src, f"{i}", (cx-10, cy+5), cv2.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0), 2)
            cv2.putText(src, f"{i}", (cx-10, cy+5), cv2.FONT_HERSHEY_COMPLEX, .5, (255, 255, 255), 1)

        if area < 1500:
            small += 1
        elif 1500 <= area < 3000:
            medium += 1
        elif area >= 3000:
            large += 1

    #save(src, f"out-images/labeled_{argv[1]}")

    print(f"\nnúmero de regiões pequenas: {small:>2}")
    print(f"número de regiões médias: {medium:>2}")
    print(f"número de regiões grandes: {large:>2}")

    #areaHistogram(areas)

if __name__ == "__main__":
    main()
        