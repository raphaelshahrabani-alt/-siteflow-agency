#!/usr/bin/env python3
"""Montreal power bank kiosk prospecting sheet, with contact details."""

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
RED = colors.HexColor("#B91C1C")
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
cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=7, leading=8.6, textColor=INK)
cellb = ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=7, leading=8.6, textColor=INK)
cellm = ParagraphStyle("cellm", fontName="Helvetica", fontSize=6.6, leading=8.2, textColor=MUTED)
cellr = ParagraphStyle("cellr", fontName="Helvetica-Bold", fontSize=6.6, leading=8.2, textColor=RED)

# venue, address, phone, email / web, note
TIERS = [
    ("Tier 1", T1, "Walk in this week",
     "Owner-operated. One decision maker. You can get a yes in a single conversation.", [
        ("Nightlife: Saint-Laurent, Plateau, Mile End", [
            ("Les Foufounes Electriques", "87 rue Sainte-Catherine E, H2X 1K5", "514-844-5539",
             "info@foufouneselectriques.com", "Daily 4pm-3am. Multi-floor, pool tables, open since 1983"),
            ("Apt. 200", "3643 boul Saint-Laurent, H2X 2V5", "438-880-3354",
             "montreal@apt200.com / apt200.com", "Tue-Sun 9pm-3am. Dance-focused, young crowd"),
            ("Ecole Privee", "3500 boul Saint-Laurent, H2X 2V2", "514-558-1738",
             "clubecoleprivee.com", "Thu-Sat 10pm-3am. Tables: 438-921-5767"),
            ("Bar Datcha", "98 av Laurier O, H2T 2N4", "514-279-3555",
             "bardatcha.ca / IG @bardatcha", "Wed-Sun nights. Connected to Bar Kabinet"),
            ("Blue Dog Motel", "3958 boul Saint-Laurent, H2W 1Y3", "514-581-4187",
             "", "Daily 10pm-3am. Cheap, packed, late"),
            ("Bar Le Ritz PDB", "179 rue Jean-Talon O, H2R 2X2", "438-289-9994",
             "info@barleritzpdb.com", "Daily 4pm-3am. Email for bookings"),
            ("Cafe Campus", "57 rue Prince-Arthur E, H2X 1B4", "514-844-1010",
             "cafecampus.com", "Worker co-op. Club nights Tue/Thu/Fri/Sat. Student crowd"),
            ("Bily Kun", "354 av du Mont-Royal E, H2T 1P9", "514-845-5392",
             "info@bilykun.com", "Daily 3pm-3am. Regulars who sit for hours"),
            ("Quai des Brumes", "4481 rue Saint-Denis, H2J 2L2", "514-499-0467",
             "quaidesbrumes.ca", "Mon-Fri 4pm-3am. Live music most nights"),
            ("Chez Baptiste", "1045 av du Mont-Royal E, H2J 1X7", "514-522-1384",
             "chezbaptiste.com", "Daily from 3pm. Craft beer, neighbourhood crowd"),
            ("Le Salon Daome", "4465 boul Saint-Laurent, H2W 1Z8", "514-982-7070",
             "lesalondaome@gmail.com", "Thu-Sat 10:30pm-3am. House and techno, long sessions"),
            ("Ausgang Plaza", "6524 rue Saint-Hubert, H2S 2M3", "514-312-1585",
             "ausgangplaza.com", "Office Mon-Fri 9-5. Shows plus club nights"),
            ("Turbo Haus", "2040 rue Saint-Denis, H2X 3K7", "514-379-6363",
             "turbohaus.ca/contact", "Live music, late"),
            ("Le Mal Necessaire", "1015 rue Saint-Alexandre, H2Z 1N9", "514-397-1118",
             "", "Daily from 4:30pm. Tiki bar, very photo-heavy"),
            ("Bar Waverly", "5550 boul Saint-Laurent, H2T 1S8", "514-903-1121",
             "barwaverly@gmail.com", "Daily 4pm-3am. Mile End, corner of St-Viateur"),
            ("Le Rouge Bar", "7 rue Prince-Arthur O", "",
             "lerougebar.com", "VERIFY OPEN. Listings conflict. Multi-floor club"),
        ]),
        ("Nightlife: downtown and Old Montreal", [
            ("New City Gas", "950 rue Ottawa, H3C 1S4", "514-879-1166",
             "newcitygas.com/en/contact", "40,000 sqft over two floors. International DJs"),
            ("Stereo", "858 rue Sainte-Catherine E, H2L 2E3", "514-658-2646",
             "stereonightclub.net", "Afterhours Fri-Sat 2am-10am. Phones dead by 4am"),
            ("Sir Winston Churchill Pub", "1455-1459 rue Crescent, H3G 2B2", "514-288-3814",
             "swcpc.com", "Daily 11:30am-3am. Founding Crescent St venue"),
            ("Brutopia", "1219 rue Crescent, H3G 2B1", "514-393-9277",
             "brutopia@videotron.ca", "Daily. Multi-floor brewpub, live music"),
            ("Hurley's Irish Pub", "1225 rue Crescent, H3G 2B1", "514-861-4111",
             "hurleysirishpub.com", "Daily 11am-3am. Multiple rooms"),
            ("Ziggy's Pub", "1470 rue Crescent, H3G 2B6", "514-285-8855",
             "ziggyspub.ca", "Daily 3pm-3am"),
            ("Thursday's", "1449 rue Crescent, H3G 2B2", "514-288-5656",
             "thursdaysleclub.com", "VERIFY OPEN. Listings conflict"),
            ("Soubois", "1106 boul de Maisonneuve O, H3A 1M7", "514-564-3672",
             "soubois.com", "Thu-Sat only. Dinner into late club"),
            ("Flyjin", "417 rue Saint-Pierre, H2Y 2M3", "514-564-8881",
             "", "Wed-Sat from 7pm, club after 11pm"),
            ("Bord'Elle", "390 rue Saint-Jacques O, H2Y 1S1", "514-379-3553",
             "concierge@bordelle.ca", "Thu-Sat 6pm-3am. Burlesque supper club, seated"),
            ("Velvet Speakeasy", "426 rue Saint-Gabriel", "514-878-9782",
             "velvetspeakeasy.ca / IG @velvet_speakeasy", "Under Auberge Saint-Gabriel. Late techno and house"),
            ("Terrasse Nelligan", "106 rue Saint-Paul O, H2Y 1Z3", "514-788-2040",
             "info@hotelnelligan.com", "Rooftop, 5th floor of Hotel Nelligan. Seasonal"),
            ("Jardin Nelson", "407 Place Jacques-Cartier, H2Y 3B1", "514-861-5731",
             "jardinnelson.com", "No reservations. Huge terrasse, all-day turnover"),
            ("Time Out Market", "705 rue Sainte-Catherine O, H3B 4G5", "514-370-3883",
             "timeout.com", "40,000 sqft in Eaton Centre. 15 eateries, 7 bars"),
            ("Le Central", "30 rue Sainte-Catherine O, H2X 0C8", "",
             "lecentral.ca", "No public phone listed. Use site form. 20+ counters"),
        ]),
        ("Nightlife: the Village", [
            ("Complexe Sky", "1478 rue Sainte-Catherine E, H2L 2J1", "514-529-6969",
             "complexeskymontreal@gmail.com", "Multi-level plus rooftop pool. High capacity"),
            ("Club Unity", "1171 rue Sainte-Catherine E, H2L 2G8", "514-523-2777",
             "clubunity.com", "Thu-Sat 10pm-3am. Three floors, open since 2002"),
            ("Cabaret Mado", "1115 rue Sainte-Catherine E, H2L 2G2", "514-525-7566",
             "gestion@cabaretmado.com / IG @cabaretmado", "Drag cabaret. Seated shows, long dwell, heavy filming"),
            ("Stock Bar", "1171 rue Sainte-Catherine E, H2L 2G8", "514-842-1336",
             "stockbar.com", "Wed-Sun 8pm-3am. Seated, late"),
        ]),
        ("Games and long-dwell entertainment", [
            ("Randolph Pub Ludique (Quartier Latin)", "2041 rue Saint-Denis, H2X 3K8", "514-419-5001",
             "randolph.ca", "Board games, 3-4hr sessions with table service"),
            ("Randolph Pub Ludique (Rosemont)", "6505 rue des Ecores, H2G 2J8", "438-387-4001",
             "randolph.ca", "Second location, same profile"),
            ("North Star Machines a Piastres", "3908 boul Saint-Laurent, H2W 1Y2", "514-904-6444",
             "", "Closed Mon-Tue. Pinball bar, players stay put"),
            ("Arcade MTL", "2031 rue Saint-Denis, H2X 3K8", "514-303-1123",
             "", "Tue-Sun 7pm-3am. Cover charge means people stay"),
            ("FUNHUB Montreal", "733 rue Cathcart #2, H3B 1M6", "514-564-4664",
             "support@funhub.ca", "130+ games plus bar and bistro"),
            ("FUNHUB DIX30", "9415 boul Leduc, Brossard, J4Y 0A5", "450-904-1480",
             "support@funhub.ca", "Same operator. Pitch both together"),
            ("Mira Amusement MTL Forum", "2313 rue Sainte-Catherine O, 3rd fl, H3H 1N2", "514-320-6472",
             "Mira.MTLforum@MiraAmusement.com", "Open to midnight or 1am. Arcade, VR, billiards, sports bar"),
            ("Salon de quilles Darling", "3350 rue Ontario E, H1W 1P7", "514-522-7773",
             "info@darlingbowling.com", "Tue-Sat. 24 lanes, group bookings"),
            ("Quilles G Plus (head office)", "6510 rue Saint-Jacques, H4B 1T6", "514-482-7200",
             "quillesgplus.com", "MULTI-SITE. Pitch head office to land every location at once"),
            ("Quilles G Plus Rose Bowl", "920 rue Saint-Zotique E, H2S 1M8", "514-274-0797",
             "quillesgplus.com", "Rosemont-La Petite-Patrie"),
            ("Quilles G Plus Bannantyne", "5146 av Bannantyne, Verdun", "514-761-1422",
             "quillesgplus.com", "West end"),
            ("Rage Axe Throwing", "1436 rue Atateken, H2L 3L3", "514-303-7243",
             "info@rageaxethrowing.com", "Daily. Group bookings, constant filming"),
            ("Escaparium Dorval", "2064 Route Transcanadienne, Dorval, H9P 2N4", "514-548-3307",
             "clients@escaparium.ca", "Open to 1am Fri-Sat. Groups waiting between rooms"),
            ("Escaparium Laval", "5545 boul des Rossignols, Laval, H7L 5S7", "514-548-3370",
             "clients@escaparium.ca", "Same operator, pitch both"),
            ("Laser Game Evolution Ste-Catherine", "1226 rue Sainte-Catherine O, H3G 1P1", "514-281-6464",
             "lasergame-evolution.ca", "Groups between rounds"),
            ("Laser Game Evolution Marche Central", "8791 boul de l'Acadie, H4N 3K1", "514-384-4848",
             "lasergame-evolution.ca", "Open to midnight Fridays"),
            ("Pang Pang Karaoke", "1226 rue MacKay, H3G 2H4", "514-938-8886",
             "pangpangkaraoke.com", "Private rooms, multi-hour. No alcohol, all ages"),
            ("iVR Amusement", "Montreal and Laval", "438-993-6520",
             "ivramusement.ca", "VR arcade. Sessions plus waiting groups"),
            ("Dooly's Longueuil", "3366 chemin Chambly, Longueuil", "450-646-5252",
             "doolysquebec.com", "Closest Dooly's to the island. Chain HQ: 506-857-8050"),
        ]),
        ("Adult venues (long dwell, late hours)", [
            ("Chez Paree", "1258 rue Stanley, H3B 2S7", "514-866-0495",
             "chezparee@chezparee.ca", "Mon 7pm-3am, Tue-Sat 3pm-3am, Sun 7pm-3am"),
        ]),
    ]),
    ("Tier 2", T2, "Big traffic, slow to close",
     "Real volume, but expect procurement, insurance review and months of lead time. Chase in parallel. Ask the main line who handles vendor placements or concessions, then email that person.", [
        ("Institutions and transit", [
            ("Grande Bibliotheque (BAnQ)", "475 boul de Maisonneuve E", "514-873-1100",
             "info@banq.qc.ca", "Government procurement. All-day dwell, huge volume"),
            ("Casino de Montreal", "1 av du Casino, H3C 4W7", "514-392-2746",
             "mtlsacren@casino.qc.ca", "Loto-Quebec process. Groups line: 514-499-5180"),
            ("Bell Centre", "1909 av des Canadiens-de-Montreal, H3B 4C9", "1-855-219-0576",
             "location@groupech.ca", "Groupe CH / evenko. Business contact is the location@ address"),
            ("Palais des congres", "1001 Place Jean-Paul-Riopelle, H2Z 1H2", "514-871-8122",
             "info@congresmtl.com", "Comiccon and Otakuthon crowds. Ask for client services"),
            ("Gare d'autocars de Montreal", "1717 rue Berri, H2L 4E9", "1-800-858-8555",
             "gamtl.com", "Intercity travellers, long waits, dead phones"),
            ("Gare Centrale", "895 rue de la Gauchetiere O, H3B 4G1", "514-737-3344",
             "info.garecentrale@cominar.com", "RETAIL LEASING: Dinah Corriveau or Stephanie Larocque, same number"),
            ("Montreal-Trudeau (YUL)", "975 boul Romeo-Vachon N, Dorval", "514-633-3333",
             "yulsatisfaction@admtl.com", "ADM concession process. Long lead time"),
        ]),
        ("Retail and malls", [
            ("Centre Eaton de Montreal", "705 rue Sainte-Catherine O, H3B 4G5", "514-288-3708",
             "centreeatondemontreal.com", "Management office. Leasing runs through JLL"),
            ("Complexe Desjardins", "150 rue Sainte-Catherine O, H2X 3Y2", "514-845-4636",
             "complexedesjardins.com", "Management office: 514-281-1870"),
            ("Carrefour Laval", "3035 boul le Carrefour, Laval, H7T 1C8", "450-687-1360",
             "service.laval@cadillacfairview.com", "Cadillac Fairview. Largest mall in Quebec"),
            ("Fairview Pointe-Claire", "6801 Transcanada Hwy, Pointe-Claire, H9R 5J2", "514-695-1610",
             "cfshops.com", "Cadillac Fairview. Same landlord as Carrefour Laval"),
            ("Quartier DIX30", "9120 boul Leduc #230, Brossard, J4Y 0L3", "450-486-1222",
             "quartierdix30.com", "Management office. Retail plus entertainment"),
            ("Galeries d'Anjou", "7999 boul des Galeries-d'Anjou, H1M 1W9", "514-353-6140",
             "galeriesdanjou.com", "Managed by JLL, owned by Ivanhoe Cambridge"),
            ("Place Ville Marie", "1 Place Ville Marie, H3B 2B6", "",
             "placevillemarie.com", "Ivanhoe Cambridge / La Caisse. No direct line found"),
        ]),
        ("Hospitals (longest dwell in the city)", [
            ("CHUM", "1000 rue Saint-Denis, H2X 0C1", "514-890-8000",
             "chumontreal.qc.ca", "Emergency and clinic waits run hours"),
            ("MUHC Glen site", "1001 boul Decarie, H4A 3J1", "514-934-1934",
             "muhc.ca", "Five hospitals on one site including Children's and Royal Vic"),
            ("Jewish General", "3755 ch de la Cote-Sainte-Catherine, H3T 1E2", "514-340-8222",
             "jgh.ca", "Emergency waits"),
            ("CHU Sainte-Justine", "3175 ch de la Cote-Sainte-Catherine, H3T 1C5", "514-345-4931",
             "chusj.org", "Parents waiting hours. Largest mother-child centre in Canada"),
        ]),
        ("Campuses", [
            ("Dawson College", "3040 rue Sherbrooke O, H3Z 1A4", "514-931-8731",
             "buildingmaintenance@dawsoncollege.qc.ca", "Facilities Management office 2E.21, Mon-Fri 8:30-4:30"),
            ("Concordia Webster Library", "1400 boul de Maisonneuve O, H3G 1M8", "514-848-2424 x7706",
             "library.concordia.ca", "J.W. McConnell Building. Open late, very dense"),
            ("McGill McLennan-Redpath", "3459 rue McTavish, H3A 0C9", "514-398-4734",
             "hssl.library@mcgill.ca", "Extended hours funded by SSMU. Try SSMU too"),
            ("UQAM Bibliotheque centrale", "400 rue Sainte-Catherine E, H2L 2C5", "514-987-3824",
             "bibliotheques.uqam.ca", "Metro-connected, huge downtown campus"),
            ("UdeM BLSH", "Pavillon Samuel-Bronfman, 3000 rue Jean-Brillant", "514-343-7430 x1030",
             "umontreal.ca", "Main humanities library"),
            ("Cegep du Vieux Montreal", "255 rue Ontario E / 2040 av Hotel-de-Ville, H2X 3B2", "514-982-3401",
             "cvm.qc.ca", "Very central, dense"),
            ("LaSalle College", "2000 rue Sainte-Catherine O, H3H 2T2", "514-939-2006",
             "experience@collegelasalle.com", "Large downtown campus. Mon-Fri 8-4"),
            ("Vanier College", "821 av Sainte-Croix, Saint-Laurent, H4L 3X9", "1-855-744-7500",
             "info@vaniercollege.qc.ca", "Large campus, big library"),
            ("Marianopolis College", "4873 av Westmount, Westmount, H3Y 1X9", "514-931-8792",
             "admissions@marianopolis.edu", "Dense compact campus"),
            ("College de Maisonneuve", "3800 rue Sherbrooke E, H1X 2A2", "514-254-7131",
             "cmaisonneuve.qc.ca", "Large enrolment"),
            ("HEC Montreal", "3000 ch de la Cote-Sainte-Catherine, H3T 2A7", "514-340-6220",
             "hec.ca", "Business students, long study days"),
            ("Polytechnique Montreal", "2500 ch de Polytechnique", "514-340-4711",
             "polymtl.ca", "Long lab days"),
            ("ETS", "1220 rue Notre-Dame O, H3C 1K3", "514-396-8888",
             "etsmtl.ca", "Griffintown. Near Lucien-L'Allier metro"),
            ("John Abbott College", "21275 rue Lakeshore, Sainte-Anne-de-Bellevue, H9X 3L9", "514-457-6610",
             "communications@johnabbott.qc.ca", "West Island campus"),
        ]),
    ]),
    ("Tier 3", T3, "Seasonal, where the real money is",
     "One festival weekend can out-earn a bar for a quarter. Organisers lock vendors three to six months ahead, so contact them now for next season.", [
        ("Festivals, events and conventions", [
            ("evenko (Osheaga, ileSoniq, LASSO, Heavy MTL)", "Montreal", "514-925-2005",
             "evenko.ca", "One contact covers several of the biggest festivals. Start here"),
            ("Piknic Electronik", "Office: 5455 av De Gaspe #470, H2T 3B3", "514-904-1247",
             "piknicelectronik.com/en/partners", "Every Sunday May-Sept at Parc Jean-Drapeau. Recurring all season"),
            ("Igloofest", "473 boul Saint-Joseph E, H2J 1J8", "514-904-1247",
             "info@igloofest.ca", "January, Old Port. Same operator as Piknic. Cold destroys batteries"),
            ("Festival International de Jazz", "L'Equipe Spectra, Montreal", "",
             "montrealjazzfest.com/en/Home/Contact", "Late June into July, Quartier des Spectacles"),
            ("Just for Laughs / Juste pour rire", "2101 boul Saint-Laurent, H2X 2T5", "",
             "hahaha.com", "July. Corporate line starts 514-845"),
            ("MURAL Festival", "4200 boul Saint-Laurent #1100, H2W 2R2", "",
             "muralfestival.com", "June, Saint-Laurent. Ask for the Sponsorship Director"),
            ("Fierte Montreal / Pride", "4262 rue Sainte-Catherine E #200", "514-903-6193",
             "info@fiertemontrealpride.com", "August"),
            ("Montreal Comiccon", "Palais des congres", "",
             "expo@montrealcomiccon.com", "July. Exhibitor email goes straight to the right desk"),
            ("Otakuthon", "Palais des congres", "",
             "dealers@otakuthon.com", "August. Dealers' area contact"),
            ("National Bank Open, IGA Stadium", "285 rue Gary-Carter", "",
             "accueil@tenniscanada.com", "August, two weeks. Tennis Canada owns the venue"),
        ]),
    ]),
]

# venues with no single phone number: prospect on foot
FOOT = [
    ("Shisha lounges, Saint-Laurent strip", "Two to four hour sessions, crowd is 18 to 30. Almost nobody is pitching them"),
    ("Shisha lounges, Jean-Talon corridor", "Villeray and Saint-Michel. Same profile"),
    ("Shisha lounges, Saint-Laurent borough", "Dense cluster, long sessions"),
    ("Tattoo studios, Plateau and Mile End", "Three to six hour sessions, phone out the whole time"),
    ("Barbershops with walk-in waits", "Thirty to ninety minute waits, repeat traffic"),
    ("Nail and beauty salons", "Long appointments, one hand free, heavy scrolling"),
    ("Laundromats, Plateau / NDG / Verdun", "Ninety minutes with nothing else to do"),
    ("Dealership service lounges", "One to three hour captive waits"),
]

CLOSED = [
    ("SuWu", "3581 boul Saint-Laurent", "Permanently closed. Was on the earlier list"),
    ("Le Saint-Sulpice", "1680 rue Saint-Denis", "Permanently closed. Was on the earlier list"),
    ("Sharx Pool Bar", "1606 rue Sainte-Catherine O", "Closed. Was on the earlier list"),
]

COLS = [c * inch for c in [0.30, 1.72, 2.05, 0.92, 1.85, 2.36, 0.70]]
HEADERS = ["#", "Venue", "Address", "Phone", "Email / web", "Notes", "Status"]


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
                    "Contacts compiled from public listings. Confirm by phone before you plan a route. "
                    "All addresses are Montreal QC unless another city is named.")
    canv.restoreState()


def make_table(rows, start_idx):
    data = [[Paragraph(x, cellb) for x in HEADERS]]
    flags = []
    for i, (name, addr, phone, web, note) in enumerate(rows):
        warn = note.startswith("VERIFY") or note.startswith("MULTI-SITE") or note.startswith("RETAIL")
        if warn:
            flags.append(i + 1)
        data.append([
            Paragraph(str(start_idx + i), cellm),
            Paragraph(name, cellb),
            Paragraph(addr, cell),
            Paragraph(phone, cell),
            Paragraph(web, cellm),
            Paragraph(note, cellr if warn else cellm),
            "",
        ])
    t = Table(data, colWidths=COLS, repeatRows=1)
    style = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (0, 0), (-1, 0), BAND),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, INK),
        ("LINEBELOW", (0, 1), (-1, -1), 0.3, LINE),
        ("BACKGROUND", (6, 1), (6, -1), FILLIN),
        ("LINEBEFORE", (6, 0), (6, -1), 0.6, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ]
    t.setStyle(TableStyle(style))
    return t


def build():
    doc = BaseDocTemplate(OUT, pagesize=PAGE,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN + 0.12 * inch, bottomMargin=MARGIN + 0.12 * inch,
                          title="Montreal Power Bank Kiosk Prospecting Sheet", author="")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=header_footer)])

    story = []
    story.append(Paragraph("Montreal power bank kiosk placement list", h1))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "Venues grouped by how quickly you can realistically close them, not by how big they are. Work Tier 1 first.", body))
    story.append(Spacer(1, 10))

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
        "and malls at 25% to the venue, and chargeFUZE Canada is in market. Walk in and look for a kiosk first. If one "
        "is there, ask the manager how it is working out. Match 25% or beat it, or lead with the thing they cannot "
        "offer: you are local, you answer a text, and you show up the same day when a battery jams.", body))

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

    # foot-prospecting categories
    story.append(Spacer(1, 14))
    story.append(Paragraph("Walk-the-strip categories (no single contact, pitch the owner in person)", h2))
    frows = [[Paragraph("Category", cellb), Paragraph("Why it rents", cellb), Paragraph("Status", cellb)]]
    for name, why in FOOT:
        frows.append([Paragraph(name, cell), Paragraph(why, cellm), ""])
    ft = Table(frows, colWidths=[2.6 * inch, 5.2 * inch, 0.9 * inch])
    ft.hAlign = "LEFT"
    ft.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, 0), BAND),
        ("BACKGROUND", (2, 1), (2, -1), FILLIN),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, INK),
        ("LINEBELOW", (0, 1), (-1, -1), 0.3, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ]))
    story.append(ft)

    # closures
    story.append(Spacer(1, 14))
    story.append(Paragraph("Checked and dropped", h2))
    story.append(Paragraph(
        "These were on the earlier version of this list. Public listings show them closed, so do not waste a trip.", small))
    story.append(Spacer(1, 4))
    crows = [[Paragraph("Venue", cellb), Paragraph("Address", cellb), Paragraph("Finding", cellb)]]
    for name, addr, note in CLOSED:
        crows.append([Paragraph(name, cell), Paragraph(addr, cellm), Paragraph(note, cellr)])
    cl = Table(crows, colWidths=[2.0 * inch, 2.6 * inch, 4.1 * inch])
    cl.hAlign = "LEFT"
    cl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, 0), BAND),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, INK),
        ("LINEBELOW", (0, 1), (-1, -1), 0.3, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ]))
    story.append(cl)

    story.append(Spacer(1, 14))
    story.append(Paragraph("How to work this list", h2))
    steps = [
        "Nightlife and lounges: the Instagram DM beats the phone and beats email. It reaches the owner, not a "
        "generic inbox, and they read it at 2am when the bar is dead.",
        "Restaurants, arcades and salons: walk in between 2pm and 4pm. That is the dead hour and the manager is "
        "on the floor with time to talk.",
        "Multi-site operators are the best use of a single call. Quilles G Plus, FUNHUB, Escaparium, Randolph "
        "and Laser Game Evolution each run several rooms. One yes places several machines.",
        "evenko alone controls Osheaga, ileSoniq, LASSO and Heavy MTL. Piknic and Igloofest share a phone number "
        "and an office. Two calls cover most of the summer and one winter festival.",
        "Campuses, hospitals, malls and transit: call the main line and ask who handles vendor placements or "
        "concessions, then email that named person. Do not pitch the switchboard.",
        "Phone numbers here come from public directory listings. Confirm the venue is open before you drive across "
        "town, especially on anything flagged VERIFY.",
    ]
    rows = [[Paragraph(str(i + 1), cellm), Paragraph(s, cell)] for i, s in enumerate(steps)]
    st = Table(rows, colWidths=[0.3 * inch, 8.0 * inch])
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

    doc.build(story)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
