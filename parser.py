from bs4 import BeautifulSoup

def get_subjects(soup):
    subjects = []
    sub_ids = ['nav-location-nav-physics', 'nav-location-nav-biology',\
               'nav-location-nav-chemistry', 'nav-location-nav-earth-science',\
               'nav-location-nav-math']
    for sub_id in sub_ids:
        tags = soup.select('a#' + sub_id + ' span.selected')
        for tag in tags:
            subjects.append(str(tag.get_text(strip=True)))
    return subjects

def get_grades(soup):
    grades = []
    grade_ids = ['nav-location-nav-elementary-school', 'nav-location-nav-middle-school',\
                 'nav-location-nav-high-school', 'nav-location-nav-university']
    for grade_id in grade_ids:
        tags = soup.select('a#' + grade_id + ' span.selected')
        for tag in tags:
            grades.append(str(tag.get_text(strip=True)))
    return grades

def get_keywords(soup):
    # tags = soup.select('div#about span[itemprop="keywords"]')
    tags = soup.select('td.simulation-main-description span[itemprop="keywords"]')
    keywords = [str(tag.get_text(strip=True)) for tag in tags]
    return keywords

def get_desc(soup):
    tags = soup.select('div#about p[itemprop="description about"]')
    return str(tags[0].get_text(strip=True))

def get_related_sims(soup):
    tags = soup.select('div#related-sims span.simulation-list-title')
    related_sims = [str(tag.get_text(strip=True)) for tag in tags]
    return related_sims

def get_creds(soup):
    rows = soup.select('div#credits tr')
    credits = {}
    for c1, c2 in zip(rows[0].select('th'), rows[1].select('td')):
        tags = c2.select('span')
        credits[str(c1.get_text(strip=True))] = [str(tag.get_text(strip=True)) for tag in tags]
    return credits

def get_html(soup):
    html = soup.select('div.simulation-main-content')
    return str(html[0].prettify())
