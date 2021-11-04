import os
import csv
import glob
from PIL import Image, ImageDraw, ImageFont


def load_data(input_path, output_path):
    """
    Read data from csv file
    """
    print("-" * 80)
    print("LOADING DATA")
    print("-" * 80)

    try:
        for filename in glob.glob(os.path.join(input_path, "*.csv")):

            print(filename)

            # CREATE OUTPUT DIRECTORY FOR EACH FILE

            output_folder_name = os.path.basename(filename).split(".")[0]
            output_folder_path = os.path.join(output_path, output_folder_name)

            if os.path.isdir(output_folder_path):
                print(f"[*] Já existe uma pasta no diretório de saída. \n")
            else:
                os.mkdir(output_folder_path)

            # OPEN FILE AND READ EACH ROW

            with open(
                os.path.join(os.getcwd(), filename), "r", encoding="utf-8"
            ) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                line_counter = 0
                draw_counter = 0
                for row in csv_reader:
                    if line_counter == 0:
                        header = row
                        line_counter += 1
                    else:
                        # DRAW FOLDER
                        tags = dict(zip(header, row))
                        draw_folders(output_folder_path, **tags)
                        draw_counter += 1
                        line_counter += 1

                print(
                    f"\n Foram criadas {draw_counter} capas a partir do arquivo {filename}"
                )
                print("-" * 80)

    except Exception as e:
        return print(e)


def draw_folders(path, **data):
    """
    Draw text in A3 page
    """

    print(
        f"[desenhando]  {data['Record name']}  {data['Pasta']}  {data['Título'][:40]}..."
    )

    im = Image.new("RGB", (842, 1191), "white")
    draw = ImageDraw.Draw(im)

    arialLarge = ImageFont.truetype("arial.ttf", 20)

    arialSmall = ImageFont.truetype("arial.ttf", 14)

    draw.text((60, 80), str(data["collection"]), fill="gray", font=arialSmall)

    draw.text((60, 120), str(data["Record name"]),
              fill="black", font=arialLarge)

    draw.text(
        (700, 120), str(data["Pasta"]), fill="black", font=arialLarge,
    )

    draw.text((60, 180), str(data["Título"]), fill="black", font=arialSmall)

    draw.text(
        (60, 230),
        str("Número de fotografias: " + data["Quantidade de imagens"]),
        fill="black",
        font=arialSmall,
    )

    im.save(
        path
        + "/"
        + str(data["Record name"])
        + " ("
        + str(data["Pasta"])
        + ").pdf",
        "PDF",
        quality=100,
    )


def main():

    load_data("input", "output")


if __name__ == "__main__":
    main()
