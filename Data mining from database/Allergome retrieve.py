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
import re
protein_sequence_collection = []
import os
os.getcwd()
data_list = pd.read_excel('/Users/zhenjiaodu/Downloads/allergenicity dataset/allergome_database.xlsx')
accession_number_collection = data_list['Code']
accession_num= accession_number_collection[1]
accession_number_collection
accession_num
driver = webdriver.Chrome('/Users/zhenjiaodu/Downloads/chromedriver')
accession_num = 5803
for accession_num in accession_number_collection:
    url = 'https://www.allergome.org/script/dettaglio.php?id_molecule=' + str(accession_num)
    try:
        driver.get(url)
        # Find the element using its full XPath (website NCBI)
        time.sleep(2)
        element = driver.find_element_by_xpath("/html/body/center/div/ul/li[2]/a")
        try:
            element.click()
            time.sleep(1)
            # switch to it.
            # driver.switch_to.window(driver.window_handles[-1])
            # Find the start and end elements using their XPaths
            total_text = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]')
            # export text info
            export_information = total_text.text.split('\n')
            export_information
            count_num_seq =0
            for seq in export_information:
                if seq =='Close':
                    count_num_seq = count_num_seq+1
            count_num_seq
            sequence_collection_single_web = []
            for count in range(count_num_seq):
                for seq in export_information:
                    if seq == 'Close':
                        extract_partial_list = export_information[:export_information.index('Close')+1]
                        extract_partial_list = [re.sub(r'\d+', '', s) for s in extract_partial_list] # delete number
                        export_information=export_information[export_information.index('Close')+1:]
                        for judge_item in extract_partial_list:
                            if 'NO' in judge_item or 'YES' in judge_item:
                                extract_partial_list = extract_partial_list[extract_partial_list.index(judge_item):]
                                break
                        extract_partial_list
                        single_seq = str()
                        capture = False
                        for item in extract_partial_list:
                            if item == "NO" or item == "YES":
                                capture = True
                            elif item == "Close":
                                capture = False
                            elif capture and item != '':
                                single_seq= single_seq + (item.strip())
                        sequence_collection_single_web.append(single_seq)
                        single_seq
            for seq in sequence_collection_single_web:
                # print(seq)
                protein_sequence_collection.append(seq)
                protein_sequence_collection
            # collect all the sequence from these websites
            driver.back()
        except NoSuchElementException:
            continue
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
    except NoSuchElementException:
        continue
count_num_seq
protein_sequence_collection
len(protein_sequence_collection)
pd.DataFrame(protein_sequence_collection).to_csv('Allergome.csv')


len(protein_sequence_collection)


protein_sequence_collection
