from datetime import datetime
import os.path
import sys
import random

if int(sys.version[0]) < 3:
    print("Please use Python 3.x for this script.")
    exit("EXITING")

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Make sure you have Pillow installed -> pip install Pillow")
    exit("EXITING")

# Get number of iterations, check if it's an integer
ITERATIONS = input("How many times would you like the program to iterate (over 5000 suggested)?: ")
try:
    ITERATIONS = int(ITERATIONS)
except ValueError as e:
    print("Please input an integer number!")
    exit("EXITING")

# Get image name, check if exists
FILE_NAME = input("Provide a file: ")
original = None
try:
    original = Image.open(FILE_NAME)
except IOError as e:
    print("Make sure the file exists!")
    exit("EXITING")

# Create file names for images to be written in
IMAGE_ONE = FILE_NAME.split(".")[0] + "_image1.png"
IMAGE_TWO = FILE_NAME.split(".")[0] + "_image2.png"

# Save original image's height and width
width, height = original.size

# Check if file has been drawn before. Let user know
# that they will be overwriting the file
if os.path.isfile(IMAGE_ONE):
    choice = input("File has already been drawn. If you continue, the file will be erased. Continue? y/n: ")
    if choice.lower() == "n":
        exit("EXITING")

# Create two images which will be used for drawing
image1 = Image.new('RGB', (width, height))
image2 = Image.new('RGB', (width, height))

# Initialize drawing tool
draw = ImageDraw.Draw(image1)

# Get colors of the original image and store them into a list
colors = original.convert('RGB').getdata()

# Iteration counter and date log
itr_ctr = 0
start_time = datetime.now().time()


# Compares original image with two new images. Returns
# differences as a tuple
def compare_image(line_y, line_x, line_x_end, line_y_end):
    difference1 = 0
    difference2 = 0
    # Load all pixels of all three images
    img1_colors = image1.convert('RGB').load()
    img2_colors = image2.convert('RGB').load()
    org_colors = original.convert('RGB').load()

    # Iteration count
    px_count = 0

    # Sets the final coordinates up until which the
    # loop will be iterating through
    y_end = line_y_end if line_y_end < height else height - 1
    x_end = line_x_end if line_x_end < width else width - 1

    # In case the starting point of a line is on the same
    # x or y as the end point, subtract from them so more
    # area could be checked.
    if line_y >= height - 2:
        line_y = line_y - 2
    if line_x >= width - 2:
        line_x = line_x - 2

    # i->y, j->x
    for i in range(line_y, y_end):
        for j in range(line_x, x_end):
            # Calculate the difference of RGB of a single pixel and add it
            # to an overall difference sum
            difference1 = difference1 + abs(org_colors[j, i][0] - img1_colors[j, i][0]) \
                          + abs(org_colors[j, i][1] - img1_colors[j, i][1]) \
                          + abs(org_colors[j, i][2] - img1_colors[j, i][2])

            difference2 = difference2 + abs(org_colors[j, i][0] - img2_colors[j, i][0]) \
                          + abs(org_colors[j, i][1] - img2_colors[j, i][1]) \
                          + abs(org_colors[j, i][2] - img2_colors[j, i][2])
            px_count += 1

    # Return average difference of both images
    return int(int(difference1) / px_count), int(int(difference2) / px_count)


# Draw lines of color chosen from original image
for _ in range(ITERATIONS):
    # Get random length and width of the line drawn
    line_length = random.randint(int(original.size[0] / 50), int(original.size[0] / 10))
    line_width = random.randint(int(original.size[1] / 150), int(original.size[1] / 50))
    # Choose random color
    pos = random.randint(0, len(colors) - 1)
    # Get color
    color = colors[pos]
    # Get random coordinates
    x = random.randint(0, width)
    y = random.randint(0, height)

    #
    # TODO CHANGE THICKNESS AFTER ~  50000 it?
    #

    # Draw line on image1
    draw.line((x, y, x + line_length, y), fill=color, width=line_width)

    # Compare image1 and image2 to original. If image1 difference is smaller
    # set image2 to the value of image1
    comp_diff = compare_image(y, x, x + line_length, y + line_width)

    if comp_diff[0] < comp_diff[1]:
        image2.paste(image1)
    else:
        image1.paste(image2)

    itr_ctr += 1

    # Saves images during iteration. Comment the if statement out if you don't want
    # to see the progress
    # if itr_ctr == 100 or itr_ctr == 500 or (itr_ctr % 1000 == 0 and itr_ctr < 5000) \
    #         or (itr_ctr % 5000 == 0 and itr_ctr < 10000) or itr_ctr % 50000 == 0:
    #     image1.save(str(itr_ctr) + "itr_" + IMAGE_ONE)

    # Prints iteration count, can be commented out as well
    # print(_)

end_time = datetime.now().time()
image1.save(IMAGE_ONE)
print("Started: " + str(start_time) + ", ended: " + str(end_time))
