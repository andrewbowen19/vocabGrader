# Script to grade our vocab quizzes automaticall
# Takes in response sheet from google forms (csv) and outputs 4 class csv files

import os
import pandas as pd
import numpy as np
import datetime
from fractions import Fraction


my_path = os.path.join('.', 'sampleResponses.csv')
advisories = ['SHN', 'BOS', "'BNU Cats", 'Casa Amigos']
today = (datetime.datetime.now()).date()

def vocabGrader(path):
    '''
    Grades vocab quiz response csv
    '''
    print('Grading vocab quizzes...')

    scores = pd.read_csv(path)
    # print(scores['Score'])
    scores = scores[['What is your name?', 'Score', 'What is your homeroom?']]
    print(scores)
    scores.columns = ['Name', 'Score', 'Homeroom']

    for a in advisories:
        print(f'Getting data for {a}')
        dat = scores
        df = dat.loc[np.where(dat['Homeroom'] == a)]

        # reformatting data
        df['Score'] = [float(Fraction(x.replace(' ', '') )) * 100  for x in df['Score']]
        df['Name'] = [x.capitalize() for x in df['Name']] # Capitalizing names
        print(f'{a} scores:', df)

        # Printing stats
        print(f'{a} # of quizzes submitted: ', len(df))
        print(f'{a} class average:', np.mean(df['Score']))
        print(f'{a} class std dev: ', np.std(df['Score']))


        # print('Scholars of concern: ', df.loc[np.where(df['Score'] <= 50.)]['Name'])

        grades_path = os.path.join('grades', f'grades-{today}')
        if not os.path.isdir(grades_path):
            os.mkdir(grades_path)
        advisory_path_name = a.replace(' ', '-')
        file_name = f'vocab-grades-{advisory_path_name}-{today}.csv'
        file_path = os.path.join(grades_path, file_name)
        df.to_csv(file_path)
        
    


if __name__ == "__main__":
    vocabGrader(my_path)




