import os
from smmryapi import SmmryAPI

sm = SmmryAPI('61917EE288')

class Scnr:
    
    def __init__(self):
        
        self.pdfCount = 0
        self.summaries = dict()
        self.urls = list()
    
    def smmrize(self, url):
        
        s = SmmryAPI('61917EE288').summarize(url, sm_length = 5)
        self.summaries[s.sm_api_title] = s.sm_api_content
        
    def add_url(self, url):
            
        self.urls.append(url)
        self.pdfCount += 1
        self.smmrize(url)
    
    def format_summary(self): # just to show it better
        
        for s in self.summaries:
            
            print(s)
            print(self.summaries[s])