from PIL import Image, ImageOps

test = Image.open("./test_images/source/shirt.png")
test = ImageOps.grayscale(test)
test = test.resize((28, 28))
test.save("test.png")
