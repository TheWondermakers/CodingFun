import pandas as pd

data = {
    'product': ['tomato', 'apple', 'lemon', 'peach', 'watermelon'],
    'width': [12, 24, 13, 14, 23],
    'height': [13, 14, 15, 12, 30],
}
data = pd.DataFrame(data)


# TODO: create a new column named "size" that equals width * height


# TODO: sort the dataframe based on the new column "size"


# TODO: remove all but the two smallest products


# TODO: calculate the average size of the two smallest products


print(data)
