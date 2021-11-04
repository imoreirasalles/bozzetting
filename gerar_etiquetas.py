import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

EXCEL_EXTENSIONS = ["xls", "xlsx"]
INPUT = "input"
OUTPUT = "output"


input_files = [pd.read_excel(os.path.join(INPUT,file)) for file in os.listdir(
    INPUT) if file.split(".")[1] in EXCEL_EXTENSIONS]


def draw_folders(output_dir, row):
    """
    Draw text in A3 page
    """

    print(
        f"[desenhando]  {row['Record name']}  {row['Pasta']}  {row['Título'][:40]}..."
    )

    im = Image.new("RGB", (842, 1191), "white")
    draw = ImageDraw.Draw(im)

    arial_large = ImageFont.truetype("arial.ttf", 20)

    arial_small = ImageFont.truetype("arial.ttf", 14)

    draw.text((60, 80), str(row["collection"]), fill="gray", font=arial_small)

    draw.text((60, 120), str(row["Record name"]),
              fill="black", font=arial_large)

    draw.text(
        (700, 120), str(row["Pasta"]), fill="black", font=arial_large,
    )

    draw.text((60, 180), str(row["Título"]), fill="black", font=arial_large)

    draw.text(
        (60, 230),
        "Número de fotografias: " + str(row["Número de imagens"]),
        fill="black",
        font=arial_small,
    )

    filename = f'{row["Record name"]} ({row["Pasta"]}).pdf'
    im.save(os.path.join(output_dir, filename), "PDF", quality=100)


def main():
    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)
    for df in input_files:
        for _,row in df.iterrows():
            row["collection"] = "Col. 036 Diários Associados"
            draw_folders(OUTPUT, row)


if __name__ == "__main__":
    main()
