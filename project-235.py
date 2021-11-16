import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

dataset=pd.read_csv('projectC234_EPL.csv')

Football_club=dataset['Club'].value_counts().head(20)

print(Football_club)

club_fig=go.Figure(data=[go.Pie(labels=Football_club.index,values=Football_club.values,hole=.5)])

club_fig.show()