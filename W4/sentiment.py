# Packages
import os 
import pandas as pd
import spacy
import matplotlib.pyplot as plt
from spacytextblob.spacytextblob import SpacyTextBlob


# Achieving polarity
def polarity(df):
    polarity_scores = []

    for doc in nlp.pipe(df["headline_text"]):
        polarity_scores.append(doc._.sentiment.polarity)

    return polarity_scores


# Plot function 1
def plot_polarity(df, roll_val1 = 7, roll_val2 = 30, save = False):
    
    plt.figure(figsize=(10, 5))
    plt.plot(df.groupby("publish_date").mean("polarity").rolling(roll_val1).mean(), label = 'Weekly')
    plt.plot(df.groupby("publish_date").mean("polarity").rolling(roll_val2).mean(), label = 'Monthly')
    plt.title('Polarity scores for headlines')
    plt.xlabel('Date')
    plt.ylabel('Polarity score')
    plt.legend()
    if save == True:
        plt.savefig("polarity_plot.png")
    plt.show()
    
# Plot function 2
def plot_polarity(df, roll_val1 = 7, roll_val2 = 30, save = False):
    fig = plt.figure(figsize = (10.0, 3.0))
    axes_1 = fig.add_subplot(1,2,1) # 1 row , 3 columns, 1st column position
    axes_2 = fig.add_subplot(1,2,2) # 1 row , 3 columns, 2nd column position

     # axes_1.set_ylabel("polarity")
    axes_1.set_ylabel(f"Polarity (rolling mean of {roll_val1} days)")
    smoothed_sent_week = df.groupby("publish_date").mean("polarity").rolling(roll_val1).mean()
    axes_1.plot(smoothed_sent_week) # on the "canvas" we made above, plot the mean_val on the axes_1
    axes_1.legend("Week average",loc="upper left")
    ## axes_2.set_ylabel("polarity")
    axes_2.set_ylabel(f"Polarity average (rolling mean of {roll_val2} days)")
    smoothed_sent_month = df.groupby("publish_date").mean("polarity").rolling(roll_val2).mean()
    axes_2.plot(smoothed_sent_month) # on the "canvas" we made above, plot the mean_val on the axes_1
    axes_2.legend("Month average",loc="upper left")

    fig.tight_layout()
    if save == True:
        plt.savefig("polarity_plot.png")
    plt.show()
    
def main():
    # initialising spaCy
    nlp = spacy.load("en_core_web_sm")
    # defining path and csv
    path_to_csv = os.path.join("abc_data", "abcnews-date-text.csv")
    abc_news = pd.read_csv(path_to_csv)
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    # choosing 10000 rows as sample 
    sample = abc_news[1:10000]
    # changing dates
    sample["publish_date"]= pd.to_datetime(sample.publish_date, format="%Y%m%d")
    sample = date_change(sample)
    sample["polarity"] = polarity_scores
    plot_polarity(sample, save = True)

# Define behaviour when called from command line
if __name__=="__main__":
    main()
