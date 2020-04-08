import os
import openpyxl
from PIL import Image, ImageDraw, ImageFont


def load_data(path):
    """
    Read spreadsheet from file
    """
    wb = openpyxl.load_workbook(path)

    sheet = wb["Plan1"]

    return sheet


def draw_folders(data):
    """
    Draw text in A3 page
    """

    counter = 0

    for rowOfCellObjects in data:
        counter += 1
        print(rowOfCellObjects)
        im = Image.new("RGBA", (1600, 1200), "white")
        draw = ImageDraw.Draw(im)
        arialFont = ImageFont.truetype("arial.ttf", 22)
        draw.text((0, 0), str(rowOfCellObjects[0].value), fill="black", font=arialFont)
        draw.text((0, 40), str(rowOfCellObjects[1].value), fill="black", font=arialFont)
        draw.text((0, 20), str(rowOfCellObjects[2].value), fill="black", font=arialFont)
        draw.text((0, 60), "Col. 036 Diários Associados", fill="gray", font=arialFont)
        im.save(
            "images/"
            + str(rowOfCellObjects[1].value)
            + "-"
            + str(rowOfCellObjects[0].value)
            + ".png"
        )
    return print(f"Você gerou {counter} pastas")


def main():

    PATH = "file.xlsx"

    sheet = load_data(PATH)
    draw_folders(sheet)


if __name__ == "__main__":
    main()
