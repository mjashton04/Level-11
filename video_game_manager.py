import pandas as pd

#Read the CSV file using Pandas.
df = pd.read_csv("video_games_raw.csv")
#• Ask the user for a specific row number to inspect.
row_number = int(input("Enter the row number of the game you want to inspect: "))
#• Use .iloc[] to display information about the selected game.
print(df.iloc[row_number])
#• Ask the user to enter a new status for that game, such as Backlog, Playing, Completed,
#or Dropped.
new_status = input("Enter the new status for the game (Backlog, Playing, Completed, Dropped): ")
#• Use .at[] to update the selected game’s status.
df.at[row_number, "Status"] = new_status
#• Add a Recommended column to the panda.
df["Recommended"] = "No"
#• Set Recommended to Yes for games that meet both of these criteria:
df.loc[(df["Rating"] >= 8) & (df["Price"] <= 40), "Recommended"] = "Yes"
#o Rating is at least 8.
#o Price is $40 or less.
#• Set Recommended to No for all other games.
#• Use .query() to display the recommended games.
recommended_games = df.query('Recommended == "Yes"')
print("Recommended Games:")
print(recommended_games)
#• Save the updated data to a new file named video_games_cleaned.csv.
df.to_csv("video_games_cleaned.csv", index=False)