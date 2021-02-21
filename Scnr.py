import os
from smmryapi import SmmryAPI

sm = SmmryAPI('61917EE288')

class Scnr:
    
    def __init__(self):
        
        self.count = 0
        self.summaries = dict()
        self.urls = list()
        self.titles = list()
    
    def smmrize(self, url):
        """
        generates summary of provided article from url via smmry API, with length of 5 sentences

        args:
            url (str): the url to an article to be summarized
            
        returns:
            none
        """
        
        s = sm.summarize(url, sm_length = 5)
        self.summaries[s.sm_api_title] = s.sm_api_content
        self.titles.append(s.sm_api_title)
        
    def add_url(self, url):
        """
        add url to list of urls to be summarized

        args:
            url (str): the url to be added to study guide
            
        returns:
            none
        """
            
        self.urls.append(url)
        self.count += 1
        self.smmrize(url)
    
    def format_summary(self): # just to show it better (for testing)
        """
        for testing print statements, just summary number, title, and content
        
        args:
            none
            
        returns:
            none
        """
        
        for i, s in enumerate(self.summaries):
            
            print('article number: ' + str(i+1))
            print('title: ' + s)
            print(self.summaries[s])
            print("\n")
            
    def remove_article(self, i):
        """
        removes a url from the study guide

        args:
            i (int): index of article (1-indexed) to be removed from the study guide
            
        returns:
            none
        """
        
        if i <= len(self.urls):
            
            url_remove = self.titles[i-1]
            del self.urls[i-1]
            self.summaries = { k:v for k,v in self.summaries.items() if k is not self.titles[i-1] }
            del self.titles[i-1]
            self.count -= 1
            
    def to_latex(self):
        """
        turns summary dict into latex code for the pdf
        
        args:
            none

        returns:
            lat (str): latex code to generate pdf
        """
        
        lat = str()
        
        lat = "\\documentclass{article}\n\\usepackage{natbib}\n\\usepackage{graphicx}\
            \n\\usepackage[a4paper, total={6.5in, 9.25in}]{geometry}\n\\begin{document}\
            \n\n"
            
        for article in self.summaries:
            
            lat += "\\section" + "{" + article + "}" + "\n"
            lat += self.summaries[article].replace("%", "\\%")
            lat += "\n\n"
            
        lat += "\\end{document}"
        
        return lat
    
    def to_pdf(self):
        """
        creates pdf from to_latex()
        """
        
        f = open("demo.tex", "w")
        f.write(self.to_latex())
        f.close()
        
        os.system("pdflatex demo.tex")

