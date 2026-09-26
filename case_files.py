from http.server import SimpleHTTPRequestHandler, HTTPServer
import random

NAMES = ["Alex", "Sara", "Daniel", "Emma", "Ryan", "Maya", "Leo", "Nora"]
PLACES = ["Hotel", "Museum", "Station", "Office", "Mansion", "Gallery", "Cafe", "Library"]
ITEMS = ["Diamond", "Painting", "Secret Document", "Gold Watch", "Key", "Necklace"]
MOTIVES = ["Money", "Revenge", "Jealousy", "Blackmail", "A Secret"]

def make_case():
    suspects = random.sample(NAMES, 4)
    culprit = random.choice(suspects)
    places = random.sample(PLACES, 4)
    alibis = dict(zip(suspects, places))
    records = alibis.copy()
    records[culprit] = random.choice([x for x in PLACES if x != alibis[culprit]])
    crime_place, item, motive = random.choice(PLACES), random.choice(ITEMS), random.choice(MOTIVES)
    clues = [f"{name} says they were at the {alibis[name]}." for name in suspects]
    clues += [f"An independent record places {name} at the {records[name]}." for name in suspects]
    clues += [f"The {item.lower()} disappeared from the {crime_place}.",
              "The security system stopped during the incident.",
              f"A note mentions {motive.lower()}, but gives no name."]
    random.shuffle(clues)
    return suspects, culprit, crime_place, item, motive, clues

class Game(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            return super().do_GET()
        suspects, culprit, place, item, motive, clues = make_case()
        page = open("index.html", encoding="utf-8").read()
        page = page.replace("{{SUSPECTS}}", "".join(
            f'<button class="suspect" data-name="{name}">{name}</button>' for name in suspects))
        page = page.replace("{{CLUES}}", "".join(f"<li>{clue}</li>" for clue in clues))
        for key, value in {"PLACE": place, "ITEM": item, "MOTIVE": motive, "CULPRIT": culprit}.items():
            page = page.replace("{{" + key + "}}", value)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(page.encode("utf-8"))

HTTPServer(("localhost", 8000), Game).serve_forever()
