"""例如，假設我們想要計算《血字的研究》文本的 Scrabble 分數。每次出現字母 'e' 可獲得 1 分，
而 'q' 則可獲得 10 分。我們有另一個字典，存儲在變數 letter_values 中。
現在，為了計算總分，我們從 0 開始一個累加器，然後遍歷 counts 字典中的每個字母。
對於每個具有對應字母分數的字母（空格、標點符號、大寫字母等不計分），我們將其分數加到總分中。"""
"""f = open('scarlet2.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1
print(letter_counts)
letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for letter in letter_counts:
    if letter in letter_values:
        tot = tot + letter_values[letter] * letter_counts[letter]

print(tot)
"""
# ----------------------------------------------------------
#practice 1 
"""The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!"""
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica":0, "Australia": 1}
# anwser 1
total = sum(travel.values())

# anwser 2 use Accumulating results from a dictionary
total2 = 0
for continent in travel:#遍歷travel字典中的每個key（洲的名稱）
    total2 += travel[continent]#取出洲對應的國家數量並累加到total2
print(total2)
# ----------------------------------------------------------
#practice 2
"""schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode."""
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
# anwser 1
total_credits = sum(schedule.values())
print(total_credits)
# anwser 2 use Accumulating results from a dictionary
total_credits2 = 0
for credit in schedule:
    total_credits2 += schedule[credit]
print(total_credits2)
