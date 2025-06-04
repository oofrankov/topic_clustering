#  Test Task

Detection of Main Topics in Media across Two Information Spaces
— Ukrainian and International News.

## Project structure

```
ds_test_task/
├── notebooks/
│   ├── international_research.ipynb  # International news analysis
│   └── ukrainian_research.ipynb      # Ukrainian news analysis
├── output/
│   ├── res_international.csv    # International research results
│   └── res_ukrainian.csv        # Ukrainian research results
├── src/
│   ├── __init__.py             # Package initialization
│   ├── custom_names.py         # Topic custom naming utilities
│   ├── preprocess.py           # Data preprocessing functions
│   └── save_results.py         # Results saving utilities
├── data.xlsx                   # Raw data file
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

## Setup instructions

1. Create a Virtual Environment
    ```bash
    python -m venv venv
    ```
   
2. Activate the Virtual Environment

   (Windows)

    ```bash
   venv\Scripts\Activate
    ```
   
    (macOS/Linux)
    ```bash
    source venv/bin/activate
    ```

3. Install the required dependencies:

   ```bash  
   pip install -r "requirements.txt"  
   ```
   
4. Install jupyter notebook if needed: 

   ```bash  
   pip install jupyter
   ```

## Usage

Run jupyter notebooks. They are in `notebooks` folder.

## About project pipeline

1. The topic clustering was implemented using BERTopic. It is a SOTA approach for this kind of task.
It performs better than other methods such as: LDA, NMF, Top2Vec.
It also has lower computational costs than LDA and NMF.
Additionally, BERTopic can identify outliers - documents that don't fit well into any topic cluster,
 which helps to filter out noise and irrelevant content from the analysis.

2. For clustering were used text attributes: `'Заголовок'` + `. ` + `'Опис'` (`Header` + `Description`)
and the day from `'Дата'` (`Date`).

3. International news are only in English. So to achieve better results was used BERTopic specified for English.
For Ukrainian - BERTopic multilingual. 

4. To avoid duplicates the amount of clusters was reduced to `50`. It helped to achieve the most unique topics.

5. For obtained topics were generated custom names, because BERTopic's ones are often uninformative. 
For the topic name I took the first sentence from the description. It's a very quick and simple approach.
It helps to avoid using additional summarizing models and makes topic names understandable. 

6. For analysis were built `intertopic distance map` and `topics over time graph`.

7. The most popular topics with their number of occurrences are saved in `output` folder in appropriate `.csv` files.

## Results

Created interactive plots and graphs that help to analyze news.

Ukrainian and international news are intersect in perspective of Russian-Ukrainian war: 
negotiations with Trump and shelling of Ukraine.