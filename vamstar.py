# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:55:17 2021

@author: APARNA
"""
import pandas as pd

class Health:
    def __init__(self,data):
        self.data = data
        self.analysis()
        
    
    def custom_algo(self,x):
        if x.BMI<=18.4:
            return "Underweight",'Malnutrition risk'
        elif 18.5<=x.BMI<= 24.9:
            return "Normal weight","Low risk"
        elif 25<=x.BMI<= 29.9:
            return "Overweight","Enhanced risk"
        elif 30<=x.BMI<= 34.9:
            return "Moderately obese","Medium risk"
        elif 35<=x.BMI<= 39.9:
            return "Severely obese","High risk"
        elif 40<=x.BMI:
            return "Very severely obese","Very high risk"
        else:
            pass
        
    def analysis(self):
        self.data_df = pd.DataFrame(self.data)
        self.data_df['BMI'] = self.data_df.apply(lambda x :round((x.WeightKg/(x.HeightCm/100)**2),2),axis =1)
        self.data_df[['BMI_Category','Health_risk']] = self.data_df.apply(self.custom_algo,axis = 1,result_type='expand')
        self.overweight_people = list(self.data_df[self.data_df["BMI_Category"] == "Overweight"].count())[0]
        print(self.data_df)
    
    def __repr__(self):
        return f"Total number of overweight people:{self.overweight_people}"

def main():
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    obj = Health(data)
    print(obj)
    
if __name__ == "__main__":
    main()