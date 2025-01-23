import pdfplumber


def extract_text_from_pdf(pdf_path,
                          exclude_headers_and_footers=True,
                          headers_line=1,
                          footer_line=0
                          ):
    """
    Extrai texto de um pdf com opções para ignorar cabeçalhos e rodapés

    :param pdf_path: Caminho para um arquivo pdf
    :param exclude_headers_and_footers: Ignorar os cabeçalhos e rodapés
    :param headers_line: Numero de linhas a ignorar no topo de cada página
    :param footer_line: Numero de linhas a ignorar na parte inferior de cada página
    :return:
    """

    laparams = {#"header": 70,
                #"footer": 750,
                "line_overlap": 0.7,
                "line_margin": 0.5,
                "char_margin": 0.5,
                }

    try:
        # Abrir o arquivo pdf
        with pdfplumber.open(pdf_path, laparams=laparams) as pdf:
            extracted_text = ""

            # Processar para cada página
            for page in pdf.pages:
                page_number = page.page_number - 1
                page_text = page.extract_text(layout=True)

                extracted_text += page_text + '\n'

                im = pdf.pages[page_number].to_image()
                im.draw_rects(pdf.pages[page_number].extract_text_lines())
                im.save(f"visual_debug/visual_debugging-{page_number + 1}.png", format="PNG")

        return extracted_text

    except Exception as e:
        print(f"Erro ao processar pdf: {e}")
        return None


# Exemplo de uso
if __name__ == '__main__':
    pdf_path = "samples/PL das Bets.pdf"
    texto = extract_text_from_pdf(pdf_path)

    if texto:
        print("Texto Extraído:")
        print(texto)
