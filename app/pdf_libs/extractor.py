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
    try:
        # Abrir o arquivo pdf
        with pdfplumber.open(pdf_path) as pdf:
            extracted_text = ""

            # Processar para cada página
            for page in pdf.pages:
                page_text = page.extract_text()

                if exclude_headers_and_footers and page_text:
                    # Dividir o texto em linhas
                    lines = page_text.split('\n')

                    # Remover os cabeçalhos e rodapés
                    lines = lines[headers_line:len(lines) - footer_line]

                    # Reunir o texto processado
                    page_text = ' '.join(lines)

                    extracted_text += page_text + '\n'
                    
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
