import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import uuid


class TextComparer():

    def __init__(self, url_list=[]):
        self.url_list = url_list
        self.file_list = []

    def download(self, url, filename):
        r = requests.get(url)
        if r.status_code == '404':
            raise Exception("Given url not found")
        else:
            f = open(filename, "a")
            f.write(r.text)

    def multi_download(self):
        threads = []
        with ThreadPoolExecutor(max_workers=20) as executor:
            for url in self.url_list:
                file_name = str(uuid.uuid1())
                self.file_list.append(file_name)
                threads.append(executor.submit(self.download(url, file_name)))

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.file_list) == 0:
            raise StopIteration
        return self.file_list.pop()

    def urllist_generator(self):
        while len(self.url_list) > 0:
            yield self.url_list.pop()

    def avg_vowels(self, text):
        all_vowels = 'aeiouyæøå'
        count_vowels = 0
        all_words = text.split(' ')
        for word in all_words:
            for x in word:
                if x in all_vowels:
                    count_vowels += 1

        return count_vowels/len(all_words)

    def worker(self):
        print('hej')

    def hardest_read(self, workers=multiprocessing.cpu_count()):
        all_vowels = 'aeiouyæøå'
        vowel_dict = {}
        count_vowels = 0
        for file_name in self.file_list:
            f = open(str(file_name), "r")
            line = f.readline()
            all_words = line.split(' ')
            for word in all_words:
                for l in word:
                    if l in all_vowels:
                        count_vowels += 1
            vowel_dict[count_vowels] = file_name
        key_max = max(vowel_dict, key=vowel_dict.get)
        return vowel_dict[key_max]
        


tc = TextComparer(
    ['https://stackoverflow.com/questions/46349681/count-all-words-in-a-sentence-separated-by-spaces'])
print(tc.multi_download())
print(tc.urllist_generator)
print(tc.hardest_read())