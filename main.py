from bs4 import BeautifulSoup
import operator

teams = []
players = []
ratings = {}
ctratings = {}
tratings = {}
awpratings = {}
hsratings = {}
entryratings = {}
clutchratings = {}
supportratings = {}
multiratings = {}
deathsratings = {}
money = {}

with open("mainsource.txt", "r") as file:
    text = file.read()
    soup = BeautifulSoup(text, "lxml")
    teamsev = soup.find_all("div", class_="teamCon")
    playersev = soup.find_all("div", class_="teamPlayer")



    for iinfo in playersev:

        ratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Rating 2.0").text), str(iinfo.find("div", class_= "playerButtonText").text)
        ctratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Rating 2.0, CT side").text), str(iinfo.find("div", class_= "playerButtonText").text)
        tratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_="stat-flex", title="Rating 2.0, T side").text), str(iinfo.find("div", class_= "playerButtonText").text)
        awpratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="AWP kills per round").text), str(iinfo.find("div", class_= "playerButtonText").text)
        hsratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Headshot percentage").text), str(iinfo.find("div", class_= "playerButtonText").text)
        entryratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Entry frags per round").text), str(iinfo.find("div", class_= "playerButtonText").text)
        clutchratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Clutches per round").text), str(iinfo.find("div", class_= "playerButtonText").text)
        supportratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Support rounds (assist, survived or traded)").text), str(iinfo.find("div", class_= "playerButtonText").text)
        multiratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Multi kills per round").text), str(iinfo.find("div", class_= "playerButtonText").text)
        deathsratings[iinfo.find("div", class_="card-player-tag text-ellipsis").text] = str(iinfo.find("div", class_= "stat-flex", title="Deaths per round").text), str(iinfo.find("div", class_= "playerButtonText").text)






ratings = sorted(ratings.items(), key=operator.itemgetter(1), reverse=True)
ctratings = sorted(ctratings.items(), key=operator.itemgetter(1), reverse=True)
tratings = sorted(tratings.items(), key=operator.itemgetter(1), reverse=True)
awpratings = sorted(awpratings.items(), key=operator.itemgetter(1), reverse=True)
hsratings = sorted(hsratings.items(), key=operator.itemgetter(1), reverse=True)
entryratings = sorted(entryratings.items(), key=operator.itemgetter(1), reverse=True)
clutchratings = sorted(clutchratings.items(), key=operator.itemgetter(1), reverse=True)
supportratings = sorted(supportratings.items(), key=operator.itemgetter(1), reverse=True)
multiratings = sorted(multiratings.items(), key=operator.itemgetter(1), reverse=True)
deathsratings = sorted(deathsratings.items(), key=operator.itemgetter(1), reverse=True)




with open("analiz.txt", "a") as file1:
    file1.write("Overall Ratings\n")
    for ratingsindict in ratings:

        file1.write("".join(str(ratingsindict)))

        file1.write("\t")
        file1.write("\n")
    file1.write("\n")

    file1.write("CT Ratings\n")
    for ctratingsindict in ctratings:
        file1.write("".join(str(ctratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("T Ratings\n")
    for tratingsindict in tratings:
        file1.write("".join(str(tratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("AWP Ratings\n")
    for awpratingsindict in awpratings:
        file1.write("".join(str(awpratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("HS Ratings\n")
    for hsratingsindict in hsratings:
        file1.write("".join(str(hsratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("Entry Ratings\n")
    for entryratingsindict in entryratings:
        file1.write("".join(str(entryratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("Clutch Ratings\n")
    for clutchratingsindict in clutchratings:
        file1.write("".join(str(clutchratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("Support Ratings\n")
    for supportratingsindict in supportratings:
        file1.write("".join(str(supportratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("Multi Kills Ratings\n")
    for multiratingsindict in multiratings:
        file1.write("".join(str(multiratingsindict)))
        file1.write("\n")
    file1.write("\n")

    file1.write("Deaths Ratings\n")
    for deathratingsindict in deathsratings:
        file1.write("".join(str(deathratingsindict)))
        file1.write("\n")
    file1.write("\n")
