from PIL import Image

def get_coord(age,bmi):
    x = 143+(age-30)*((4377-241)/(43-30))
    x = round(x)
    y = -90+(bmi-35)*-((27-2128)/(18-35))
    y = round(y)
    return(x,y)

def produce_img(coord):
    img1 = Image.open("static/pic.png")
    img2 = Image.open("static/cursor.png")
    cursor_size = (250,250)
    img2 = img2.resize(cursor_size)
    img1.paste(img2, coord, mask = img2)
    img_to_save = img1.convert('RGB')
    img_to_save.save('static/graph.jpg')

def output_graph(age,bmi):
    coord = get_coord(age,bmi)
    produce_img(coord)