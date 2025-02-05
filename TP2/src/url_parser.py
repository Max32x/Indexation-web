
def extract_info(url):
    # Extraction de l'ID produit
    extracted_id = None
    extracted_variant = None

    # Vérification de la présence de "/product/"
    if "/product/" in url:
        # Découpe pour isoler l'ID produit
        parts = url.split("/product/")[1]
        # Si une variante existe, elle est après "?"
        if "?" in parts:
            extracted_id, query = parts.split("?", 1)
            if "variant=" in query:
                extracted_variant = query.split("variant=")[1]
        else:
            extracted_id = parts

    return extracted_id, extracted_variant

