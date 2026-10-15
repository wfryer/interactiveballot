#!/usr/bin/env python3
"""Builds the Union County, NC interactive ballot as a single HTML file.

Link kinds:
  campaign : the candidate's own campaign website or campaign social page
  gov      : an official government page about the person (not a campaign site)
  third    : a third-party information page (voter guide, Branch, BallotReady, Ballotpedia)
"""
import html
from urllib.parse import urlparse

PRECINCT = "032_FAIRVIEW ELEM-B0056"
GATHERED = "October 15, 2026"

BRANCH = "Branch Politics profile"
BR = "BallotReady profile"
BP = "Ballotpedia"


def L(kind, label, url):
    return {"kind": kind, "label": label, "url": url}


WFAE_SEN = "https://www.wfae.org/politics/2026-10-13/u-s-senate-north-carolina"
WFAE_HOUSE = "https://www.wfae.org/2026-09-22/u-s-house-of-representatives-nc-8-candidates"
WFAE_SC = "https://www.wfae.org/2026-09-22/nc-supreme-court-associate-justice-seat-1"
WFAE_COA1 = "https://www.wfae.org/2026-09-22/nc-court-of-appeals-judge-seat-1-candidates"
WFAE_COA2 = "https://www.wfae.org/2026-09-22/nc-court-of-appeals-judge-seat-2-candidates"
WFAE_COA3 = "https://www.wfae.org/2026-09-22/nc-court-of-appeals-judge-seat-3-candidates"

SECTIONS = [
    {
        "id": "federal",
        "title": "Federal races",
        "races": [
            {
                "id": "us-senate",
                "title": "U.S. Senate",
                "vote": 1,
                "guide": ("WFAE nonpartisan voter guide", WFAE_SEN),
                "cands": [
                    {"name": "Michael Dublin", "party": "G", "links": [
                        L("campaign", "Campaign website", "https://www.dublinforcongress.com/"),
                        L("third", BR, "https://www.ballotready.org/people/michael-dublin-6fb05305-1943-4492-82ab-432100905d64")]},
                    {"name": "Roy Cooper", "party": "D", "links": [
                        L("campaign", "Campaign website", "https://roycooper.com/")]},
                    {"name": "Shannon W. Bray", "party": "L", "links": [
                        L("campaign", "Campaign website", "https://www.shannonbray.us/")]},
                    {"name": "Michael Whatley", "party": "R", "links": [
                        L("campaign", "Campaign website", "https://www.michaelwhatley.com/")]},
                ],
            },
            {
                "id": "us-house-8",
                "title": "U.S. House of Representatives, District 8",
                "vote": 1,
                "guide": ("WFAE nonpartisan voter guide", WFAE_HOUSE),
                "cands": [
                    {"name": "Bo Whitehead", "party": "G", "links": [
                        L("campaign", "Campaign website", "https://whiteheadforcongressnc.carrd.co"),
                        L("campaign", "Campaign Instagram", "https://www.instagram.com/whitehead_for_congress_nc/"),
                        L("third", BR, "https://www.ballotready.org/people/robert-bo-whitehead")]},
                    {"name": "Colby Watson", "party": "D", "links": [
                        L("campaign", "Campaign website", "https://www.colbyforcongress.com/"),
                        L("third", BP, "https://ballotpedia.org/Colby_Watson")]},
                    {"name": "Mark Harris", "party": "R", "incumbent": True, "links": [
                        L("campaign", "Campaign website", "https://markharrisforcongress.org/"),
                        L("gov", "Official U.S. House page (government)", "https://markharris.house.gov")]},
                ],
            },
        ],
    },
    {
        "id": "courts",
        "title": "North Carolina courts",
        "races": [
            {
                "id": "nc-supreme-1",
                "title": "N.C. Supreme Court, Associate Justice, Seat 1",
                "vote": 1,
                "guide": ("WFAE nonpartisan voter guide", WFAE_SC),
                "cands": [
                    {"name": "Anita Earls", "party": "D", "incumbent": True, "links": [
                        L("campaign", "Campaign website", "https://earls4justice.com/"),
                        L("third", BP, "https://ballotpedia.org/Anita_Earls"),
                        L("third", BR, "https://www.ballotready.org/people/anita-earls")]},
                    {"name": "Sarah Stevens", "party": "R", "links": [
                        L("campaign", "Campaign website", "https://www.sarahstevensnc.com/"),
                        L("third", BR, "https://www.ballotready.org/people/sarah-stevens-37eb5ba0-da46-49b3-8f71-b2da9fdc8d20")]},
                ],
            },
            {
                "id": "nc-coa-1",
                "title": "N.C. Court of Appeals Judge, Seat 1",
                "vote": 1,
                "guide": ("WFAE nonpartisan voter guide", WFAE_COA1),
                "cands": [
                    {"name": "Michael C. Byrne", "party": "R", "links": [
                        L("campaign", "Campaign website", "https://mb4nc.com/")]},
                    {"name": "John S. Arrowood", "party": "D", "incumbent": True, "links": [
                        L("campaign", "Campaign website", "https://www.keepjudgearrowood.com/")]},
                ],
            },
            {
                "id": "nc-coa-2",
                "title": "N.C. Court of Appeals Judge, Seat 2",
                "vote": 1,
                "guide": ("WFAE nonpartisan voter guide", WFAE_COA2),
                "cands": [
                    {"name": "George Cooper Bell", "party": "R", "links": [
                        L("campaign", "Campaign website", "https://www.judgegeorgebell.com/"),
                        L("third", BP, "https://ballotpedia.org/George_Bell")]},
                    {"name": "Tobias (Toby) Hampson", "party": "D", "incumbent": True, "links": [
                        L("campaign", "Campaign website", "https://www.judgetobyhampson.com/"),
                        L("third", BP, "https://ballotpedia.org/Toby_Hampson")]},
                ],
            },
            {
                "id": "nc-coa-3",
                "title": "N.C. Court of Appeals Judge, Seat 3",
                "vote": 1,
                "guide": ("WFAE nonpartisan voter guide", WFAE_COA3),
                "cands": [
                    {"name": "Craig Collins", "party": "R", "links": [
                        L("campaign", "Campaign website", "https://www.votecraigcollins.com")]},
                    {"name": "Christine Marie Walczyk", "party": "D", "links": [
                        L("campaign", "Campaign website", "https://www.judgechristine.org/")]},
                ],
            },
        ],
    },
    {
        "id": "state-leg",
        "title": "N.C. General Assembly and District Attorney",
        "races": [
            {
                "id": "nc-senate-35",
                "title": "N.C. State Senate, District 35",
                "vote": 1,
                "cands": [
                    {"name": "Christine E. Winward", "party": "D", "links": [
                        L("campaign", "Campaign Substack", "https://winwardfornc.substack.com"),
                        L("third", BR, "https://www.ballotready.org/people/christine-e-winward")]},
                    {"name": "Todd Johnson", "party": "R", "incumbent": True, "links": [
                        L("campaign", "Campaign website", "http://www.votetoddjohnson.com/"),
                        L("third", BR, "https://www.ballotready.org/people/matthew-todd-t-johnson")]},
                ],
            },
            {
                "id": "nc-house-69",
                "title": "N.C. House of Representatives, District 69",
                "vote": 1,
                "cands": [
                    {"name": "Dean Arp", "party": "R", "incumbent": True, "links": [
                        L("campaign", "Campaign website", "https://deanarp.com/"),
                        L("third", BP, "https://ballotpedia.org/Dean_Arp")]},
                    {"name": "Heidi Sinsley", "party": "D", "links": [
                        L("campaign", "Campaign website", "https://sinsleyfornc.com/")]},
                ],
            },
            {
                "id": "da-30",
                "title": "District Attorney, District 30",
                "vote": 1,
                "note": "Only one candidate appears on this ballot.",
                "cands": [
                    {"name": "Trey Robison", "party": "R", "incumbent": True, "links": [
                        L("third", BRANCH, "https://www.branch.vote/races/2026-north-carolina-general-election-nc-state-district-attorney-nc-prosecutorial-30/candidates/trey-robison")]},
                ],
            },
        ],
    },
    {
        "id": "county",
        "title": "Union County offices",
        "races": [
            {
                "id": "county-commissioners",
                "title": "Union County Board of Commissioners",
                "vote": 3,
                "cands": [
                    {"name": "Christina Dupont", "party": "D", "links": [
                        L("third", "Branch Politics race page (lists Dupont)", "https://branch.vote/races/2026-north-carolina-primary-election-nc-state-county-commissioner-nc-county-union-d")]},
                    {"name": "Melissa M. Merrell", "party": "R", "incumbent": True, "links": [
                        L("gov", "Official county commissioner page (government)", "https://www.unioncountync.gov/government/boards-committees/board-of-county-commissioners/melissa-merrell"),
                        L("third", BR, "https://www.ballotready.org/people/melissa-merrell"),
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-primary-election-nc-state-county-commissioner-nc-county-union-r/candidates/melissa-m-merrell")]},
                    {"name": "Brian W. Helms", "party": "R", "incumbent": True, "links": [
                        L("third", BR, "https://www.ballotready.org/people/brian-helms"),
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-primary-election-nc-state-county-commissioner-nc-county-union-r/candidates/brian-w-helms")]},
                    {"name": "Sam Harris", "party": "R", "links": [
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-general-election-nc-state-county-commissioner-nc-county-union/candidates/sam-harris")]},
                ],
            },
            {
                "id": "county-commissioner-unexpired",
                "title": "Union County Board of Commissioners, unexpired term ending 2028",
                "vote": 1,
                "cands": [
                    {"name": "Madeleine Byl", "party": "D", "links": [
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-general-election-nc-state-county-commissioner-nc-county-union-special/candidates/madeleine-byl")]},
                    {"name": "Errol Wedra", "party": "R", "incumbent": True, "note": "Appointed to this seat in May 2026.", "links": [
                        L("gov", "Official county commissioner page (government)", "https://www.unioncountync.gov/government/boards-committees/board-of-county-commissioners/errol-wedra"),
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-general-election-nc-state-county-commissioner-nc-county-union-special/candidates/errol-wedra")]},
                ],
            },
            {
                "id": "boe-at-large",
                "title": "Union County Board of Education, At-Large",
                "vote": 1,
                "cands": [
                    {"name": "Alexis Stadler", "party": "D", "links": [
                        L("campaign", "Campaign website", "https://www.stadlerforucps.com")]},
                    {"name": "Linda O. Robinson", "party": "R", "links": [
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-general-election-nc-state-county-board-of-education-member-nc-county-union/candidates/linda-o-robinson")]},
                ],
            },
            {
                "id": "boe-d4",
                "title": "Union County Board of Education, District 4",
                "vote": 1,
                "cands": [
                    {"name": "Brittany Cabuno", "party": "D", "links": [
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-general-election-nc-state-county-board-of-education-member-nc-union-county-school-district-4-post-04/candidates/brittany-cabuno")]},
                    {"name": "Stephen Smith", "party": "R", "links": [
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-primary-election-nc-state-county-board-of-education-member-nc-union-county-school-district-4-r-post-04/candidates/stephen-smith")]},
                ],
            },
            {
                "id": "clerk",
                "title": "Union County Clerk of Superior Court",
                "vote": 1,
                "note": "Only one candidate appears on this ballot.",
                "cands": [
                    {"name": "Wendy Maynard", "party": "R", "links": [
                        L("campaign", "Campaign website", "https://votewendymaynard.com/")]},
                ],
            },
            {
                "id": "sheriff",
                "title": "Union County Sheriff",
                "vote": 1,
                "note": "Only one candidate appears on this ballot.",
                "cands": [
                    {"name": "Eddie Cathey", "party": "R", "incumbent": True, "links": [
                        L("gov", "Sheriff's Office biography (government)", "https://www.unioncountysheriffsoffice.com/about-us/sheriff-eddie-cathey"),
                        L("third", BR, "https://www.ballotready.org/people/eddie-cathey")]},
                ],
            },
        ],
    },
    {
        "id": "nonpartisan",
        "title": "Nonpartisan elections",
        "races": [
            {
                "id": "swcd",
                "title": "Union County Soil and Water Conservation District Supervisor",
                "vote": 2,
                "writeins": 2,
                "cands": [
                    {"name": "Taylor Moyer", "party": "N", "links": [
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-general-election-nc-state-soil-and-water-conservation-district-supervisor-nc-county-union/candidates/taylor-moyer")]},
                    {"name": "Wayne S. Moser", "party": "N", "incumbent": True, "links": [
                        L("third", BRANCH, "https://branch.vote/races/2026-north-carolina-general-election-nc-state-soil-and-water-conservation-district-supervisor-nc-county-union/candidates/wayne-s-moser")]},
                ],
            },
        ],
    },
]

OFFICIAL_SUMMARY = L("official", "Official summary explanation of the amendments (PDF, hosted by the Beaufort County Board of Elections)",
                     "https://www.beaufortncboe.org/sites/beaufortncboe.org/files/attachments/2026-09/2026_11_03_Summary%20Explanation%20of%20Constitutional%20Amendments.pdf")
WUNC = L("news", "WUNC explainer on all three amendments",
         "https://www.wunc.org/politics/2026-09-22/explainer-nc-constitutional-amendments-2026-ballot-property-tax-voter-id")
AXIOS = L("news", "Axios Charlotte: the amendments, with arguments for and against",
          "https://www.axios.com/local/charlotte/2026/10/06/nc-constitutional-amendments-2026-explained")
WBTV = L("news", "WBTV: what to know before you vote on the amendments",
         "https://www.wbtv.com/2026/09/25/north-carolina-2026-ballot-amendments-what-know-before-you-vote/")
BPNEWS = L("news", "Ballotpedia News: the income tax and property tax amendments",
           "https://news.ballotpedia.org/2026/05/22/north-carolina-voters-to-decide-on-two-measures-related-to-property-and-income-tax-limits-on-the-november-2026-ballot/")

MEASURES = [
    {
        "id": "amend-photo-id",
        "title": "Constitutional Amendment: Photo ID for all voters",
        "text": "Constitutional amendment to require all voters, not just those presenting to vote in person, to present photo identification before voting.",
        "opts": ["For", "Against"],
        "links": [OFFICIAL_SUMMARY, WUNC, AXIOS, WBTV],
    },
    {
        "id": "amend-income-tax",
        "title": "Constitutional Amendment: State income tax rate cap",
        "text": "Constitutional amendment to keep the State income tax rate from being raised higher than three and one-half percent (3.5%).",
        "opts": ["For", "Against"],
        "links": [OFFICIAL_SUMMARY, WUNC, AXIOS, BPNEWS],
    },
    {
        "id": "amend-property-tax",
        "title": "Constitutional Amendment: Limits on local property tax increases",
        "text": "Constitutional amendment requiring limits on property tax increases by local governments.",
        "opts": ["For", "Against"],
        "links": [OFFICIAL_SUMMARY, WUNC, AXIOS, BPNEWS],
    },
    {
        "id": "jail-bond",
        "title": "Union County Jail Bonds",
        "text": ("Shall the order authorizing $200,000,000 of bonds plus interest to pay the capital costs of providing for the design, "
                 "construction, furnishing and equipping of a new jail facility, and providing that additional taxes may be levied in an "
                 "amount sufficient to pay the principal of and interest on the bonds, be approved? (Abbreviated. Your ballot lists the full "
                 "question, including an estimated total cost over the life of the bond of $312,224,000 and an estimated property tax "
                 "increase of $31.10 per year for each $100,000 of property tax value.)"),
        "opts": ["Yes", "No"],
        "links": [
            L("official", "Union County government announcement on the bond referendum",
              "https://www.unioncountync.gov/Home/Components/News/News/3227/14"),
            L("news", "WSOC: hearing on the $200M jail bond",
              "https://www.wsoctv.com/news/local/union-county-hold-public-hearing-200m-jail-bond-referendum/LTIFQIAMYJGITD6EQTRSJS72EA/"),
            L("news", "Spectrum News: Union County jail referendum",
              "https://spectrumlocalnews.com/nc/charlotte/news/2026/07/22/union-county-jail-referendum"),
        ],
    },
]

PARTY = {
    "R": ("Republican", "R"),
    "D": ("Democratic", "D"),
    "G": ("Green", "G"),
    "L": ("Libertarian", "L"),
    "N": ("Nonpartisan", "NP"),
}


def esc(s):
    return html.escape(s, quote=True)


def host(url):
    h = urlparse(url).netloc.lower()
    return h[4:] if h.startswith("www.") else h


def status_for(links):
    kinds = [l["kind"] for l in links]
    if "campaign" in kinds:
        return ("campaign", "Official campaign website")
    if "gov" in kinds:
        return ("gov", "No campaign website found. Official government page below.")
    return ("third", "No campaign website found. Third-party information below.")


def link_li(l):
    cls = "k-" + l["kind"]
    return ('<li class="lk %s"><a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
            '<span class="host">%s</span></li>') % (cls, esc(l["url"]), esc(l["label"]), esc(host(l["url"])))


def cand_html(race, c, idx):
    party_name, party_abbr = PARTY[c["party"]]
    st_kind, st_text = status_for(c["links"])
    cid = "%s-%d" % (race["id"], idx)
    order = {"campaign": 0, "gov": 1, "third": 2}
    links = sorted(c["links"], key=lambda l: order[l["kind"]])
    inc = '<span class="tag">Incumbent</span>' if c.get("incumbent") else ""
    note = '<p class="cnote">%s</p>' % esc(c["note"]) if c.get("note") else ""
    icon = {"campaign": "&#10003;", "gov": "&#9873;", "third": "&#9432;"}[st_kind]
    out = []
    out.append('<li class="cand party-%s">' % c["party"])
    out.append('<div class="who"><span class="name">%s</span><span class="chip chip-%s">%s</span>%s</div>' % (
        esc(c["name"]), c["party"], esc(party_name), inc))
    out.append(note)
    out.append('<div class="links"><p class="status st-%s"><span aria-hidden="true">%s</span> %s</p><ul>' % (
        st_kind, icon, esc(st_text)))
    out.extend(link_li(l) for l in links)
    out.append('</ul></div>')
    out.append('<label class="pick"><input type="checkbox" id="%s" data-race="%s" data-name="%s" data-party="%s"> '
               '<span>My pick</span></label>' % (cid, race["id"], esc(c["name"]), party_abbr))
    out.append('</li>')
    return "".join(out)


def race_html(r):
    vote = "Vote for %s" % {1: "ONE", 2: "TWO", 3: "THREE"}[r["vote"]]
    out = []
    out.append('<section class="race" id="race-%s" data-race="%s" data-max="%d" data-title="%s">' % (
        r["id"], r["id"], r["vote"], esc(r["title"])))
    out.append('<header class="rh"><h3>%s</h3><p class="vote">%s</p>' % (esc(r["title"]), vote))
    if r.get("guide"):
        out.append('<p class="guide"><a href="%s" target="_blank" rel="noopener noreferrer">%s</a></p>' % (esc(r["guide"][1]), esc(r["guide"][0])))
    if r.get("note"):
        out.append('<p class="rnote">%s</p>' % esc(r["note"]))
    out.append('</header><ul class="cands">')
    for i, c in enumerate(r["cands"]):
        out.append(cand_html(r, c, i))
    for _ in range(r.get("writeins", 0)):
        out.append('<li class="cand party-N writein"><div class="who"><span class="name">Write-in</span></div>'
                   '<p class="cnote">A blank write-in line appears on the ballot. Fill in the oval and print a name.</p></li>')
    out.append('</ul></section>')
    return "".join(out)


def measure_html(m):
    out = []
    out.append('<section class="race measure" id="race-%s" data-race="%s" data-kind="measure" data-title="%s">' % (
        m["id"], m["id"], esc(m["title"])))
    out.append('<header class="rh"><h3>%s</h3><p class="vote">Choose one</p></header>' % esc(m["title"]))
    out.append('<blockquote class="ballot-text">%s</blockquote>' % esc(m["text"]))
    out.append('<fieldset class="opts"><legend class="sr">My choice for %s</legend>' % esc(m["title"]))
    for o in m["opts"]:
        out.append('<label class="opt"><input type="radio" name="%s" value="%s" data-race="%s"> <span>%s</span></label>' % (
            m["id"], esc(o), m["id"], esc(o)))
    out.append('</fieldset>')
    out.append('<div class="links"><p class="status st-info">Learn more (ballot questions have no campaign sites)</p><ul>')
    for l in m["links"]:
        cls = "k-official" if l["kind"] == "official" else "k-news"
        tag = "Official source" if l["kind"] == "official" else "News or explainer"
        out.append('<li class="lk %s"><a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
                   '<span class="host">%s &middot; %s</span></li>' % (cls, esc(l["url"]), esc(l["label"]), esc(host(l["url"])), tag))
    out.append('</ul></div></section>')
    return "".join(out)


CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.5;color:#1b1f24;background:#f5f3ee;padding-bottom:84px}
a{color:#0b4f9c}
a:hover{color:#06336a}
a:focus-visible,input:focus-visible,button:focus-visible{outline:3px solid #1a1a1a;outline-offset:2px}
.skip{position:absolute;left:-999px;top:0;background:#fff;padding:8px 12px;z-index:100}
.skip:focus{left:8px;top:8px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.wrap{max-width:860px;margin:0 auto;padding:0 16px}
header.site{background:#1c2b3a;color:#fff;padding:28px 0 24px}
header.site h1{margin:0 0 6px;font-size:1.65rem;line-height:1.2}
header.site p{margin:4px 0;color:#dbe4ee}
header.site .meta{font-size:.92rem}
header.site a{color:#fff}
.pill{display:inline-block;border:1px solid #8fa3b8;border-radius:999px;padding:2px 10px;font-size:.82rem;margin:6px 6px 0 0;color:#e9eff5}
.panel{background:#fff;border:1px solid #d9d4c7;border-radius:12px;padding:16px 18px;margin:18px 0}
.panel h2{margin:0 0 8px;font-size:1.15rem}
.panel p,.panel li{margin:6px 0}
.panel ol,.panel ul{padding-left:22px;margin:6px 0}
.legend{display:grid;grid-template-columns:1fr;gap:8px}
@media(min-width:640px){.legend{grid-template-columns:1fr 1fr}}
.swatch{display:flex;align-items:center;gap:10px;font-size:.95rem}
.sw{width:22px;height:22px;border-radius:6px;border:1px solid #888;flex:none}
.sw.R{background:#fbdcdc;border-color:#d68a8a}
.sw.D{background:#dbe8fb;border-color:#8cb0e6}
.sw.G{background:#dcf1dc;border-color:#8cc58c}
.sw.L{background:#fff1c9;border-color:#d9bd62}
.sw.N{background:#eeeeee;border-color:#aaa}
.badges{display:grid;gap:8px;margin-top:10px}
.st-demo{font-size:.9rem;display:flex;gap:8px;align-items:flex-start;flex-wrap:wrap}
h2.sec{margin:34px 0 6px;font-size:1.3rem;border-bottom:3px solid #1c2b3a;padding-bottom:4px}
.race{background:#fff;border:1px solid #cfc9b8;border-radius:12px;margin:16px 0;overflow:hidden}
.rh{padding:12px 16px;background:#ebe7da;border-bottom:1px solid #cfc9b8}
.rh h3{margin:0;font-size:1.05rem}
.rh p{margin:2px 0;font-size:.9rem}
.vote{font-weight:700;letter-spacing:.02em}
.guide a{font-weight:600}
.rnote{font-style:italic}
ul.cands{list-style:none;margin:0;padding:0}
.cand{padding:14px 16px;border-top:1px solid #d9d4c7;display:grid;grid-template-columns:1fr;gap:8px}
.cand:first-child{border-top:0}
@media(min-width:700px){.cand{grid-template-columns:1.05fr 1.6fr auto;align-items:start}.cand .cnote{grid-column:1 / -1}}
.party-R{background:#fdeaea;box-shadow:inset 6px 0 0 #d98080}
.party-D{background:#e6effc;box-shadow:inset 6px 0 0 #7ea4e0}
.party-G{background:#e5f4e5;box-shadow:inset 6px 0 0 #7fbf7f}
.party-L{background:#fff5d6;box-shadow:inset 6px 0 0 #d6b84e}
.party-N{background:#f1f1f1;box-shadow:inset 6px 0 0 #a8a8a8}
.who{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding-left:6px}
.name{font-weight:700;font-size:1.05rem;margin-right:2px}
.chip{font-size:.78rem;font-weight:700;padding:2px 8px;border-radius:999px;border:1px solid;background:#fff}
.chip-R{color:#8a1c1c;border-color:#d98080}
.chip-D{color:#1b4a94;border-color:#7ea4e0}
.chip-G{color:#1d6a1d;border-color:#7fbf7f}
.chip-L{color:#6b5300;border-color:#d6b84e}
.chip-N{color:#444;border-color:#999}
.tag{font-size:.78rem;border:1px dashed #555;border-radius:6px;padding:1px 6px;background:#fff}
.cnote{margin:0 0 0 6px;font-size:.88rem;color:#333}
.links{padding-left:6px}
.status{margin:0 0 4px;font-size:.88rem;font-weight:700}
.st-campaign{color:#0d5c2a}
.st-gov{color:#5a2d86}
.st-third{color:#8a4b00}
.st-info{color:#333}
.links ul{list-style:none;margin:0;padding:0}
.lk{margin:3px 0;font-size:.93rem;word-break:break-word}
.lk .host{display:block;font-size:.8rem;color:#444}
.lk.k-campaign a{font-weight:700}
.pick,.opt{display:inline-flex;align-items:center;gap:8px;font-weight:600;background:#fff;border:2px solid #1c2b3a;border-radius:10px;padding:8px 12px;cursor:pointer;min-height:44px}
.pick input,.opt input{width:22px;height:22px;accent-color:#1c2b3a;cursor:pointer}
.pick:has(input:checked),.opt:has(input:checked){background:#1c2b3a;color:#fff}
.pick:has(input:checked) input,.opt:has(input:checked) input{accent-color:#fff}
.writein{opacity:.9}
.measure{padding-bottom:12px}
.measure .links{padding:0 16px}
.ballot-text{margin:12px 16px;padding:10px 14px;background:#f7f5ee;border-left:5px solid #1c2b3a;border-radius:6px;font-size:.95rem}
fieldset.opts{border:0;margin:6px 16px 10px;padding:0;display:flex;gap:10px;flex-wrap:wrap}
.bar{position:fixed;left:0;right:0;bottom:0;background:#1c2b3a;color:#fff;padding:10px 12px;z-index:50;box-shadow:0 -2px 10px rgba(0,0,0,.25)}
.bar .in{max-width:860px;margin:0 auto;display:flex;gap:10px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.bar button,.btn{font:inherit;font-weight:700;border-radius:10px;border:2px solid #fff;background:#fff;color:#1c2b3a;padding:8px 14px;min-height:44px;cursor:pointer}
.btn{border-color:#1c2b3a}
.bar button.ghost{background:transparent;color:#fff}
#sheet{background:#fff;border:1px solid #cfc9b8;border-radius:12px;padding:18px;margin:30px 0}
#sheet h2{margin:0 0 4px}
#sheet table{width:100%;border-collapse:collapse;margin:12px 0;font-size:.95rem}
#sheet th,#sheet td{border:1px solid #999;padding:6px 8px;text-align:left;vertical-align:top}
#sheet th{background:#ebe7da}
#sheet td.undecided{color:#666;font-style:italic}
.pp{display:inline-block;min-width:1.6em;text-align:center;border:1px solid #555;border-radius:4px;font-size:.8rem;font-weight:700;margin-right:4px;padding:0 3px}
.sheet-actions{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}
.small{font-size:.88rem;color:#333}
footer.site{padding:10px 0 30px;font-size:.88rem;color:#333}
@media print{
  @page{margin:.6in}
  body{background:#fff;padding:0;font-size:11pt}
  header.site,main#ballot,footer.site,.bar,.skip,.sheet-actions,.noprint{display:none !important}
  #sheet{border:0;padding:0;margin:0}
  tr{page-break-inside:avoid}
}
"""

JS = r"""
(function () {
  var KEY = 'interactiveBallot.unionNC.2026-11-03';
  var picks = {};
  try {
    var saved = localStorage.getItem(KEY);
    if (saved) { picks = JSON.parse(saved) || {}; }
  } catch (e) { picks = {}; }

  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(picks)); } catch (e) {}
  }

  var boxes = Array.prototype.slice.call(document.querySelectorAll('input[type=checkbox][data-race]'));
  var radios = Array.prototype.slice.call(document.querySelectorAll('input[type=radio][data-race]'));

  function raceEl(id) { return document.getElementById('race-' + id); }

  boxes.forEach(function (b) {
    var arr = picks[b.getAttribute('data-race')] || [];
    if (arr.indexOf(b.id) !== -1) { b.checked = true; }
  });
  radios.forEach(function (r) {
    var v = picks[r.getAttribute('data-race')];
    if (v && v === r.value) { r.checked = true; }
  });

  boxes.forEach(function (b) {
    b.addEventListener('change', function () {
      var race = b.getAttribute('data-race');
      var max = parseInt(raceEl(race).getAttribute('data-max'), 10) || 1;
      var arr = picks[race] || [];
      if (b.checked) {
        arr.push(b.id);
        while (arr.length > max) {
          var drop = arr.shift();
          var dropEl = document.getElementById(drop);
          if (dropEl) { dropEl.checked = false; }
        }
      } else {
        arr = arr.filter(function (x) { return x !== b.id; });
      }
      picks[race] = arr;
      save();
      render();
    });
  });

  radios.forEach(function (r) {
    r.addEventListener('change', function () {
      picks[r.getAttribute('data-race')] = r.value;
      save();
      render();
    });
  });

  function pill(p) { return '<span class="pp">' + p + '</span>'; }

  function render() {
    var races = Array.prototype.slice.call(document.querySelectorAll('section.race'));
    var decided = 0;
    var rows = [];
    races.forEach(function (sec) {
      var id = sec.getAttribute('data-race');
      var title = sec.getAttribute('data-title');
      var cell = '';
      var did = false;
      if (sec.getAttribute('data-kind') === 'measure') {
        var v = picks[id];
        if (v) { did = true; cell = '<strong>' + v + '</strong>'; }
      } else {
        var arr = picks[id] || [];
        var parts = [];
        arr.forEach(function (bid) {
          var el = document.getElementById(bid);
          if (el) { parts.push(pill(el.getAttribute('data-party')) + el.getAttribute('data-name')); }
        });
        if (parts.length) { did = true; cell = parts.join('<br>'); }
      }
      if (did) { decided += 1; }
      rows.push('<tr><td>' + title + '</td>' + (did ? '<td>' + cell + '</td>' : '<td class="undecided">Not decided yet</td>') + '</tr>');
    });
    document.getElementById('sheet-body').innerHTML = rows.join('');
    document.getElementById('count').textContent = decided + ' of ' + races.length + ' decided';
  }

  function doPrint() { render(); window.print(); }
  document.getElementById('btn-print').addEventListener('click', doPrint);
  document.getElementById('btn-print2').addEventListener('click', doPrint);
  document.getElementById('btn-view').addEventListener('click', function () {
    document.getElementById('sheet').scrollIntoView({ behavior: 'smooth' });
  });
  document.getElementById('btn-clear').addEventListener('click', function () {
    if (!window.confirm('Clear all of your picks on this page?')) { return; }
    picks = {};
    save();
    boxes.forEach(function (b) { b.checked = false; });
    radios.forEach(function (r) { r.checked = false; });
    render();
  });

  render();
})();
"""


def build():
    out = []
    out.append('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
               '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
               '<title>Interactive Ballot: Union County, NC, November 3, 2026</title>\n'
               '<meta name="description" content="An interactive version of a Union County, North Carolina sample ballot for the November 3, 2026 general election, with links to each candidate\'s official website or the next best information source.">\n'
               '<style>%s</style>\n</head>\n<body>\n' % CSS)
    out.append('<a class="skip" href="#ballot">Skip to the ballot</a>\n')
    out.append('<header class="site"><div class="wrap">'
               '<h1>Interactive Ballot: Union County, North Carolina</h1>'
               '<p>November 3, 2026 General Election &middot; Precinct %s</p>'
               '<p class="meta"><span class="pill">Nonpartisan</span><span class="pill">Experimental</span>'
               '<span class="pill">Not affiliated with any candidate, campaign, party, or election office</span></p>'
               '<p class="meta">Created by <a href="https://ai.wesfryer.com">Wes Fryer</a> &middot; Part of <a href="https://healourculture.org">Heal Our Culture</a> &middot; <a href="#make-your-own">Make your own</a> &middot; Links gathered %s</p>'
               '</div></header>\n' % (esc(PRECINCT), GATHERED))
    out.append('<div class="wrap"><main id="ballot">\n')

    out.append('<div class="panel"><h2>How to use this page</h2><ol>'
               '<li>Compare it with your own official sample ballot from the '
               '<a href="https://vt.ncsbe.gov/RegLkup" target="_blank" rel="noopener noreferrer">N.C. State Board of Elections Voter Search</a>. '
               'Your races depend on your address, so yours may differ.</li>'
               '<li>Follow the links under each name to learn about that person. '
               'Campaign websites show how a candidate presents themselves. Third-party pages are listed when no campaign site was found.</li>'
               '<li>Tap <strong>My pick</strong> to track your choices. They are saved only in this browser. Then print your cheat sheet at the bottom of the page.</li>'
               '</ol></div>\n')

    out.append('<div class="panel"><h2>Colors and badges</h2>'
               '<div class="legend">'
               '<div class="swatch"><span class="sw R"></span>Republican (light red)</div>'
               '<div class="swatch"><span class="sw D"></span>Democratic (light blue)</div>'
               '<div class="swatch"><span class="sw G"></span>Green Party</div>'
               '<div class="swatch"><span class="sw L"></span>Libertarian Party</div>'
               '<div class="swatch"><span class="sw N"></span>Nonpartisan race</div>'
               '</div>'
               '<div class="badges">'
               '<div class="st-demo st-campaign"><strong>&#10003; Official campaign website</strong><span>The candidate\'s own site or campaign page, found through nonpartisan voter guides.</span></div>'
               '<div class="st-demo st-gov"><strong>&#9873; Official government page</strong><span>A county, state, or federal page about the person. Helpful, but not a campaign site.</span></div>'
               '<div class="st-demo st-third"><strong>&#9432; Third-party information</strong><span>No campaign site found. Links go to Branch Politics, BallotReady, Ballotpedia, or news coverage instead.</span></div>'
               '</div>'
               '<p class="small">Every party is also written out in a label, so you never have to rely on color alone.</p></div>\n')

    out.append('<div class="panel"><h2>Early voting in Union County: Oct. 15 to Oct. 31</h2>'
               '<p>Monday to Friday 8:00 am to 7:30 pm. Saturdays Oct. 17, 24, and 31, 8:00 am to 3:00 pm. No Sunday voting. '
               'Bring photo ID. Same day registration is available only during early voting.</p>'
               '<p class="small">Sites: Edwards Memorial Library (Marshville), Fairview Town Hall, Hemby Bridge VFD, Mineral Springs VFD, Stallings VFD, '
               'Union County Library Griffin Room (Monroe), Waxhaw Recreation Barn, Wesley Chapel VFD Stations 41 and 42. '
               '<a href="https://unioncountyncelections.gov/voting/early-voting-schedule" target="_blank" rel="noopener noreferrer">Full schedule and addresses</a>.</p></div>\n')

    for s in SECTIONS:
        out.append('<h2 class="sec" id="%s">%s</h2>\n' % (s["id"], esc(s["title"])))
        for r in s["races"]:
            out.append(race_html(r) + "\n")
    out.append('<h2 class="sec" id="questions">Ballot questions</h2>\n')
    out.append('<p class="small">Ballot questions have no candidates, so there are no campaign websites. '
               'Each links to the official source where one exists, plus news explainers.</p>\n')
    for m in MEASURES:
        out.append(measure_html(m) + "\n")
    out.append('</main>\n')

    out.append('<section id="sheet" aria-labelledby="sheet-h"><h2 id="sheet-h">My voting cheat sheet</h2>'
               '<p class="small">Union County, NC &middot; General Election, Tuesday, November 3, 2026 &middot; Early voting Oct. 15 to Oct. 31. '
               'Bring photo ID. Compare against your official sample ballot before you vote.</p>'
               '<table><thead><tr><th scope="col">Race or question</th><th scope="col">My choice</th></tr></thead><tbody id="sheet-body"></tbody></table>'
               '<p class="small">Key: <span class="pp">R</span>Republican <span class="pp">D</span>Democratic <span class="pp">G</span>Green '
               '<span class="pp">L</span>Libertarian <span class="pp">NP</span>Nonpartisan. This sheet is a memory aid, not an official ballot.</p>'
               '<div class="sheet-actions"><button class="btn" id="btn-print2" type="button">Print cheat sheet</button>'
               '<button class="btn" id="btn-clear" type="button">Clear my picks</button></div></section>\n')

    out.append('<section class="panel noprint" id="make-your-own" aria-labelledby="myo-h"><h2 id="myo-h">Make your own interactive ballot</h2>'
               '<p>You can build a page like this one for your own sample ballot, in about ten minutes, with an AI tool such as Claude. '
               'Get the free prompt and instructions at <a href="https://interactiveballot.com">interactiveballot.com</a>, then share what you make with the hashtag <strong>#InteractiveBallot</strong>.</p>'
               '<h3>Why this project exists</h3>'
               '<p>Interactive Ballot is part of <a href="https://healourculture.org" target="_blank" rel="noopener noreferrer">Heal Our Culture</a>, an effort to reduce political polarization and help neighbors engage as informed citizens. '
               'When voters learn about every candidate on their ballot, not only the names in the headlines, our conversations get less angry and our choices get better.</p>'
               '<p>The goal is twofold. First, to encourage voters to arrive at the polls better informed. Second, to encourage candidates to use their websites and other digital resources to explain their ideas, experience, background, and fitness for office, so that voters can find those answers easily. '
               'When a candidate has no website, this page says so plainly.</p></section>\n')

    out.append('<footer class="site"><p>This project is <strong>nonpartisan</strong>, <strong>experimental</strong>, and '
               '<strong>not affiliated with any candidate, campaign, political party, or election office</strong>. '
               'Links are provided for convenience and civic learning. Candidates, districts, and websites can change, so always verify with the '
               '<a href="https://www.ncsbe.gov" target="_blank" rel="noopener noreferrer">N.C. State Board of Elections</a> and the '
               '<a href="https://unioncountyncelections.gov" target="_blank" rel="noopener noreferrer">Union County Board of Elections</a> (704-283-3809).</p>'
               '<p>Interactive Ballot &middot; Union County, NC &middot; 2026 &middot; A <a href="https://healourculture.org" target="_blank" rel="noopener noreferrer">Heal Our Culture</a> project &middot; <a href="https://ai.wesfryer.com">AI and media literacy projects by Wes Fryer</a></p></footer>\n')
    out.append('</div>\n')

    out.append('<div class="bar" role="region" aria-label="My picks"><div class="in">'
               '<span id="count" aria-live="polite">0 decided</span>'
               '<span><button class="ghost" id="btn-view" type="button">View cheat sheet</button> '
               '<button id="btn-print" type="button">Print</button></span></div></div>\n')
    out.append('<script>%s</script>\n</body>\n</html>\n' % JS)
    return "".join(out)


if __name__ == "__main__":
    import sys
    dest = sys.argv[1] if len(sys.argv) > 1 else "interactive-ballot-union-2026.html"
    with open(dest, "w", encoding="utf-8") as f:
        f.write(build())
    print("wrote", dest)
