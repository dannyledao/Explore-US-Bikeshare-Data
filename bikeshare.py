import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhich city are you looking to explore?\n").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Invalid Input. Please check for typos.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month are you looking to explore? Please type either January, February, March, April, May, June or 'all'.\n").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Invalid Input. Please check for typos.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhich days of the week are you looking to explore? Please type eitehr: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all'.\n").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Invalid Input. Please check for typos.")
        continue
      else:
        break

    print('-'*30)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_common_month = df['month'].mode()[0]
    print('The most Common Month is:', most_common_month)


    # TO DO: display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print('The most Common day is:', most_common_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most Common Hour is:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*30)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Most_Common_Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Most_Common_Start_Station)


    # TO DO: display most commonly used end station

    Most_Common_End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', Most_Common_End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    print('\nThe Most Frequently used combination of start station and end station trip is:', Most_Common_Start_Station, " & ", Most_Common_End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*30)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('The Total travel time is:', Total_Travel_Time/3600, " Hours")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The Mean travel time is:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*30)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data is provided")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_YOB = df['Birth Year'].min()
      print('\nThe Earliest Year of Birth is:', Earliest_YOB)
    except KeyError:
      print("\nThe Earliest Year of Birth is:\nNo data is provided.")

    try:
      Most_Recent_YOB = df['Birth Year'].max()
      print('\nThe Most Recent Year of Birth is:', Most_Recent_YOB)
    except KeyError:
      print("\nThe Most Recent Year of Birth is:\nNo data is provided.")

    try:
      Most_Common_YOB = df['Birth Year'].value_counts().idxmax()
      print('\nThe Most Common Year of Birth is:', Most_Common_YOB)
    except KeyError:
      print("\nThe Most Common Year of Birth is:\nNo data is provided.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*30)
    
def display_raw_data(df):
    """
    prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', 
    and continue these prompts and displays until the user says 'no'.
    """
    raw_input = input('Would you like to view some raw observations? Please enter yes or no.\n')
    starting_point = 0
    while True: 
        if raw_input.lower() != 'no':
            print(df.iloc[starting_point : starting_point +5])
            starting_point += 5
            raw_input = input('Would you like to see additional observations?  Enter yes or no.\n')
        else:
            break 
           
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()