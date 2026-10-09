import data_fetcher

name = input("Enter a name of an animal: ")

animals_data = data_fetcher.fetch_data(name)

if animals_data is None:
    request_successful = False
    animals_data = []
else:
    request_successful = True

def load_html(html_file):
    with open(html_file, "r", encoding="utf-8") as handle:
        return handle.read()


html_template = load_html("animals_template.html")


def serialize_animal(animal_obj):
    output = ""

    output += '<li class="cards__item">'

    output += f"""
    <div class="card__title">{animal_obj['name']}</div>
    <p class="card__text">
    """

    if "diet" in animal_obj["characteristics"]:
        output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"

    if "type" in animal_obj["characteristics"]:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"

    output += """
    </p>
    </li>
    """

    return output


# Prüfen, ob das Tier gefunden wurde
if not request_successful:
    animals_info = "<h2>Die Tierdaten konnten nicht geladen werden.</h2>"

elif not animals_data:
    animals_info = f'<h2>Das Tier „{name}“ existiert nicht.</h2>'

else:
    animals_info = ""

    for animal in animals_data:
        animals_info += serialize_animal(animal)


html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__",
    animals_info
)


with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html)

print("Website was successfully generated to the file animals.html.")