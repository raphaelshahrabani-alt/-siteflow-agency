#!/usr/bin/env python3
"""Montreal power bank kiosk prospecting sheet."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                               Spacer, Table, TableStyle)

OUT = "montreal-kiosk-prospecting-sheet.pdf"

INK = colors.HexColor("#1A1A1A")
MUTED = colors.HexColor("#6B7280")
LINE = colors.HexColor("#D4D4D8")
BAND = colors.HexColor("#F4F4F5")
FILLIN = colors.HexColor("#FAFAF9")
ACCENT = colors.HexColor("#15803D")
T1 = colors.HexColor("#166534")
T2 = colors.HexColor("#9A3412")
T3 = colors.HexColor("#1D4ED8")

PAGE = landscape(letter)
MARGIN = 0.4 * inch

body = ParagraphStyle("body", fontName="Helvetica", fontSize=9, leading=12.5, textColor=INK)
small = ParagraphStyle("small", fontName="Helvetica", fontSize=8, leading=10.5, textColor=MUTED)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=19, leading=23, textColor=INK)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=INK,
                    spaceBefore=10, spaceAfter=5)
cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=7.4, leading=9, textColor=INK)
cellb = ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=7.4, leading=9, textColor=INK)
cellm = ParagraphStyle("cellm", fontName="Helvetica", fontSize=7, leading=8.6, textColor=MUTED)

# name, type, area, why it rents
TIERS = [
    ("Tier 1", T1, "Walk in this week", "Owner-operated. One decision maker. You can get a yes in a single conversation.", [
        ("Nightlife: Saint-Laurent and the Plateau", [
            ("Les Foufounes Electriques", "Bar / club", "Sainte-Catherine E", "Multi-floor, open since 1983, pool tables, very late"),
            ("Apt. 200", "Club", "Saint-Laurent", "Dance-focused, young crowd, constant phone use"),
            ("Ecole Privee", "Club", "Saint-Laurent", "Late dance nights, same strip and crowd"),
            ("Bar Datcha", "Club", "Plateau", "Late electronic, people stay for hours"),
            ("Flyjin", "Club", "Old Montreal", "Late-night, high-spend crowd"),
            ("Blue Dog Motel", "Bar", "Saint-Laurent", "Cheap, packed, open very late"),
            ("Suwu", "Bar / resto", "Saint-Laurent", "Food service rolling into a late bar"),
            ("Bar Le Ritz PDB", "Venue", "Mile Ex", "Shows and dance nights, long sets"),
            ("Le Saint-Sulpice", "Bar", "Saint-Denis", "Huge multi-floor terrasse, student volume"),
            ("Cafe Campus", "Club", "Prince-Arthur", "Student nights, long-running institution"),
            ("Bily Kun", "Bar", "Mont-Royal E", "Regulars who sit for hours"),
            ("Quai des Brumes", "Bar", "Saint-Denis", "Live music, late close"),
            ("Chez Baptiste", "Bar", "Mont-Royal E", "Neighbourhood bar, late"),
            ("Salon Daome", "Club", "Saint-Denis", "Late electronic, hours-long sessions"),
            ("Ausgang Plaza", "Venue", "Plateau / Rosemont", "Shows plus club nights"),
            ("Turbo Haus", "Venue", "Saint-Denis", "Live music, late"),
            ("Le Mal Necessaire", "Bar", "Chinatown", "Tiki bar, busy, very photo-heavy"),
            ("Bar Waverly", "Bar", "Mile End", "Late crowd, tight room"),
            ("Rouge Bar", "Club", "Saint-Laurent", "Late, bottle service"),
        ]),
        ("Nightlife: downtown and Old Montreal", [
            ("New City Gas", "Club", "Griffintown", "Huge capacity, international DJs, long nights"),
            ("Stereo", "After-hours", "Sainte-Catherine E", "Open until sunrise, phones are dead by 4am"),
            ("Sir Winston Churchill Pub", "Pub", "Crescent", "Tourist and student density, multi-room"),
            ("Brutopia", "Brewpub", "Crescent", "Multi-floor, live music, long sits"),
            ("Hurley's Irish Pub", "Pub", "Crescent", "Late, multiple rooms"),
            ("Thursday's", "Bar / club", "Crescent", "Long-running, late close"),
            ("Ziggy's Pub", "Bar", "Crescent", "Late night, steady regulars"),
            ("Soubois", "Club / resto", "Downtown", "Dinner service into a late club"),
            ("Bord'Elle", "Club / resto", "Old Montreal", "Burlesque supper club, seated for hours"),
            ("Terrasse Nelligan", "Rooftop", "Old Montreal", "Tourists shooting photos all afternoon"),
            ("Jardin Nelson", "Terrasse", "Place Jacques-Cartier", "Huge terrasse, all-day turnover"),
            ("Velvet Speakeasy", "Club", "Old Montreal", "Late underground room"),
            ("Time Out Market", "Food hall", "Eaton Centre", "High traffic and people sit to eat"),
            ("Le Central", "Food hall", "Saint-Laurent", "25+ counters, groups linger"),
        ]),
        ("Nightlife: the Village", [
            ("Complexe Sky", "Club complex", "Sainte-Catherine E", "Rooftop plus several floors, high capacity"),
            ("Club Unity", "Club", "Sainte-Catherine E", "Large, late, dance-focused"),
            ("Cabaret Mado", "Cabaret", "Sainte-Catherine E", "Seated shows, long dwell, heavy filming"),
            ("Stock Bar", "Bar", "Sainte-Catherine E", "Seated, late, high phone use"),
        ]),
        ("Games and long-dwell entertainment", [
            ("Randolph Pub Ludique", "Board game pub", "Mont-Royal E", "Three to four hour sessions with table service"),
            ("Randolph Pub Ludique", "Board game pub", "Saint-Denis", "Second location, same profile"),
            ("North Star Machines a Piastres", "Pinball bar", "Saint-Laurent", "Arcade plus bar, players stay put"),
            ("Arcade MTL", "Arcade bar", "Saint-Laurent", "Cover charge means people stay all night"),
            ("FUNHUB Montreal", "Arcade centre", "Montreal", "130+ games plus bar and bistro"),
            ("FUNHUB Brossard", "Arcade centre", "Brossard / DIX30", "130+ games plus bar and bistro"),
            ("Mira Amusement", "Entertainment", "Forum, Atwater", "Arcade, VR, mini-golf, billiards, sports bar"),
            ("Sharx Pool Bar", "Pool hall", "Downtown", "Pool plus bar, verify current status"),
            ("Dooly's", "Pool halls", "Island-wide", "Multiple sites, two hour minimum sessions"),
            ("Quilles G Plus", "Bowling", "Multiple", "League nights, groups of eight plus"),
            ("Salle de quilles Darling", "Bowling", "Rosemont", "Retro bowling, group bookings"),
            ("Escaparium", "Escape rooms", "Saint-Laurent", "Groups waiting between sessions"),
            ("Adventure Rooms Montreal", "Escape rooms", "Downtown", "Groups waiting between sessions"),
            ("Virtual Room Montreal", "VR", "Old Montreal", "Sessions plus waiting groups"),
            ("Rage Axe Throwing", "Axe throwing", "Multiple", "Group bookings, constant filming"),
            ("HatchetHouse", "Axe throwing", "Montreal", "Group bookings, long sessions"),
            ("Pang Pang Karaoke", "Karaoke", "Chinatown", "Private rooms, multi-hour, phones for song lookup"),
            ("Mademoiselle Karaoke", "Karaoke", "Downtown", "Private rooms, multi-hour"),
            ("iSaute / Clip 'n Climb", "Trampoline", "Multiple", "Parents waiting the whole session"),
            ("Laser Game Evolution", "Laser tag", "Multiple", "Groups between rounds"),
        ]),
        ("Shisha lounges (walk the strips, pitch the owner directly)", [
            ("Saint-Laurent strip lounges", "Lounge", "Saint-Laurent", "Two to four hour sessions, crowd is 18 to 30"),
            ("Jean-Talon corridor lounges", "Lounge", "Villeray / Saint-Michel", "Same profile, almost nobody is pitching them"),
            ("Saint-Laurent borough lounges", "Lounge", "Saint-Laurent borough", "Dense cluster, long sessions"),
        ]),
        ("Other long-dwell independents", [
            ("Tattoo studios", "Studio", "Plateau / Mile End", "Three to six hour sessions, phone out the whole time"),
            ("Barbershops with walk-in waits", "Barber", "Downtown / Plateau", "Thirty to ninety minute waits, repeat traffic"),
            ("Nail and beauty salons", "Salon", "Island-wide", "Long appointments, one hand free, heavy scrolling"),
            ("Laundromats", "Laundromat", "Plateau / NDG / Verdun", "Ninety minutes with nothing else to do"),
            ("Dealership service lounges", "Auto", "Island-wide", "One to three hour captive waits"),
            ("Chez Paree", "Adult venue", "Downtown", "Very long dwell, late hours"),
            ("Wanda's", "Adult venue", "Saint-Laurent", "Late hours, phones die"),
            ("Kamasutra", "Adult venue", "Downtown", "Late hours, long dwell"),
        ]),
    ]),
    ("Tier 2", T2, "Big traffic, slow to close", "Real volume, but expect procurement, insurance review and months of lead time. Chase in parallel. Never let these block your first installs.", [
        ("Institutions and transit", [
            ("Grande Bibliotheque (BAnQ)", "Library", "Berri-UQAM", "Among the busiest libraries on the continent, all-day dwell"),
            ("Casino de Montreal", "Casino", "Ile Notre-Dame", "Enormous dwell and traffic, Loto-Quebec procurement"),
            ("Bell Centre", "Arena", "Downtown", "21,000 capacity, phones dead by the third period"),
            ("Palais des congres", "Convention centre", "Chinatown", "Comiccon and Otakuthon are the most phone-heavy crowds in the city"),
            ("Gare d'autocars de Montreal", "Bus terminal", "Berri-UQAM", "Intercity travellers with long waits and dead phones"),
            ("Gare Centrale", "Train station", "Downtown", "VIA and exo commuter volume"),
            ("Montreal-Trudeau (YUL)", "Airport", "Dorval", "Huge, but the ADM concession process is long"),
        ]),
        ("Retail and malls", [
            ("Eaton Centre", "Mall", "Sainte-Catherine", "Downtown foot traffic plus the food hall"),
            ("Complexe Desjardins", "Mall / food court", "Quartier des Spectacles", "RESO connected, office lunch volume"),
            ("Place Ville Marie", "Mall / food hall", "Downtown", "Office towers plus a food hall people sit in"),
            ("Carrefour Laval", "Mall", "Laval", "Largest mall in Quebec"),
            ("Fairview Pointe-Claire", "Mall", "West Island", "High suburban traffic"),
            ("Quartier DIX30", "Lifestyle centre", "Brossard", "Retail plus entertainment district"),
            ("Galeries d'Anjou", "Mall", "Anjou", "East end anchor"),
            ("Marche Central", "Retail strip", "Ahuntsic", "High volume big-box corridor"),
        ]),
        ("Hospitals (longest dwell in the city, institutional sales)", [
            ("CHUM", "Hospital", "Downtown", "Emergency and clinic waits run for hours"),
            ("MUHC Glen site", "Hospital", "Westmount / NDG", "Emergency and clinic waits"),
            ("Jewish General", "Hospital", "Cote-des-Neiges", "Emergency waits"),
            ("CHU Sainte-Justine", "Hospital", "Cote-des-Neiges", "Parents waiting for hours with kids"),
            ("Maisonneuve-Rosemont", "Hospital", "Rosemont", "Emergency and clinic waits"),
        ]),
        ("Campuses (student unions often move faster than facilities)", [
            ("Dawson College", "CEGEP", "Sherbrooke W / Atwater", "Your own campus, library plus main floor"),
            ("Concordia Webster Library", "University", "Downtown", "Open late, very high density"),
            ("Concordia Hall Building", "University", "Downtown", "Main student hub"),
            ("McGill McLennan-Redpath", "University", "Downtown", "Exam-season dwell is extreme"),
            ("McGill SSMU Building", "University", "Downtown", "Student-run, faster decision"),
            ("UQAM Bibliotheque centrale", "University", "Berri-UQAM", "Metro-connected, huge downtown campus"),
            ("UdeM BLSH", "University", "Cote-des-Neiges", "Main humanities library"),
            ("Cegep du Vieux Montreal", "CEGEP", "Saint-Denis", "Very central, dense"),
            ("LaSalle College", "College", "Sainte-Catherine", "Large downtown campus"),
            ("Vanier College", "CEGEP", "Saint-Laurent", "Large campus, big library"),
            ("Marianopolis College", "CEGEP", "Westmount", "Dense compact campus"),
            ("College de Maisonneuve", "CEGEP", "Rosemont", "Large enrolment"),
            ("HEC Montreal", "University", "Cote-des-Neiges", "Long study days"),
            ("Polytechnique Montreal", "University", "Cote-des-Neiges", "Long lab days"),
            ("ETS", "University", "Griffintown", "Engineering, long days on campus"),
            ("John Abbott College", "CEGEP", "Sainte-Anne-de-Bellevue", "West Island campus"),
        ]),
    ]),
    ("Tier 3", T3, "Seasonal, where the real money is", "One festival weekend can out-earn a bar for a quarter. Organisers lock vendors months ahead, so contact them now for next season.", [
        ("Festivals and events", [
            ("Piknic Electronik", "Festival", "Parc Jean-Drapeau", "Every Sunday, May to September, recurring all season"),
            ("Osheaga", "Festival", "Parc Jean-Drapeau", "August, three days, enormous"),
            ("ileSoniq", "Festival", "Parc Jean-Drapeau", "August, electronic, same site"),
            ("Festival International de Jazz", "Festival", "Quartier des Spectacles", "Late June into July"),
            ("Francos de Montreal", "Festival", "Quartier des Spectacles", "June"),
            ("Just for Laughs", "Festival", "Quartier des Spectacles", "July"),
            ("Mural Festival", "Festival", "Saint-Laurent", "June, extremely photo-heavy crowd"),
            ("Grand Prix weekend", "Street festival", "Crescent / Peel", "June, highest street density of the year"),
            ("Fierte Montreal", "Festival", "The Village", "August"),
            ("Igloofest", "Festival", "Old Port", "January, and cold drains phones faster than anything here"),
            ("Montreal Comiccon", "Convention", "Palais des congres", "July, all-day dwell, constant filming"),
            ("Otakuthon", "Convention", "Palais des congres", "August, same profile"),
            ("Nuits d'Afrique", "Festival", "Quartier des Spectacles", "July"),
            ("Fantasia Festival", "Film festival", "Concordia / downtown", "July into August, long screening days"),
            ("National Bank Open, IGA Stadium", "Tournament", "Jarry Park", "August, two weeks of heavy daily traffic"),
        ]),
    ]),
]

COLS = [0.30, 1.72, 0.86, 1.18, 2.34, 1.12, 1.12, 0.66]
COLS = [c * inch for c in COLS]
HEADERS = ["#", "Venue", "Type", "Area", "Why it rents", "Phone", "Instagram / email", "Status"]


def header_footer(canv, doc):
    canv.saveState()
    w, h = PAGE
    canv.setFont("Helvetica-Bold", 8)
    canv.setFillColor(MUTED)
    canv.drawString(MARGIN, h - MARGIN + 6, "MONTREAL KIOSK PLACEMENT / PROSPECTING SHEET")
    canv.setFont("Helvetica", 8)
    canv.drawRightString(w - MARGIN, h - MARGIN + 6, "Page %d" % canv.getPageNumber())
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.5)
    canv.line(MARGIN, h - MARGIN + 1, w - MARGIN, h - MARGIN + 1)
    canv.line(MARGIN, MARGIN - 4, w - MARGIN, MARGIN - 4)
    canv.setFont("Helvetica", 7)
    canv.setFillColor(MUTED)
    canv.drawString(MARGIN, MARGIN - 14,
                    "Verify every venue is open and check for an existing kiosk before you pitch. "
                    "Contact fields are blank on purpose: fill them from Google Maps and Instagram.")
    canv.restoreState()


def make_table(rows, start_idx):
    data = [[Paragraph(x, cellb) for x in HEADERS]]
    for i, (name, typ, area, why) in enumerate(rows):
        data.append([
            Paragraph(str(start_idx + i), cellm),
            Paragraph(name, cellb),
            Paragraph(typ, cellm),
            Paragraph(area, cell),
            Paragraph(why, cell),
            "", "", "",
        ])
    t = Table(data, colWidths=COLS, repeatRows=1)
    style = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (0, 0), (-1, 0), BAND),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, INK),
        ("LINEBELOW", (0, 1), (-1, -1), 0.3, LINE),
        ("BACKGROUND", (5, 1), (7, -1), FILLIN),
        ("LINEBEFORE", (5, 0), (5, -1), 0.6, LINE),
        ("LINEBEFORE", (6, 0), (6, -1), 0.3, LINE),
        ("LINEBEFORE", (7, 0), (7, -1), 0.3, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ]
    t.setStyle(TableStyle(style))
    return t


def build():
    doc = BaseDocTemplate(OUT, pagesize=PAGE,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN + 0.12 * inch, bottomMargin=MARGIN + 0.12 * inch,
                          title="Montreal Power Bank Kiosk Prospecting Sheet",
                          author="")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=header_footer)])

    story = []
    story.append(Paragraph("Montreal power bank kiosk placement list", h1))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "Prospecting sheet. Venues are grouped by how quickly you can realistically close them, "
        "not by how big they are. Work Tier 1 first.", body))
    story.append(Spacer(1, 10))

    # scoring block
    crit = [
        [Paragraph("Score any venue on these five. Take anything hitting four or more.", cellb), ""],
        [Paragraph("Dwell time", cell), Paragraph("Two hours or more in one seat", cellm)],
        [Paragraph("Phone use", cell), Paragraph("Photos, social, ordering, gaming or dating apps while they sit", cellm)],
        [Paragraph("Outlet access", cell), Paragraph("Few accessible plugs, no lending cable behind the bar", cellm)],
        [Paragraph("Crowd", cell), Paragraph("18 to 35, already taps a card without thinking about it", cellm)],
        [Paragraph("Hours", cell), Paragraph("Open past midnight, or serves people who arrive already drained", cellm)],
    ]
    ct = Table(crit, colWidths=[1.5 * inch, 5.1 * inch])
    ct.hAlign = "LEFT"
    ct.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("SPAN", (0, 0), (1, 0)),
        ("BACKGROUND", (0, 0), (-1, 0), BAND),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 1), (-1, -2), 0.3, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ]))
    story.append(ct)
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Late-night nightlife gives you the best economics. A dead phone at 1am with a ride to book is the highest "
        "willingness to pay you will ever see. A cafe at 2pm is the worst, because the customer is sitting next to "
        "an outlet with their own cable.", body))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Before pitching: Battcharge claims 100+ points across Quebec, Recharges.ca works hotels, restaurants, cafes "
        "and malls at 25% to the venue, and chargeFUZE Canada is in market. Walk in and look for a kiosk first. "
        "If one is there, ask the manager how it is working out. That is free competitive intelligence and it "
        "sometimes turns into a switch.", body))

    idx = 1
    for tier_name, tier_col, tier_title, tier_note, groups in TIERS:
        story.append(Spacer(1, 14))
        head = Table([[Paragraph(
            '<font color="%s"><b>%s</b></font> &nbsp;&nbsp;%s' % (tier_col.hexval(), tier_name.upper(), tier_title),
            ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=INK))]],
            colWidths=[doc.width])
        head.setStyle(TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LINEBELOW", (0, 0), (-1, -1), 1.2, tier_col),
        ]))
        story.append(head)
        story.append(Spacer(1, 3))
        story.append(Paragraph(tier_note, small))
        story.append(Spacer(1, 7))

        for group_name, rows in groups:
            story.append(Paragraph(group_name, ParagraphStyle(
                "gh", fontName="Helvetica-Bold", fontSize=8.6, leading=11,
                textColor=tier_col, spaceBefore=7, spaceAfter=3)))
            story.append(make_table(rows, idx))
            idx += len(rows)

    # working notes page
    story.append(Spacer(1, 16))
    story.append(Paragraph("How to fill the contact columns fast", h2))
    steps = [
        "Search the venue on Google Maps. Phone and website are on the listing. Copy the phone straight across.",
        "Find the venue on Instagram. For Montreal bars, clubs and lounges the Instagram DM gets answered faster "
        "than any email address on their website, and it usually reaches the owner rather than a generic inbox.",
        "Skip info@ addresses on nightlife venues. Nobody reads them. Use the DM or walk in.",
        "For restaurants, arcades and salons, walk in between 2pm and 4pm. That is the dead hour and the "
        "manager is on the floor with time to talk.",
        "For campuses, hospitals, malls and transit, you need a named facilities or ancillary services contact. "
        "Call the main line and ask who handles vendor placements or concessions, then email that person.",
        "For festivals, search the event's vendor or partner page and apply through it. Most lock their vendor "
        "list three to six months out.",
    ]
    rows = [[Paragraph(str(i + 1), cellm), Paragraph(s, cell)] for i, s in enumerate(steps)]
    st = Table(rows, colWidths=[0.3 * inch, 6.8 * inch])
    st.hAlign = "LEFT"
    st.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ]))
    story.append(st)

    story.append(Spacer(1, 12))
    story.append(Paragraph("The pitch, in one breath", h2))
    story.append(Paragraph(
        "Free to install, free to keep, you take a cut of every rental and I handle everything. "
        "Recharges.ca pays venues 25%, so match it or beat it, or lead with the thing they cannot offer: "
        "you are local, you answer a text, and you show up the same day when a battery jams.", body))

    story.append(Spacer(1, 12))
    story.append(Paragraph("Accuracy note", h2))
    story.append(Paragraph(
        "Venue names and areas were compiled from general knowledge of the city and a light check for closures. "
        "Montreal venues close, move and rebrand constantly. Confirm each one is open before you plan a route. "
        "Phone numbers and email addresses were deliberately left blank rather than guessed.", small))

    doc.build(story)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
