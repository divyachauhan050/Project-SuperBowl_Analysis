# Whether or not you like football, the Super Bowl is a spectacle. 
# There's a little something for everyone at your Super Bowl party. 
# Drama in the form of blowouts, comebacks, and controversy for the sports fan. 
# There are the ridiculously expensive ads, some hilarious, others gut-wrenching, thought-provoking, and weird. 
# The half-time shows with the biggest musicians in the world, sometimes riding giant mechanical tigers or leaping from the roof of the stadium. 
# It's a show, baby. And in this notebook, we're going to find out how some of the elements of this show interact with each other. 
# After exploring and cleaning our data a little, we're going to answer questions like:

# What are the most extreme game outcomes?
# How does the game affect television viewership?
# How have viewership, TV ratings, and ad cost evolved over time?
# Who are the most prolific musicians in terms of halftime show performances?

# The dataset we'll use was scraped and polished from Wikipedia. 
# It is made up of three CSV files, one with game data, one with TV data, and one with halftime musician data for all 52 Super Bowls through 2018. 
# Let's take a look, using display() instead of print() since its output is much prettier in Jupyter Notebooks.

# Import pandas
import pandas as pd
# Import matplotlib and set plotting style
import matplotlib.pyplot as plt
# Import seaborn
import seaborn as sns

# Load the CSV data into DataFrames
super_bowls = pd.read_csv('Datasets/super_bowls.csv')
tv = pd.read_csv('Datasets/tv.csv')
halftime_musicians = pd.read_csv('Datasets/halftime_musicians.csv')

# Display the first five rows of each DataFrame
print(super_bowls.head())
print(tv.head())
print(halftime_musicians.head())

# Summary of the TV data to inspect
print(tv.info())

print('\n')

# Summary of the halftime musician data to inspect
print(halftime_musicians.info())

plt.style.use('seaborn')

# Plot a histogram of combined points
plt.hist(super_bowls['combined_pts'])
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls['combined_pts'] > 70])
print(super_bowls[super_bowls['combined_pts'] < 25])

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls['difference_pts'] == 1])
print(super_bowls[super_bowls['difference_pts'] >= 35])

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=games_tv)
plt.show()

# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color = '#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color = '#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout()
plt.show()

# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
print(halftime_musicians[halftime_musicians['super_bowl'] <= 27])

# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
print(halftime_appearances)
print(halftime_appearances[halftime_appearances['super_bowl'] > 1])

# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
print(no_bands.head(15))

# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = 'Los Angeles Rams'
print('\n')
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)