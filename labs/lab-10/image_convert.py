from PIL import Image, ImageOps

test = Image.open("./test_images/source/hoodie.jpg")
test = ImageOps.grayscale(test)
test = ImageOps.invert(test)
test = test.resize((28, 28))
test.save("test.png")
