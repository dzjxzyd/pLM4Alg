# pLM4Alg
pLM4Alg: Protein Language Model-Based Predictors for Allergenic Proteins and Peptides
doi.org/10.1021/acs.jafc.3c07143

**Notice: pLM4Allergen is ONLY freely available for academic research; for commercial usage, please contact us**, zhenjiao@ksu.edu; yonghui@ksu.edu;


## Explaination of the datast
Allergenic sequences were labeled as 0 (positive) and non-allergenic sequence were labeled as 1 (negative). The dataset used in this study was compiled from four known public databases: CAMPARE, AllergenOnline, IUIS, and Uniprot. Datamining was used for AllergenOnline and IUIS (you can use our code for your latest dataset retrival). [See the data mining code.](https://github.com/dzjxzyd/pLM4Allergen/tree/main/Data%20mining%20from%20database)

## web server codes and correspinding models deployed at server
The original codes can be downloaded at [Google Drive](https://drive.google.com/drive/folders/1veD40uj8R7gpIo8y1niXtoKij_vZ3eiD?usp=sharing.)
 


## Requirements
Implementation platform Google Colab.
The majoy dependencies used in this project are as following:
```
Python 3.8.16
fair-esm 2.0.0
keras 2.9.0
pandas 1.3.5
numpy 1.21.6
scikit-learn 1.0.2
tensorflow 2.9.2
torch 1.13.0+cu116
h5py 1.21.6
```
More detailed python libraries used in this project are referred to requirements.txt. All the implementation can be down in Google Colab and all you need is just a browser and a google account. Install all the above packages by ```!pip install fair-esm==2.0.0```

## Further model tuning and modifications

In our experiments, we follow our previous architecture design [UniDL4BioPep](https://github.com/dzjxzyd/UniDL4BioPep/tree/main), and conduct a series paramaters tuning based on experiences, mainly focus on filter size selected from [16,32,64,128,256], kernel size selected from [3,6,9,12], stride selected from [1,2,4,8] and units selected from [32,64,128,256,512,1024,2048,4096,8192].

Feel free to make your personalized modifications. Just scroll down to the model architecture sections and make revisions to fit your expectation. Based on our experience in esm protein language models, our model architecture is quite reliable as your initial attempts on your own datasets. But, any attempts in new architecture design are highly encouraged. 
