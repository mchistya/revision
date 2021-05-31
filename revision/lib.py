def handle_duplicates(dataset):
    dataset=dataset.drop_duplicates()
    return dataset

def handle_na(dataset):
    # drop a column if 95% is missing values
    for i in dataset.columns:
        if dataset[i].isnan().sum()/len(dataset)<= 0.5:
            dataset.drop(columns=i,inplace=True)
    return dataset

