from withoutbg import WithoutBG

img = WithoutBG.opensource()
result = img.remove_background("vas.jpg")
result.save("output_vas.png")
