from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
protein_sequence_collection = []
missed_sequence_web_collection = []
import os
os.getcwd()
data_list = pd.read_excel('/Users/zhenjiaodu/Downloads/allergenicity dataset/AllergenOnlineV21.xlsx')
accession_number_collection = data_list['Accession']
accession_num= accession_number_collection[0]
driver = webdriver.Chrome('/Users/zhenjiaodu/Downloads/chromedriver')
for accession_num in accession_number_collection:
    url = 'https://www.ncbi.nlm.nih.gov/protein/' + accession_num
    try:
        driver.get(url)
        # Find the element using its full XPath (website NCBI)
        time.sleep(2)
        # switch to it.
        # Find the start and end elements using their XPaths
        total_text = driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[1]/div[4]/div/div[5]/div[2]/div[1]/div/div/pre')
        # export text info
        export_information = total_text.text.split(' ')
        a = 0
        seq_col_1 = []
        import re
        export_information = [re.sub(r'\d+', '', s) for s in export_information]
        for seq in export_information:
            if 'ORIGIN' in seq:
                a = 1
            if a == 1:
                if len(seq)>0:
                    seq_col_1.append(seq)
        protein_sequences = []
        for element in seq_col_1:
            if element[0].islower():
                if '//' in element:
                    element = element.replace('//','')
                    protein_sequences.append(element.strip())
                else:
                    protein_sequences.append(element.strip())
        single_seq = str()
        for seq in protein_sequences:
            single_seq = single_seq+seq.upper()
        # collect all the sequence from these websites
        protein_sequence_collection.append(single_seq)
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
    except NoSuchElementException:
        continue

protein_sequence_collection
len(protein_sequence_collection)
pd.DataFrame(protein_sequence_collection).to_csv('AllergenOnlineV21_dataset.csv')



sequence_col = pd.read_csv('AllergenOnlineV21_dataset.csv',header = 0, index_col = 0)
sequence_col_new = []
for i in range(sequence_col.shape[0]):
    seq = sequence_col.iloc[i][0]
    if 'ORIGIN' in seq:
        origin_index = seq.index('ORIGIN')
        new_string = seq[origin_index:]
        new_string_1 = new_string[6:]
        sequence_col_new.append(new_string_1)
    else:
        sequence_col_new.append(seq)
sequence_col_new
pd.DataFrame(sequence_col_new).to_csv('AllergenOnlineV21_dataset.csv')
import os
